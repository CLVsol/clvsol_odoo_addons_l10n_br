# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class AddressAux(models.Model):
    _inherit = 'clv.address_aux'

    use_district = fields.Boolean(
        string='Use District',
        help="If checked, the Address Name will contain the field District.",
        default=True
    )

    @api.depends('street', 'street_number', 'street2', 'district')
    def _get_suggested_name(self):
        for record in self:
            if record.street:
                record.suggested_name = record.street
                if record.street_number:
                    record.suggested_name = record.suggested_name + ', ' + record.street_number
                if record.street2:
                    record.suggested_name = record.suggested_name + ' - ' + record.street2
                if record.use_district:
                    if record.district:
                        record.suggested_name = record.suggested_name + ' (' + record.district + ')'
            else:
                record.suggested_name = 'Address Name...'
            if record.automatic_set_name:
                if record.name != record.suggested_name:
                    record.name = record.suggested_name
