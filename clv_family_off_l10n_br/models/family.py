# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class FamilyOff(models.Model):
    _inherit = 'clv.family_off'

    @api.multi
    def do_family_off_get_related_person_data(self):

        for family_off in self:

            _logger.info(u'>>>>> %s', family_off.related_person_id)

            # if (family_off.reg_state in ['draft', 'revised']) and \
            #    (family_off.related_person_id.id is not False):
            if (family_off.related_person_id.id is not False):

                data_values = {}
                data_values['name'] = family_off.related_person_id.name
                data_values['code'] = family_off.related_person_id.code
                data_values['gender'] = family_off.related_person_id.gender
                data_values['birthday'] = family_off.related_person_id.birthday
                data_values['responsible_id'] = family_off.related_person_id.responsible_id.id
                data_values['caregiver_id'] = family_off.related_person_id.caregiver_id.id

                if family_off.related_person_id.ref_address_id.id is not False:

                    data_values['ref_address_id'] = family_off.related_person_id.ref_address_id.id

                    data_values['street'] = family_off.related_person_id.ref_address_id.street
                    data_values['street_number'] = family_off.related_person_id.ref_address_id.street_number
                    data_values['street2'] = family_off.related_person_id.ref_address_id.street2
                    data_values['district'] = family_off.related_person_id.ref_address_id.district
                    data_values['zip'] = family_off.related_person_id.ref_address_id.zip
                    data_values['city'] = family_off.related_person_id.ref_address_id.city
                    data_values['city_id'] = family_off.related_person_id.ref_address_id.city_id.id
                    data_values['state_id'] = family_off.related_person_id.ref_address_id.state_id.id
                    data_values['country_id'] = family_off.related_person_id.ref_address_id.country_id.id
                    # data_values['phone'] = family_off.related_person_id.ref_address_id.phone
                    # data_values['mobile'] = family_off.related_person_id.ref_address_id.mobile

                if family_off.related_person_id.family_id.id is not False:

                    data_values['family_id'] = family_off.related_person_id.family_id.id

                _logger.info(u'>>>>>>>>>> %s', data_values)

                family_off.write(data_values)

        return True
