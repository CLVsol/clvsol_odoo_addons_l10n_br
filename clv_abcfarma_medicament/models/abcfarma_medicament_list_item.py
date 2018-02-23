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


class ABCFarmaMedicamentListItem(models.Model):
    _description = 'ABCFarma Medicament List Item'
    _name = 'clv.abcfarma.medicament.list.item'
    _order = 'order'

    list_id = fields.Many2one(
        comodel_name='clv.abcfarma.medicament.list',
        string='ABCFarma List',
        help='ABCFarma List',
        required=False
    )
    medicament_id = fields.Many2one(
        comodel_name='clv.abcfarma.medicament',
        string='Medicament',
        help='ABCFarma Medicament',
        required=False
    )

    notes = fields.Text(string='Notes')

    order = fields.Integer(string='Order', default=10)

    med_pla1 = fields.Float(string='MED_PLA1')
    med_pco1 = fields.Float(string='MED_PCO1')
    med_fra1 = fields.Float(string='MED_FRA1')
    med_pla0 = fields.Float(string='MED_PLA0')
    med_pco0 = fields.Float(string='MED_PCO0')
    med_fra0 = fields.Float(string='MED_FRA0')

    # med_pco18 = fields.Float(string='MED_PCO18')
    # med_pla18 = fields.Float(string='MED_PLA18')
    # med_fra18 = fields.Float(string='MED_FRA18')
    # med_pco17 = fields.Float(string='MED_PCO17')
    # med_pla17 = fields.Float(string='MED_PLA17')
    # med_fra17 = fields.Float(string='MED_FRA17')
    # med_pco12 = fields.Float(string='MED_PCO12')
    # med_pla12 = fields.Float(string='MED_PLA12')
    # med_fra12 = fields.Float(string='MED_FRA12')
    # med_pco19 = fields.Float(string='MED_PCO19')
    # med_pla19 = fields.Float(string='MED_PLA19')
    # med_fra19 = fields.Float(string='MED_FRA19')
    # med_pcozfm = fields.Float(string='MED_PCOZFM')
    # med_plazfm = fields.Float(string='MED_PLAZFM')
    # med_frazfm = fields.Float(string='MED_FRAZFM')
    # med_pco0 = fields.Float(string='MED_PCO0')
    # med_pla0 = fields.Float(string='MED_PLA0')
    # med_fra0 = fields.Float(string='MED_FRA0')

    # med_pla20 = fields.Float(string='MED_PLA20')
    # med_pco20 = fields.Float(string='MED_PCO20')
    # med_fra20 = fields.Float(string='MED_FRA20')
    # med_pla175 = fields.Float(string='MED_PLA175')
    # med_pco175 = fields.Float(string='MED_PCO175')
    # med_fra175 = fields.Float(string='MED_FRA175')
    # med_plaz18 = fields.Float(string='MED_PLAZ18')
    # med_pcoz18 = fields.Float(string='MED_PCOZ18')
    # med_fraz18 = fields.Float(string='MED_FRAZ18')
    # med_plaz17 = fields.Float(string='MED_PLAZ17')
    # med_pcoz17 = fields.Float(string='MED_PCOZ17')
    # med_fraz17 = fields.Float(string='MED_FRAZ17')
    # med_plz175 = fields.Float(string='MED_PLZ175')
    # med_pcz175 = fields.Float(string='MED_PCZ175')
    # med_frz175 = fields.Float(string='MED_FRZ175')

    active = fields.Boolean(string='Active', default=1)


class ABCFarmaMedicamentList(models.Model):
    _inherit = 'clv.abcfarma.medicament.list'

    abcfarma_list_item_ids = fields.One2many(
        comodel_name='clv.abcfarma.medicament.list.item',
        inverse_name='list_id',
        string='ABCFarma List Itens'
    )
