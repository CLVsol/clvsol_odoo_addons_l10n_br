# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class PersonOff(models.Model):
    _inherit = 'clv.person_off'

    @api.multi
    def do_person_off_get_ref_address_data(self):

        for person_off in self:

            _logger.info(u'>>>>> %s', person_off.ref_address_id)

            if (person_off.reg_state in ['draft', 'revised']) and \
               (person_off.ref_address_id.id is not False):

                data_values = {}

                if person_off.ref_address_id.id is not False:

                    data_values['ref_address_id'] = person_off.ref_address_id.id

                    data_values['street'] = person_off.ref_address_id.street
                    data_values['street_number'] = person_off.ref_address_id.street_number
                    data_values['street2'] = person_off.ref_address_id.street2
                    data_values['district'] = person_off.ref_address_id.district
                    data_values['zip'] = person_off.ref_address_id.zip
                    data_values['city'] = person_off.ref_address_id.city
                    data_values['city_id'] = person_off.ref_address_id.city_id.id
                    data_values['state_id'] = person_off.ref_address_id.state_id.id
                    data_values['country_id'] = person_off.ref_address_id.country_id.id
                    # data_values['phone'] = person_off.ref_address_id.phone
                    # data_values['mobile'] = person_off.ref_address_id.mobile

                _logger.info(u'>>>>>>>>>> %s', data_values)

                person_off.write(data_values)

    @api.multi
    def do_person_off_clear_ref_address_data(self):

        for person_off in self:

            _logger.info(u'>>>>> %s', person_off.ref_address_id)

            if (person_off.reg_state in ['draft', 'revised']):

                data_values = {}

                data_values['street'] = False
                data_values['street_number'] = False
                data_values['street2'] = False
                data_values['district'] = False
                data_values['zip'] = False
                data_values['city'] = False
                data_values['city_id'] = False
                data_values['state_id'] = False
                data_values['country_id'] = False
                # data_values['phone'] = False
                # data_values['mobile'] = False

                _logger.info(u'>>>>>>>>>> %s', data_values)

                person_off.write(data_values)

        return True
