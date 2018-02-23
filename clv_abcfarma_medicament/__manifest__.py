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

{
    'name': 'ABCFarma Medicament',
    'summary': 'ABCFarma Medicament Module used by CLVsol Solutions.',
    'version': '3.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_medicament',
    ],
    'data': [
        'security/abcfarma_medicament_security.xml',
        'security/ir.model.access.csv',
        'views/abcfarma_medicament_view.xml',
        'views/abcfarma_medicament_list_view.xml',
        'views/abcfarma_medicament_list_item_view.xml',
        'views/file_system_view.xml',
        'wizard/abcfarma_medicament_list_file_upload_view.xml',
        'wizard/abcfarma_medicament_list_file_import_view.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
