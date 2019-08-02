# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class FamilyAux(models.Model):
    _inherit = 'clv.family_aux'

    use_district = fields.Boolean(
        string='Use District',
        help="If checked, the Family Name will contain the field District.",
        default=True
    )

    @api.multi
    def do_family_aux_get_related_family_data(self):

        for family_aux in self:

            _logger.info(u'>>>>> %s', family_aux.related_family_id)

            # if (family_aux.reg_state in ['draft', 'revised']) and \
            #    (family_aux.related_family_id.id is not False):
            if (family_aux.related_family_id.id is not False):

                data_values = {}
                data_values['name'] = family_aux.related_family_id.name
                data_values['code'] = family_aux.related_family_id.code

                if self.related_family_id.ref_address_id.id is not False:

                    data_values['ref_address_id'] = family_aux.related_family_id.ref_address_id.id

                    data_values['street'] = family_aux.related_family_id.street
                    data_values['street_number'] = family_aux.related_family_id.street_number
                    data_values['street2'] = family_aux.related_family_id.street2
                    data_values['district'] = family_aux.related_family_id.district
                    data_values['zip'] = family_aux.related_family_id.zip
                    data_values['city'] = family_aux.related_family_id.city
                    data_values['city_id'] = family_aux.related_family_id.city_id.id
                    data_values['state_id'] = family_aux.related_family_id.state_id.id
                    data_values['country_id'] = family_aux.related_family_id.country_id.id
                    data_values['phone'] = family_aux.related_family_id.phone
                    data_values['mobile'] = family_aux.related_family_id.mobile

                _logger.info(u'>>>>>>>>>> %s', data_values)

                family_aux.write(data_values)

        return True
