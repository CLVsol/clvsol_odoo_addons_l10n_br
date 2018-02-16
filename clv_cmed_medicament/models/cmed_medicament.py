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


class CMEDMedicament(models.Model):
    _description = 'CMED Medicament'
    _name = 'clv.cmed.medicament'
    _inherit = 'clv.medicament.model'

    principio_ativo = fields.Char(string=u'Princípio Ativo')
    cnpj = fields.Char(string=u'CNPJ')
    latoratorio = fields.Char(string=u'Laboratório')
    codigo_ggrem = fields.Char(string=u'Código GGREM')
    registro = fields.Char(string=u'Registro')
    ean = fields.Char(string=u'EAN')
    produto = fields.Char(string=u'Produto')
    apresentacao = fields.Char(string=u'Apresentação')
    classe_terapeutica = fields.Char(string=u'Classe Terapêutica')
    tipo_status_produto = fields.Char(string=u'Tipo de Produto (Status do Produto)')

    restr_hospitalar = fields.Char(string=u'Restrição Hospitalar')
    cap = fields.Char(string=u'CAP')
    confaz_87 = fields.Char(string=u'CONFAZ 87')
    analise_recursal = fields.Char(string=u'Análise Recursal')
    pis_cofins = fields.Char(string=u'PIS/COFINS')
    comerc_2016 = fields.Char(string=u'Comercialização 2016')
    tarja = fields.Char(string=u'Tarja')

    _sql_constraints = [
        ('codigo_ggrem_uniq',
         'UNIQUE (codigo_ggrem)',
         u'Error! The GGREM Code must be unique!'),
    ]
