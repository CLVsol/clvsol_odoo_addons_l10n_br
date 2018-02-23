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
import base64

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ABCFarmaMedicamentListFileUpload(models.TransientModel):
    _name = 'clv.abcfarma.medicament.list.file_upload'

    def _default_directory_id(self):
        abcfarma_medicament_list = self.env['clv.abcfarma.medicament.list'].browse(self._context.get('active_id'))
        directory_id = abcfarma_medicament_list.directory_id.id
        return directory_id
    directory_id = fields.Many2one(
        comodel_name='clv.file_system.directory',
        string='Directory',
        readonly=False,
        default=_default_directory_id
    )

    upload_file = fields.Binary(string='Upload File')
    file_name = fields.Char(string='File Name')

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
    def do_abcfarma_medicament_list_file_upload(self):
        self.ensure_one()

        abcfarma_medicament_list = self.env['clv.abcfarma.medicament.list'].browse(self._context.get('active_id'))
        file_system_directory = self.directory_id

        _logger.info(u'%s %s', '>>>>>', file_system_directory.name)

        directory = file_system_directory.get_dir() or ''
        full_path = directory + self.file_name

        _logger.info(u'%s %s', '>>>>>>>>>>', full_path)

        f = open(full_path, 'w')
        f.write(base64.decodestring(self.upload_file))
        f.close()

        abcfarma_medicament_list.directory_id = file_system_directory.id
        abcfarma_medicament_list.stored_file_name = self.file_name
        abcfarma_medicament_list.file_name = self.file_name

        return True
