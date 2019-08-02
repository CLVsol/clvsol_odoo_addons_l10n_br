# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class PersonAuxContactInformationUpdate(models.TransientModel):
    _inherit = 'clv.person_aux.contact_information_updt'

    @api.multi
    def do_person_aux_contact_information_updt(self):
        self.ensure_one()

        super().do_person_aux_contact_information_updt()

        for person_aux in self.person_aux_ids:

            _logger.info(u'%s %s', '>>>>>', person_aux.name)

            person_aux.street_number = person_aux.ref_address_id.street_number
            person_aux.district = person_aux.ref_address_id.district
            person_aux.city_id = person_aux.ref_address_id.city_id

        return True
