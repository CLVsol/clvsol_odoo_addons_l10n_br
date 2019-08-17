# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class FamilyAux(models.Model):
    _inherit = 'clv.family_aux'

    use_district = fields.Boolean(
        string='Use District',
        help="If checked, the Family Name will contain the field District.",
        default=True
    )

    @api.depends('street', 'street_number', 'street2', 'district')
    def _get_suggested_name(self):
        for record in self:
            if record.street:
                address_name = record.street
                if record.street_number:
                    address_name = address_name + ', ' + record.street_number
                if record.street2:
                    address_name = address_name + ' - ' + record.street2
                if record.use_district:
                    if record.district:
                        address_name = address_name + ' (' + record.district + ')'
                family_name_format = self.env['ir.config_parameter'].sudo().get_param(
                    'clv.global_settings.current_family_name_format', '').strip()
                family_name = family_name_format.replace('<address_name>', address_name)
                record.suggested_name = family_name
            else:
                record.suggested_name = 'Family Name...'
