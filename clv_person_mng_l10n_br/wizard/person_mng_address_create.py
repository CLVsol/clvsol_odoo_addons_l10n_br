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

import logging

from odoo import api, models
from odoo import exceptions

_logger = logging.getLogger(__name__)


class PersonMngAddressCreate(models.TransientModel):
    _inherit = 'clv.person.mng.address_create'

    @api.multi
    def do_person_mng_address_create(self):
        self.ensure_one()

        if self.history_marker_id.id is False:
            raise exceptions.ValidationError('The "History Marker" has not been defined!')
            return self._reopen_form()

        Address = self.env['clv.address']

        for person_mng in self.person_mng_ids:

            _logger.info(u'>>>>> %s', person_mng.name)

            if person_mng.action_address == 'create':

                if person_mng.address_id.id is False:

                    suggested_name = False
                    if person_mng.street:
                        suggested_name = person_mng.street
                        if person_mng.number:
                            suggested_name = suggested_name + ', ' + person_mng.number
                        if person_mng.street2:
                            suggested_name = suggested_name + ' - ' + person_mng.street2

                    if suggested_name is not False:

                        l10n_br_city_id = False
                        if person_mng.l10n_br_city_id is not False:
                            l10n_br_city_id = person_mng.l10n_br_city_id.id

                        state_id = False
                        if person_mng.state_id is not False:
                            state_id = person_mng.state_id.id

                        country_id = False
                        if person_mng.country_id is not False:
                            country_id = person_mng.country_id.id

                        new_category_ids = False
                        if person_mng.addr_category_ids is not False:

                            new_category_ids = []
                            for category_id in person_mng.addr_category_ids:

                                new_category_ids.append((4, category_id.id))

                        values = {
                            'name': suggested_name,
                            'street': person_mng.street,
                            'number': person_mng.number,
                            'street2': person_mng.street2,
                            'district': person_mng.district,
                            'zip': person_mng.zip,
                            'l10n_br_city_id': l10n_br_city_id,
                            'city': person_mng.city,
                            'state_id': state_id,
                            'country_id': country_id,
                            'phone': person_mng.phone,
                            'mobile': person_mng.mobile,
                            'category_ids': new_category_ids,
                            'history_marker_id': self.history_marker_id.id,
                        }
                        _logger.info(u'>>>>> %s', values)
                        new_address = Address.create(values)
                        new_address.code = '/'

                        person_mng.address_id = new_address.id

                        _logger.info(u'>>>>>>>>>> %s: %s', 'action_address', person_mng.action_address)

                        person_mng.action_address = 'none'

        return True
