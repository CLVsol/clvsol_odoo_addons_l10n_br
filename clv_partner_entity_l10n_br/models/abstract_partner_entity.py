# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class AbstractPartnerEntity(models.AbstractModel):
    _inherit = 'clv.abstract.partner_entity'

    def zip_search(self):
        self.ensure_one()
        return self.env['l10n_br.zip'].zip_search(self)
