# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _set_street(self):
        company_country = self.env.user.company_id.country_id
        if company_country.code is not False:
            if company_country.code.upper() != 'BR':
                return super()._set_street()
