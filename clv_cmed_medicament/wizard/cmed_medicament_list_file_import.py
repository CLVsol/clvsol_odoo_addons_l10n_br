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
# You should have uploadd a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import logging
import xlrd
from time import time

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % reduce(lambda ll, b: divmod(ll[0], b) + ll[1:], [(t * 1000,), 1000, 60, 60])


def get_fields():

    '''

    fields[field_str] = [col_nr, field_header_str, is_medicament_field, is_item_field]

    '''

    fields = {}

    fields['principio_ativo'] = [False, u'PRINCÍPIO ATIVO', True, False]
    fields['cnpj'] = [False, u'CNPJ', True, False]
    fields['latoratorio'] = [False, u'LABORATÓRIO', True, False]
    fields['codigo_ggrem'] = [False, u'CÓDIGO GGREM', True, False]
    fields['registro'] = [False, u'REGISTRO', True, False]
    fields['ean'] = [False, u'EAN', True, False]
    fields['produto'] = [False, u'PRODUTO', True, False]
    fields['apresentacao'] = [False, u'APRESENTAÇÃO', True, False]
    fields['classe_terapeutica'] = [False, u'CLASSE TERAPÊUTICA', True, False]
    fields['tipo_status_produto'] = [False, u'TIPO DE PRODUTO (STATUS DO PRODUTO)', True, False]

    fields['restr_hospitalar'] = [False, u'RESTRIÇÃO HOSPITALAR', True, False]
    fields['cap'] = [False, u'CAP', True, False]
    fields['confaz_87'] = [False, u'CONFAZ 87', True, False]
    fields['analise_recursal'] = [False, u'ANÁLISE RECURSAL', True, False]
    fields['pis_cofins'] = [False, u'LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)', True, False]
    fields['comerc_2016'] = [False, u'COMERCIALIZAÇÃO 2016, True, False']
    fields['tarja'] = [False, u'TARJA', True, False]

    fields['pf_0'] = [False, u'PF 0%', False, True]
    fields['pf_12'] = [False, u'PF 12%', False, True]
    fields['pf_17'] = [False, u'PF 17%', False, True]
    fields['pf_17_alc'] = [False, u'PF 17% ALC', False, True]
    fields['pf_17_5'] = [False, u'PF 17,5%', False, True]
    fields['pf_17_5_alc'] = [False, u'PF 17,5% ALC', False, True]
    fields['pf_18'] = [False, u'PF 18%', False, True]
    fields['pf_18_alc'] = [False, u'PF 18% ALC', False, True]
    fields['pf_20'] = [False, u'PF 20%', False, True]
    fields['pmc_0'] = [False, u'PMC 0%', False, True]
    fields['pmc_12'] = [False, u'PMC 12%', False, True]
    fields['pmc_17'] = [False, u'PMC 17%', False, True]
    fields['pmc_17_alc'] = [False, u'PMC 17% ALC', False, True]
    fields['pmc_17_5'] = [False, u'PMC 17,5%', False, True]
    fields['pmc_17_5_alc'] = [False, u'PMC 17,5% ALC', False, True]
    fields['pmc_18'] = [False, u'PMC 18%', False, True]
    fields['pmc_18_alc'] = [False, u'PMC 18% ALC', False, True]
    fields['pmc_20'] = [False, u'PMC 20%', False, True]

    return fields


