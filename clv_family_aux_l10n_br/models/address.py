# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class FamilyAux(models.Model):
    _inherit = 'clv.family_aux'

    @api.multi
    def do_family_aux_get_ref_address_data(self):

        for family_aux in self:

            _logger.info(u'>>>>> %s', family_aux.ref_address_id)

            if (family_aux.ref_address_id.id is not False):

                data_values = {}

                if family_aux.ref_address_id.id is not False:

                    data_values['ref_address_id'] = family_aux.ref_address_id.id

                    data_values['street'] = family_aux.ref_address_id.street
                    data_values['street_number'] = family_aux.ref_address_id.street_number
                    data_values['street2'] = family_aux.ref_address_id.street2
                    data_values['district'] = family_aux.ref_address_id.district
                    data_values['zip'] = family_aux.ref_address_id.zip
                    data_values['city'] = family_aux.ref_address_id.city
                    data_values['city_id'] = family_aux.ref_address_id.city_id.id
                    data_values['state_id'] = family_aux.ref_address_id.state_id.id
                    data_values['country_id'] = family_aux.ref_address_id.country_id.id
                    # data_values['phone'] = family_aux.ref_address_id.phone
                    # data_values['mobile'] = family_aux.ref_address_id.mobile

                _logger.info(u'>>>>>>>>>> %s', data_values)

                family_aux.write(data_values)

        return True
