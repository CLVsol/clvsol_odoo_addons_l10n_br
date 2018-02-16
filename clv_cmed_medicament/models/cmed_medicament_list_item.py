# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import fields, models


class CMEDMedicamentListItem(models.Model):
    _description = 'CMED Medicament List Item'
    _name = 'clv.cmed.medicament.list.item'
    _order = 'order'

    list_id = fields.Many2one(
        comodel_name='clv.cmed.medicament.list',
        string='CMED List',
        help='CMED List',
        required=False
    )
    medicament_id = fields.Many2one(
        comodel_name='clv.cmed.medicament',
        string='Medicament',
        help='CMED Medicament',
        required=False
    )

    notes = fields.Text(string='Notes')

    order = fields.Integer(string='Order', default=10)

    pf_0 = fields.Float(string='PF 0%')
    pf_12 = fields.Float(string='PF 12%')
    pf_17 = fields.Float(string='PF 17%')
    pf_17_alc = fields.Float(string='PF 17% ALC')
    pf_17_5 = fields.Float(string='PF 17,5%')
    pf_18 = fields.Float(string='PF 18%')
    pf_18_alc = fields.Float(string='PF 18% ALC')
    pf_20 = fields.Float(string='PF 20%')
    pmc_0 = fields.Float(string='PMC 0%')
    pmc_12 = fields.Float(string='PMC 12%')
    pmc_17 = fields.Float(string='PMC 17%')
    pmc_17_alc = fields.Float(string='PMC 17% ALC')
    pmc_17_5 = fields.Float(string='PMC 17,5%')
    pmc_18 = fields.Float(string='PMC 18%')
    pmc_18_alc = fields.Float(string='PMC 18% ALC')
    pmc_20 = fields.Float(string='PMC 20%')

    active = fields.Boolean(string='Active', default=1)


class CMEDMedicamentList(models.Model):
    _inherit = 'clv.cmed.medicament.list'

    cmed_list_item_ids = fields.One2many(
        comodel_name='clv.cmed.medicament.list.item',
        inverse_name='list_id',
        string='CMED List Itens'
    )
