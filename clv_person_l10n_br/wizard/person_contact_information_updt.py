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

        # super().do_person_contact_information_updt()

        person_count = 0
        for person in self.person_ids:

            person_count += 1

            _logger.info(u'%s %s %s', '>>>>>', person_count, person.name)

            if person.ref_address_id is not False:

                values = {}

                values['street'] = person.ref_address_id.street
                values['street2'] = person.ref_address_id.street2
                values['country_id'] = person.ref_address_id.country_id.id
                values['state_id'] = person.ref_address_id.state_id.id
                values['city'] = person.ref_address_id.city
                values['zip'] = person.ref_address_id.zip
                if self.updt_phone:
                    values['phone'] = person.ref_address_id.phone
                if self.updt_mobile:
                    values['mobile'] = person.ref_address_id.mobile
                if self.updt_email:
                    values['email'] = person.ref_address_id.email

                values['number'] = person.ref_address_id.number
                values['district'] = person.ref_address_id.district
                values['l10n_br_city_id'] = person.ref_address_id.l10n_br_city_id.id

                _logger.info(u'%s %s %s', '>>>>>>>>>>', 'values:', values)

                person.write(values)

        return True
