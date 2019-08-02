# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class FamilyAux(models.Model):
    _inherit = 'clv.family_aux'

    @api.multi
    def do_family_aux_clear_address_data(self):

        for family_aux in self:

            # _logger.info(u'>>>>> %s', family_aux.ref_address_id)

            # if (family_aux.reg_state in ['draft', 'revised']):

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

            family_aux.write(data_values)

        return True