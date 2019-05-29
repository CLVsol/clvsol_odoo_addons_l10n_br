# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class PersonOffContactInformationUpdate(models.TransientModel):
    _inherit = 'clv.person_off.contact_information_updt'

    @api.multi
    def do_person_off_contact_information_updt(self):
        self.ensure_one()

        super().do_person_off_contact_information_updt()

        for person_off in self.person_off_ids:

            _logger.info(u'%s %s', '>>>>>', person_off.name)

            person_off.street_number = person_off.ref_address_id.street_number
            person_off.district = person_off.ref_address_id.district
            person_off.city_id = person_off.ref_address_id.city_id

        return True