class CMEDMedicamentListFileImport(models.TransientModel):
    _name = 'clv.cmed.medicament.list.file_import'

    def _default_directory_id(self):
        cmed_medicament_list = self.env['clv.cmed.medicament.list'].browse(self._context.get('active_id'))
        directory_id = cmed_medicament_list.directory_id.id
        return directory_id
    directory_id = fields.Many2one(
        comodel_name='clv.file_system.directory',
        string='Directory',
        readonly=True,
        default=_default_directory_id
    )

    def _default_file_name(self):
        cmed_medicament_list = self.env['clv.cmed.medicament.list'].browse(self._context.get('active_id'))
        file_name = cmed_medicament_list.file_name
        return file_name
    file_name = fields.Char(
        string='File Name',
        readonly=True,
        default=_default_file_name
    )

    @api.multi
    def _reopen_form(self):
        self.ensure_one()
        action = {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
        return action

    @api.multi
    def do_cmed_medicament_list_file_import(self):
        self.ensure_one()

        start = time()
        row_count = 0
        found = 0
        not_found = 0

        fields = get_fields()

        CMEDMedicament = self.env['clv.cmed.medicament']
        CMEDMedicamentListItem = self.env['clv.cmed.medicament.list.item']

        cmed_medicament_list = self.env['clv.cmed.medicament.list'].browse(self._context.get('active_id'))

        _logger.info(u'%s %s (%s)', '>>>>>', cmed_medicament_list.name, self.file_name)

        filepath = cmed_medicament_list.directory_id.directory + '/' + self.file_name
        _logger.info(u'>>>>>>>>>> %s', filepath)

        book = xlrd.open_workbook(filepath)
        sheet = book.sheet_by_index(0)

        last_row = sheet.nrows - 1

        _logger.info(u'>>>>>>>>>> %s', last_row)

        heading_row = False
        last_col_nr = 0
        col_nr = 0
        for row_nr in range(sheet.nrows):

            if heading_row is False:
                if sheet.cell_value(row_nr, 0) == fields['principio_ativo'][1] and \
                   sheet.cell_value(row_nr, 3) == fields['codigo_ggrem'][1] and \
                   sheet.cell_value(row_nr, 5) == fields['ean'][1] and \
                   sheet.cell_value(row_nr, 8) == fields['classe_terapeutica'][1] and \
                   sheet.cell_value(row_nr, 9) == fields['tipo_status_produto'][1]:
                    heading_row = row_nr

            if heading_row is not False and last_col_nr == 0:

                for col_nr in range(34):

                    cell_value = sheet.cell_value(row_nr, col_nr)
                    for field_str in fields:
                        if cell_value == fields[field_str][1]:
                            fields[field_str][0] = col_nr
                            last_col_nr = col_nr

                    col_nr += 1

                _logger.info(u'>>>>>>>>>> (%s %s)', row_nr, last_col_nr)

                _logger.info(u'>>>>>>>>>> %s', fields)

            elif heading_row is not False and last_col_nr != 0:

                codigo_ggrem = False
                if fields['codigo_ggrem'][0] is not False:
                    codigo_ggrem = sheet.cell_value(row_nr, fields['codigo_ggrem'][0])
                if codigo_ggrem is not False:

                    row_count += 1

                    cmed_medicament = CMEDMedicament.search([
                        ('codigo_ggrem', '=', codigo_ggrem),
                    ])

                    if cmed_medicament.id is False:

                        values = {}

                        values['name'] = sheet.cell_value(row_nr, fields['codigo_ggrem'][0])

                        for field_str in fields:
                            if fields[field_str][0] is not False and fields[field_str][2] is not False:
                                values[field_str] = sheet.cell_value(row_nr, fields[field_str][0])

                        new_cmed_medicament = CMEDMedicament.create(values)
                        not_found += 1
                        _logger.info(u'>>>>>>>>>>>>>>> %s %s', row_nr, new_cmed_medicament.codigo_ggrem)

                    else:

                        found += 1
                        _logger.info(u'>>>>>>>>>>>>>>> %s %s', row_nr, cmed_medicament.codigo_ggrem)

                    values = {}

                    values['list_id'] = cmed_medicament_list.id
                    if cmed_medicament.id is False:
                        values['medicament_id'] = new_cmed_medicament.id
                    else:
                        values['medicament_id'] = cmed_medicament.id
                    values['order'] = row_nr + 1

                    for field_str in fields:
                        cell_value = sheet.cell_value(row_nr, fields[field_str][0])
                        if fields[field_str][0] is not False and fields[field_str][3] is not False and \
                           cell_value != xlrd.empty_cell.value and \
                           cell_value != 'Liberado':
                            values[field_str] = \
                                float(str(cell_value).replace(",", "."))

                    new_cmed_medicament_list_item = CMEDMedicamentListItem.create(values)

                    _logger.info(u'>>>>>>>>>>>>>>>>>>>> %s', new_cmed_medicament_list_item.medicament_id.codigo_ggrem)

        _logger.info('>>>>> fields: %s', fields)
        _logger.info('>>>>> heading_row: %s', heading_row)
        _logger.info('>>>>> last_col_nr: %s', last_col_nr)
        _logger.info('>>>>> row_count: %s', row_count)
        _logger.info('>>>>> found: %s', found)
        _logger.info('>>>>> not_found: %s', not_found)
        _logger.info('>>>>> Execution time: %s', secondsToStr(time() - start))

        return True
