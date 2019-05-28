# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class FamilyOff(models.Model):
    _inherit = 'clv.family_off'

    @api.multi
    def do_family_off_get_ref_address_off_data(self):

        for family_off in self:

            _logger.info(u'>>>>> %s', family_off.ref_address_off_id)

            if (family_off.reg_state in ['draft', 'revised']) and \
               (family_off.ref_address_off_id.id is not False):

                data_values = {}

                if family_off.ref_address_off_id.id is not False:

                    data_values['ref_address_off_id'] = family_off.ref_address_off_id.id

                    data_values['street'] = family_off.ref_address_off_id.street
                    data_values['number'] = family_off.ref_address_off_id.number
                    data_values['street2'] = family_off.ref_address_off_id.street2
                    data_values['district'] = family_off.ref_address_off_id.district
                    data_values['zip'] = family_off.ref_address_off_id.zip
                    data_values['city'] = family_off.ref_address_off_id.city
                    data_values['l10n_br_city_id'] = family_off.ref_address_off_id.l10n_br_city_id.id
                    data_values['state_id'] = family_off.ref_address_off_id.state_id.id
                    data_values['country_id'] = family_off.ref_address_off_id.country_id.id
                    # data_values['phone'] = family_off.ref_address_off_id.phone
                    # data_values['mobile'] = family_off.ref_address_off_id.mobile

                _logger.info(u'>>>>>>>>>> %s', data_values)

                family_off.write(data_values)

        return True