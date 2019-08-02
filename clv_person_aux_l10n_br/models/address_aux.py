# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class PersonAux(models.Model):
    _inherit = 'clv.person_aux'

    @api.multi
    def do_person_aux_get_ref_address_aux_data(self):

        for person_aux in self:

            _logger.info(u'>>>>> %s', person_aux.ref_address_aux_id)

            if (person_aux.reg_state in ['draft', 'revised']) and \
               (person_aux.ref_address_aux_id.id is not False):

                data_values = {}

                if person_aux.ref_address_aux_id.id is not False:

                    data_values['ref_address_aux_id'] = person_aux.ref_address_aux_id.id

                    data_values['street'] = person_aux.ref_address_aux_id.street
                    data_values['street_number'] = person_aux.ref_address_aux_id.street_number
                    data_values['street2'] = person_aux.ref_address_aux_id.street2
                    data_values['district'] = person_aux.ref_address_aux_id.district
                    data_values['zip'] = person_aux.ref_address_aux_id.zip
                    data_values['city'] = person_aux.ref_address_aux_id.city
                    data_values['city_id'] = person_aux.ref_address_aux_id.city_id.id
                    data_values['state_id'] = person_aux.ref_address_aux_id.state_id.id
                    data_values['country_id'] = person_aux.ref_address_aux_id.country_id.id
                    # data_values['phone'] = person_aux.ref_address_aux_id.phone
                    # data_values['mobile'] = person_aux.ref_address_aux_id.mobile

                _logger.info(u'>>>>>>>>>> %s', data_values)

                person_aux.write(data_values)

        return True
