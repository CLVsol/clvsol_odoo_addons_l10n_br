# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import models

_logger = logging.getLogger(__name__)


class PersonAux(models.Model):
    _inherit = 'clv.person_aux'

    # # @api.multi
    # def do_person_aux_get_related_person_data(self):

    #     for person_aux in self:

    #         _logger.info(u'>>>>> %s', person_aux.related_person_id)

    #         # if (person_aux.reg_state in ['draft', 'revised']) and \
    #         #    (person_aux.related_person_id.id is not False):
    #         if (person_aux.related_person_id.id is not False):

    #             data_values = {}
    #             data_values['name'] = person_aux.related_person_id.name
    #             data_values['code'] = person_aux.related_person_id.code
    #             data_values['gender'] = person_aux.related_person_id.gender
    #             data_values['birthday'] = person_aux.related_person_id.birthday
    #             data_values['responsible_id'] = person_aux.related_person_id.responsible_id.id
    #             data_values['caregiver_id'] = person_aux.related_person_id.caregiver_id.id

    #             data_values['street_name'] = person_aux.related_person_id.street_name
    #             data_values['street_number'] = person_aux.related_person_id.street_number
    #             data_values['street2'] = person_aux.related_person_id.street2
    #             data_values['district'] = person_aux.related_person_id.district
    #             data_values['zip'] = person_aux.related_person_id.zip
    #             data_values['city'] = person_aux.related_person_id.city
    #             data_values['city_id'] = person_aux.related_person_id.city_id.id
    #             data_values['state_id'] = person_aux.related_person_id.state_id.id
    #             data_values['country_id'] = person_aux.related_person_id.country_id.id
    #             # data_values['phone'] = person_aux.related_person_id.phone
    #             # data_values['mobile'] = person_aux.related_person_id.mobile

    #             data_values['ref_address_is_unavailable'] = person_aux.related_person_id.ref_address_is_unavailable

    #             if person_aux.related_person_id.ref_address_id.id is not False:

    #                 data_values['ref_address_id'] = person_aux.related_person_id.ref_address_id.id

    #             data_values['family_is_unavailable'] = person_aux.related_person_id.family_is_unavailable

    #             if person_aux.related_person_id.family_id.id is not False:

    #                 data_values['family_id'] = person_aux.related_person_id.family_id.id

    #             _logger.info(u'>>>>>>>>>> %s', data_values)

    #             person_aux.write(data_values)

    #     return True

    # # @api.multi
    # def do_person_aux_get_ref_address_data(self):

    #     for person_aux in self:

    #         _logger.info(u'>>>>> %s', person_aux.ref_address_id)

    #         # if (person_aux.reg_state in ['draft', 'revised']) and \
    #         #    (person_aux.ref_address_id.id is not False):
    #         if (person_aux.ref_address_id.id is not False):

    #             data_values = {}

    #             if person_aux.ref_address_id.id is not False:

    #                 data_values['ref_address_id'] = person_aux.ref_address_id.id

    #                 data_values['street_name'] = person_aux.ref_address_id.street_name
    #                 data_values['street_number'] = person_aux.ref_address_id.street_number
    #                 data_values['street2'] = person_aux.ref_address_id.street2
    #                 data_values['district'] = person_aux.ref_address_id.district
    #                 data_values['zip'] = person_aux.ref_address_id.zip
    #                 data_values['city'] = person_aux.ref_address_id.city
    #                 data_values['city_id'] = person_aux.ref_address_id.city_id.id
    #                 data_values['state_id'] = person_aux.ref_address_id.state_id.id
    #                 data_values['country_id'] = person_aux.ref_address_id.country_id.id
    #                 # data_values['phone'] = person_aux.ref_address_id.phone
    #                 # data_values['mobile'] = person_aux.ref_address_id.mobile

    #             _logger.info(u'>>>>>>>>>> %s', data_values)

    #             person_aux.write(data_values)

    # # @api.multi
    # def do_person_aux_get_ref_address_aux_data(self):

    #     for person_aux in self:

    #         _logger.info(u'>>>>> %s', person_aux.ref_address_aux_id)

    #         if (person_aux.reg_state in ['draft', 'revised']) and \
    #            (person_aux.ref_address_aux_id.id is not False):

    #             data_values = {}

    #             if person_aux.ref_address_aux_id.id is not False:

    #                 data_values['ref_address_aux_id'] = person_aux.ref_address_aux_id.id

    #                 data_values['street_name'] = person_aux.ref_address_aux_id.street_name
    #                 data_values['street_number'] = person_aux.ref_address_aux_id.street_number
    #                 data_values['street2'] = person_aux.ref_address_aux_id.street2
    #                 data_values['district'] = person_aux.ref_address_aux_id.district
    #                 data_values['zip'] = person_aux.ref_address_aux_id.zip
    #                 data_values['city'] = person_aux.ref_address_aux_id.city
    #                 data_values['city_id'] = person_aux.ref_address_aux_id.city_id.id
    #                 data_values['state_id'] = person_aux.ref_address_aux_id.state_id.id
    #                 data_values['country_id'] = person_aux.ref_address_aux_id.country_id.id
    #                 # data_values['phone'] = person_aux.ref_address_aux_id.phone
    #                 # data_values['mobile'] = person_aux.ref_address_aux_id.mobile

    #             _logger.info(u'>>>>>>>>>> %s', data_values)

    #             person_aux.write(data_values)

    #     return True

    # @api.multi
    def do_person_aux_clear_address_data(self):

        for person_aux in self:

            # _logger.info(u'>>>>> %s', person_aux.ref_address_id)

            # if (person_aux.reg_state in ['draft', 'revised']):

            data_values = {}

            data_values['street_name'] = False
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

            person_aux.write(data_values)

        return True
