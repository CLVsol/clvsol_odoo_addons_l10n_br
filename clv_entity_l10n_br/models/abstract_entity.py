# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo import models, api


class AbstractEntity(models.AbstractModel):
    _inherit = 'clv.abstract.entity'

    @api.multi
    def zip_search(self):
        self.ensure_one()
        return self.env['l10n_br.zip'].zip_search(self)
