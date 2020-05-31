# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import models

_logger = logging.getLogger(__name__)


class PersonAssociateToFamily(models.TransientModel):
    _inherit = 'clv.person.associate_to_family'

    # @api.multi
    def do_person_associate_to_family(self):
        self.ensure_one()

        # super().do_person_associate_to_family()

        person_count = 0
        for person in self.person_ids:

            person_count += 1

            _logger.info(u'%s %s %s', '>>>>>', person_count, person.name)

            if person.ref_address_id.id is not False:

                Family = self.env['clv.family']
                family = Family.search([
                    ('ref_address_id', '=', person.ref_address_id.id),
                ])
                _logger.info(u'%s %s %s', '>>>>>>>>>>', 'family_id:', family.id)

                if family.id is not False:

                    values = {}
                    values['family_id'] = family.id
                    _logger.info(u'%s %s %s', '>>>>>>>>>>', 'values:', values)
                    person.write(values)

                else:

                    if self.create_new_family:

                        values = {}
                        values['name'] = person.ref_address_id.name

                        _logger.info(u'%s %s %s', '>>>>>>>>>>', 'values:', values)
                        new_family = Family.create(values)
                        _logger.info(u'%s %s %s', '>>>>>>>>>>', 'new_family:', new_family)

                        values = {}
                        values['code'] = '/'
                        values['phase_id'] = person.phase_id.id
                        values['street'] = person.ref_address_id.street
                        values['street2'] = person.ref_address_id.street2
                        values['country_id'] = person.ref_address_id.country_id.id
                        values['state_id'] = person.ref_address_id.state_id.id
                        values['city'] = person.ref_address_id.city
                        values['zip'] = person.ref_address_id.zip
                        values['phone'] = person.ref_address_id.phone
                        values['mobile'] = person.ref_address_id.mobile
                        values['email'] = person.ref_address_id.email
                        values['street_number'] = person.ref_address_id.street_number
                        values['district'] = person.ref_address_id.district
                        values['city_id'] = person.ref_address_id.city_id.id
                        _logger.info(u'%s %s %s', '>>>>>>>>>>', 'values:', values)
                        new_family.write(values)

                        values = {}
                        values['ref_address_id'] = person.ref_address_id.id
                        _logger.info(u'%s %s %s', '>>>>>>>>>>', 'values:', values)
                        new_family.write(values)

                        values = {}
                        values['family_id'] = new_family.id
                        _logger.info(u'%s %s %s', '>>>>>>>>>>', 'values:', values)
                        person.write(values)

                        if self.associate_all_persons_from_ref_address:

                            Person = self.env['clv.person']
                            persons = Person.search([
                                ('ref_address_id', '=', person.ref_address_id.id),
                            ])

                            for other_person in persons:

                                _logger.info(u'%s %s %s', '>>>>>>>>>>', 'other_person:', other_person)
                                values = {}
                                values['family_id'] = new_family.id
                                _logger.info(u'%s %s %s', '>>>>>>>>>>', 'values:', values)
                                other_person.write(values)

        return True
