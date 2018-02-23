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
from dbfpy import dbf
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

    fields['med_abc'] = [False, u'MED_ABC', True, False]
    fields['med_ctr'] = [False, u'MED_CTR', True, False]
    fields['med_lab'] = [False, u'MED_LAB', True, False]
    fields['lab_nom'] = [False, u'LAB_NOM', True, False]
    fields['med_des'] = [False, u'MED_DES', True, False]
    fields['med_apr'] = [False, u'MED_APR', True, False]
    fields['med_barra'] = [False, u'MED_BARRA', True, False]
    fields['med_negpos'] = [False, u'MED_NEGPOS', True, False]
    fields['med_princi'] = [False, u'MED_PRINCI', True, False]

    fields['med_uni'] = [False, u'MED_UNI', True, False]
    fields['med_ipi'] = [False, u'MED_IPI', True, False]
    fields['med_dtvig'] = [False, u'MED_DTVIG', True, False]
    fields['exp_13'] = [False, u'EXP_13', True, False]
    fields['med_regims'] = [False, u'MED_REGIMS', True, False]
    fields['med_varpre'] = [False, u'MED_VARPRE', True, False]

    fields['med_tipmed'] = [False, u'MED_TIPMED', True, False]
    fields['med_ref'] = [False, u'MED_REF', True, False]
    fields['med_ncm'] = [False, u'MED_NCM', True, False]
    fields['med_dcb'] = [False, u'MED_DCB', True, False]
    fields['med_cas'] = [False, u'MED_CAS', True, False]
    fields['med_atc'] = [False, u'MED_ATC', True, False]
    fields['med_clater'] = [False, u'MED_CLATER', True, False]
    fields['med_tarja'] = [False, u'MED_TARJA', True, False]
    fields['med_por344'] = [False, u'MED_POR344', True, False]
    fields['med_tiss'] = [False, u'MED_TISS', True, False]
    fields['med_conf87'] = [False, u'MED_CONF87', True, False]
    fields['med_cap'] = [False, u'MED_CAP', True, False]

    fields['med_pla1'] = [False, u'MED_PLA1', False, True]
    fields['med_pco1'] = [False, u'MED_PCO1', False, True]
    fields['med_fra1'] = [False, u'MED_FRA1', False, True]
    fields['med_pla0'] = [False, u'MED_PLA0', False, True]
    fields['med_pco0'] = [False, u'MED_PCO0', False, True]
    fields['med_fra0'] = [False, u'MED_FRA0', False, True]

    return fields


class ABCFarmaMedicamentListFileImport(models.TransientModel):
    _name = 'clv.abcfarma.medicament.list.file_import'

    def _default_directory_id(self):
        abcfarma_medicament_list = self.env['clv.abcfarma.medicament.list'].browse(self._context.get('active_id'))
        directory_id = abcfarma_medicament_list.directory_id.id
        return directory_id
    directory_id = fields.Many2one(
        comodel_name='clv.file_system.directory',
        string='Directory',
        readonly=True,
        default=_default_directory_id
    )

    def _default_file_name(self):
        abcfarma_medicament_list = self.env['clv.abcfarma.medicament.list'].browse(self._context.get('active_id'))
        file_name = abcfarma_medicament_list.file_name
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
    def do_abcfarma_medicament_list_file_import(self):
        self.ensure_one()

        start = time()
        row_count = 0
        found = 0
        not_found = 0

        fields = get_fields()

        ABCFarmaMedicament = self.env['clv.abcfarma.medicament']
        ABCFarmaMedicamentListItem = self.env['clv.abcfarma.medicament.list.item']

        abcfarma_medicament_list = self.env['clv.abcfarma.medicament.list'].browse(self._context.get('active_id'))

        abcfarma_medicament_list.abcfarma_list_item_ids.unlink()

        _logger.info(u'%s %s (%s)', '>>>>>', abcfarma_medicament_list.name, self.file_name)

        filepath = abcfarma_medicament_list.directory_id.directory + '/' + self.file_name
        _logger.info(u'>>>>>>>>>> %s', filepath)

        db = dbf.Dbf(filepath)

        headers = []
        col_nr = 0
        for field in db.header.fields:
            headers.append(field.name)
            col_nr += 1
            for field_str in fields:
                if field.name == fields[field_str][1]:
                    fields[field_str][0] = col_nr
                    last_col_nr = col_nr
        _logger.info(u'>>>>>>>>>> %s', headers)

        # last_row = sheet.nrows - 1

        # _logger.info(u'>>>>>>>>>> %s', last_row)

        # heading_row = False
        # last_col_nr = 0
        # col_nr = 0
        for rec in db:

            med_abc = False
            if fields['med_abc'][0] is not False:
                med_abc = rec[fields['med_abc'][1]]
            if med_abc is not False:

                row_count += 1

                abcfarma_medicament = ABCFarmaMedicament.search([
                    ('med_abc', '=', med_abc),
                ])

                if abcfarma_medicament.id is False:

                    values = {}

                    values['name'] = rec[fields['med_abc'][1]]

                    for field_str in fields:
                        if fields[field_str][0] is not False and fields[field_str][2] is not False:
                            values[field_str] = rec[fields[field_str][1]]

                    new_abcfarma_medicament = ABCFarmaMedicament.create(values)
                    not_found += 1
                    _logger.info(u'>>>>>>>>>>>>>>> %s %s', row_count, new_abcfarma_medicament.med_abc)

                else:

                    found += 1
                    _logger.info(u'>>>>>>>>>>>>>>> %s %s', row_count, abcfarma_medicament.med_abc)

                values = {}

                values['list_id'] = abcfarma_medicament_list.id
                if abcfarma_medicament.id is False:
                    values['medicament_id'] = new_abcfarma_medicament.id
                else:
                    values['medicament_id'] = abcfarma_medicament.id
                values['order'] = row_count + 1

                for field_str in fields:
                    value = rec[fields[field_str][1]]
                    if fields[field_str][0] is not False and fields[field_str][3] is not False and \
                       value is not None:
                        values[field_str] = \
                            float(str(value).replace(",", "."))

                new_abcfarma_medicament_list_item = ABCFarmaMedicamentListItem.create(values)

                _logger.info(u'>>>>>>>>>>>>>>>>>>>> %s', new_abcfarma_medicament_list_item.medicament_id.med_abc)

        _logger.info('>>>>>>>>>> fields: %s', fields)
        _logger.info('>>>>>>>>>> last_col_nr: %s', last_col_nr)
        _logger.info('>>>>>>>>>> row_count: %s', row_count)
        _logger.info('>>>>>>>>>> found: %s', found)
        _logger.info('>>>>>>>>>> not_found: %s', not_found)
        _logger.info('>>>>>>>>>> Execution time: %s', secondsToStr(time() - start))

        return True
