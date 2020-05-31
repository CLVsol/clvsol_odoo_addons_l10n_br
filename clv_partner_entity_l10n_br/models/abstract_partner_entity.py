# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo import models


class AbstractPartnerEntity(models.AbstractModel):
    _inherit = 'clv.abstract.partner_entity'

    # @api.multi
    def zip_search(self):
        self.ensure_one()
        return self.env['l10n_br.zip'].zip_search(self)

    # @api.multi
    # def do_set_contact_info_as_unavailable(self):

    #     for record in self:

    #         data_values = {}

    #         data_values['contact_info_is_unavailable'] = True

    #         data_values['street'] = False
    #         data_values['street_number'] = False
    #         data_values['street2'] = False
    #         data_values['district'] = False
    #         data_values['zip'] = False
    #         data_values['city'] = False
    #         data_values['city_id'] = False
    #         data_values['state_id'] = False
    #         data_values['country_id'] = False
    #         # data_values['phone'] = False
    #         # data_values['mobile'] = False

    #         record.write(data_values)

    #     return True
