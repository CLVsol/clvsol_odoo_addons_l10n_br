# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class Family(models.Model):
    _inherit = 'clv.family'

    use_district = fields.Boolean(
        string='Use District',
        help="If checked, the Family Name will contain the field District.",
        default=True
    )

    @api.depends('street', 'number', 'street2', 'district')
    def _get_suggested_name(self):
        for record in self:
            if record.street:
                record.suggested_name = record.street
                if record.use_district:
                    if record.district:
                        record.suggested_name = record.suggested_name + ' (' + record.district + ')'
                if record.number:
                    record.suggested_name = record.suggested_name + ', ' + record.number
                if record.street2:
                    record.suggested_name = record.suggested_name + ' - ' + record.street2
            # else:
            #     if not record.suggested_name:
            #         if record.code:
            #             record.suggested_name = record.code
