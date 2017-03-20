# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import api, fields, models

import re


class Address(models.Model):
    _inherit = 'clv.address'

    l10n_br_city_id = fields.Many2one(
        comodel_name='l10n_br_base.city',
        string='City',
        domain="[('state_id','=',state_id)]"
    )
    district = fields.Char(string='District')
    number = fields.Char(string='Number')

    @api.model
    def _display_address(self):

        if self.country_id and self.country_id.code != 'BR':
            # this ensure other localizations could do what they want
            return super(Address, self)._display_address(
                self,
                without_company=False)
        else:
            address_format = (
                self.country_id and
                self.country_id.address_format or
                "%(street)s\n%(street2)s\n%(city)s %(state_code)s"
                "%(zip)s\n%(country_name)s")
            args = {
                'state_code': self.state_id and self.state_id.code or '',
                'state_name': self.state_id and self.state_id.name or '',
                'country_code': self.country_id and
                self.country_id.code or '',
                'country_name': self.country_id and
                self.country_id.name or '',
                'l10n_br_city_name': self.l10n_br_city_id and
                self.l10n_br_city_id.name or '',
            }
            address_field = ['street', 'street2', 'zip', 'city',
                             'number', 'district']
            for field in address_field:
                args[field] = getattr(self, field) or ''
            return address_format % args

    @api.onchange('l10n_br_city_id')
    def onchange_l10n_br_city_id(self):
        if self.l10n_br_city_id:
            self.city = self.l10n_br_city_id.name
            self.l10n_br_city_id = self.l10n_br_city_id

    @api.onchange('zip')
    def onchange_mask_zip(self):
        if self.zip:
            val = re.sub('[^0-9]', '', self.zip)
            if len(val) == 8:
                zip = "%s-%s" % (val[0:5], val[5:8])
                self.zip = zip

    @api.model
    def _address_fields(self):
        address_fields = super(Address, self)._address_fields()
        return list(address_fields + ['l10n_br_city_id', 'number', 'district'])


class Address_2(models.Model):
    _inherit = 'clv.address'

    @api.multi
    def zip_search(self):
        self.ensure_one()
        obj_zip = self.env['l10n_br.zip']

        zip_ids = obj_zip.zip_search_multi(
            country_id=self.country_id.id,
            state_id=self.state_id.id,
            l10n_br_city_id=self.l10n_br_city_id.id,
            district=self.district,
            street=self.street,
            zip_code=self.zip,
        )

        if len(zip_ids) == 1:
            result = obj_zip.set_result(zip_ids[0])
            self.write(result)
            return True
        else:
            if len(zip_ids) > 1:
                obj_zip_result = self.env['l10n_br.zip.result']
                zip_ids = obj_zip_result.map_to_zip_result(
                    zip_ids, self._name, self.id)

                return obj_zip.create_wizard(
                    self._name,
                    self.id,
                    country_id=self.country_id.id,
                    state_id=self.state_id.id,
                    l10n_br_city_id=self.l10n_br_city_id.id,
                    district=self.district,
                    street=self.street,
                    zip_code=self.zip,
                    zip_ids=[zip.id for zip in zip_ids]
                )
            else:
                raise Warning(('Warning. No records found!'))


class Address_3(models.Model):
    _inherit = 'clv.address'

    @api.depends('street', 'number', 'street2')
    def _get_suggested_name(self):
        for record in self:
            if record.street:
                record.suggested_name = record.street
                if record.number:
                    record.suggested_name = record.suggested_name + ', ' + record.number
                if record.street2:
                    record.suggested_name = record.suggested_name + ' - ' + record.street2
            else:
                if not record.suggested_name:
                    if record.code:
                        record.suggested_name = record.code
            if record.automatic_set_name:
                record.name = record.suggested_name
