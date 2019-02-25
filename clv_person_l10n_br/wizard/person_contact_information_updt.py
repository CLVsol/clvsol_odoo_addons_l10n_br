# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class PersonContactInformationUpdate(models.TransientModel):
    _inherit = 'clv.person.contact_information_updt'

    @api.multi
    def do_person_contact_information_updt(self):
        self.ensure_one()

        super().do_person_contact_information_updt()

        for person in self.person_ids:

            _logger.info(u'%s %s', '>>>>>', person.name)

            person.number = person.ref_address_id.number
            person.district = person.ref_address_id.district
            person.l10n_br_city_id = person.ref_address_id.l10n_br_city_id

        return True
