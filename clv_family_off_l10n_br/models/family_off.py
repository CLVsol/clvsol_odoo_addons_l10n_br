# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class FamilyOff(models.Model):
    _inherit = 'clv.family_off'

    use_district = fields.Boolean(
        string='Use District',
        help="If checked, the Family Name will contain the field District.",
        default=True
    )

    @api.depends('street', 'street_number', 'street2', 'district')
    def _get_suggested_name(self):
        for record in self:
            if record.street:
                record.suggested_name = record.street
                if record.street_number:
                    record.suggested_name = record.suggested_name + ', ' + record.street_number
                if record.street2:
                    record.suggested_name = record.suggested_name + ' - ' + record.street2
                if record.use_district:
                    if record.district:
                        record.suggested_name = record.suggested_name + ' (' + record.district + ')'
            elif record.name:
                record.suggested_name = record.name
            else:
                record.suggested_name = 'x'
            # else:
            #     if not record.suggested_name:
            #         if record.code:
            #             record.suggested_name = record.code

    @api.multi
    def do_family_off_get_related_family_data(self):

        for family_off in self:

            _logger.info(u'>>>>> %s', family_off.related_family_id)

            # if (family_off.reg_state in ['draft', 'revised']) and \
            #    (family_off.related_family_id.id is not False):
            if (family_off.related_family_id.id is not False):

                data_values = {}
                # data_values['name'] = family_off.related_family_id.name
                data_values['code'] = family_off.related_family_id.code

                data_values['street'] = family_off.related_family_id.street
                data_values['street_number'] = family_off.related_family_id.street_number
                data_values['street2'] = family_off.related_family_id.street2
                data_values['district'] = family_off.related_family_id.district
                data_values['zip'] = family_off.related_family_id.zip
                data_values['city'] = family_off.related_family_id.city
                data_values['city_id'] = family_off.related_family_id.city_id.id
                data_values['state_id'] = family_off.related_family_id.state_id.id
                data_values['country_id'] = family_off.related_family_id.country_id.id
                data_values['phone'] = family_off.related_family_id.phone
                data_values['mobile'] = family_off.related_family_id.mobile

                _logger.info(u'>>>>>>>>>> %s', data_values)

                family_off.write(data_values)

        return True
