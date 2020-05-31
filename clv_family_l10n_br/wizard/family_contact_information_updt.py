# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import models

_logger = logging.getLogger(__name__)


class FamilyContactInformationUpdate(models.TransientModel):
    _inherit = 'clv.family.contact_information_updt'

    # @api.multi
    def do_family_contact_information_updt(self):
        self.ensure_one()

        # super().do_family_contact_information_updt()

        family_count = 0
        for family in self.family_ids:

            family_count += 1

            _logger.info(u'%s %s %s', '>>>>>', family_count, family.name)

            if family.ref_address_id is not False:

                values = {}

                values['street'] = family.ref_address_id.street
                values['street2'] = family.ref_address_id.street2
                values['country_id'] = family.ref_address_id.country_id.id
                values['state_id'] = family.ref_address_id.state_id.id
                values['city'] = family.ref_address_id.city
                values['zip'] = family.ref_address_id.zip
                if self.updt_phone:
                    values['phone'] = family.ref_address_id.phone
                if self.updt_mobile:
                    values['mobile'] = family.ref_address_id.mobile
                if self.updt_email:
                    values['email'] = family.ref_address_id.email

                values['street_number'] = family.ref_address_id.street_number
                values['district'] = family.ref_address_id.district
                values['city_id'] = family.ref_address_id.city_id.id

                _logger.info(u'%s %s %s', '>>>>>>>>>>', 'values:', values)

                family.write(values)

        return True
