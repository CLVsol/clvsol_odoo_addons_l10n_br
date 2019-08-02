# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class PersonAux(models.Model):
    _inherit = 'clv.person_aux'

    @api.multi
    def do_person_aux_get_ref_address_data(self):

        for person_aux in self:

            _logger.info(u'>>>>> %s', person_aux.ref_address_id)

            if (person_aux.reg_state in ['draft', 'revised']) and \
               (person_aux.ref_address_id.id is not False):

                data_values = {}

                if person_aux.ref_address_id.id is not False:

                    data_values['ref_address_id'] = person_aux.ref_address_id.id

                    data_values['street'] = person_aux.ref_address_id.street
                    data_values['street_number'] = person_aux.ref_address_id.street_number
                    data_values['street2'] = person_aux.ref_address_id.street2
                    data_values['district'] = person_aux.ref_address_id.district
                    data_values['zip'] = person_aux.ref_address_id.zip
                    data_values['city'] = person_aux.ref_address_id.city
                    data_values['city_id'] = person_aux.ref_address_id.city_id.id
                    data_values['state_id'] = person_aux.ref_address_id.state_id.id
                    data_values['country_id'] = person_aux.ref_address_id.country_id.id
                    # data_values['phone'] = person_aux.ref_address_id.phone
                    # data_values['mobile'] = person_aux.ref_address_id.mobile

                _logger.info(u'>>>>>>>>>> %s', data_values)

                person_aux.write(data_values)
