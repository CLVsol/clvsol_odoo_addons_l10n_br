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


class ABCFarmaMedicament(models.Model):
    _description = 'ABCFarma Medicament'
    _name = 'clv.abcfarma.medicament'
    _inherit = 'clv.medicament.model'

    med_abc = fields.Char(string='MED_ABC')
    med_ctr = fields.Char(string='MED_CTR')
    med_lab = fields.Char(string='MED_LAB')
    lab_nom = fields.Char(string='LAB_NOM')
    med_des = fields.Char(string='MED_DES')
    med_apr = fields.Char(string='MED_APR')
    med_barra = fields.Char(string='MED_BARRA')
    # med_gene = fields.Char(string='MED_GENE')
    med_negpos = fields.Char(string='MED_NEGPOS')
    med_princi = fields.Char(string='MED_PRINCI')

    med_uni = fields.Float(string='MED_UNI')
    med_ipi = fields.Float(string='MED_IPI')
    med_dtvig = fields.Date(string='MED_DTVIG')
    exp_13 = fields.Boolean(string='EXP_13')
    med_regims = fields.Char(string='MED_REGIMS')
    med_varpre = fields.Char(string='MED_VARPRE')

    med_tipmed = fields.Char(string='MED_TRIPMED')
    med_ref = fields.Char(string='MED_REF')
    med_ncm = fields.Char(string='MED_NCM')
    med_dcb = fields.Char(string='MED_DCB')
    med_cas = fields.Char(string='MED_CAS')
    med_atc = fields.Char(string='MED_ATC')
    med_clater = fields.Char(string='MED_CLATER')
    med_tarja = fields.Char(string='MED_TARJA')
    med_por344 = fields.Char(string='MED_POR344')
    med_tiss = fields.Char(string='MED_TISS')
    med_conf87 = fields.Char(string='MED_CONF87')
    med_cap = fields.Char(string='MED_CAP')

    _sql_constraints = [
        ('med_abc_uniq',
         'UNIQUE (med_abc)',
         u'Error! The ABCFarma Code must be unique!'),
    ]
