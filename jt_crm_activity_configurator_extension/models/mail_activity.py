# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2022 (https://www.bistasolutions.com)
#
##############################################################################

from odoo import api, exceptions, fields, models, _, Command

class MailActivity(models.Model):

    _inherit = 'mail.activity'

    @api.model
    def create(self, vals):

        res = super(MailActivity, self).create(vals)
        ctx = dict(self.env.context)

        # Checking if activity is being created from crm.lead model or not
        # if ctx.get('params', False) and ctx.get('params', False)['model'] == 'crm.lead':
        if ctx.get('default_type', False) == 'opportunity':
            crm_lead_obj = self.env['crm.lead'].search(
                        [('id', '=', vals['res_id'])])
            schedule_auto_activity_obj = self.env['schedule.auto.activity'].search(
                        [('stage_id', '=', vals['stage_id'])], limit=1)

            # If Scheduled Activity is set to assign automatically, then assigning sales person to the scheduled activity
            if schedule_auto_activity_obj.assign_automatically:
                res.update({'user_id': crm_lead_obj.user_id and crm_lead_obj.user_id.id or False})

        return res