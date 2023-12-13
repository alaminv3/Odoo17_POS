# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2022 (https://www.bistasolutions.com)
#
##############################################################################

from odoo import fields, models, _, api

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    rcp_owner_id = fields.Many2one("res.partner", string="Billing Physician", compute="compute_rcp_owner_id", readonly=True,
                                   store=True)

    @api.depends('picking_id', 'picking_id.rcp_owner_id')
    def compute_rcp_owner_id(self):
        """
        Due to huge data of partner on live database convert this fields to compute field instead of related field
        """
        for line in self:
            line.update({'rcp_owner_id': line.picking_id.rcp_owner_id and line.picking_id.rcp_owner_id.id or False})
