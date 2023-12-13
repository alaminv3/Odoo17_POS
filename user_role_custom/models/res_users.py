# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2021 (https://www.bistasolutions.com)
#
##############################################################################

from odoo import models, api, fields


class ResUsers(models.Model):
    _inherit = "res.users"

    role_user_id = fields.Many2one('res.users', 'Role')
    role_template = fields.Boolean('Role Template')

    @api.model_create_multi
    def create(self, vals_list):
        users = super(ResUsers, self).create(vals_list)
        if users.role_user_id:
            users.groups_id = [(6, 0,
                                users.role_user_id.sudo().groups_id.ids or [])] or []
        return users

    def write(self, vals):
        if vals.get('role_user_id', False):
            vals.update({'groups_id': [(6, 0, (self.env['res.users'].browse(
                vals.get('role_user_id')).sudo().groups_id.ids))]})
        return super(ResUsers, self).write(vals)

    def update_rights(self):
        for user in self:
            if user.role_user_id:
                role_id = user.role_user_id
                user.role_user_id = role_id
