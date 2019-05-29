# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class Person(models.Model):
    _inherit = 'clv.person'

    @api.multi
    def do_person_get_ref_address_data(self):

        for person in self:

            _logger.info(u'>>>>> %s', person.ref_address_id)

            if (person.ref_address_id.id is not False):

                data_values = {}

                if person.ref_address_id.id is not False:

                    data_values['ref_address_id'] = person.ref_address_id.id

                    data_values['street'] = person.ref_address_id.street
                    data_values['stret_number'] = person.ref_address_id.stret_number
                    data_values['street2'] = person.ref_address_id.street2
                    data_values['district'] = person.ref_address_id.district
                    data_values['zip'] = person.ref_address_id.zip
                    data_values['city'] = person.ref_address_id.city
                    data_values['city_id'] = person.ref_address_id.city_id.id
                    data_values['state_id'] = person.ref_address_id.state_id.id
                    data_values['country_id'] = person.ref_address_id.country_id.id
                    # data_values['phone'] = person.ref_address_id.phone
                    # data_values['mobile'] = person.ref_address_id.mobile

                _logger.info(u'>>>>>>>>>> %s', data_values)

                person.write(data_values)

        return True
