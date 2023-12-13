# -*- coding: utf-8 -*-
##############################################################################
#
#    Jupical Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Jupical Technologies(<http://www.jupical.com>).
#    Author: Jupical Technologies Pvt. Ltd.(<http://www.jupical.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


import logging
from odoo import fields, models, api, _
from datetime import datetime
from datetime import timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError


_logger = logging.getLogger(__name__)


class CRMLead(models.Model):

    _inherit = "crm.lead"

    # @api.multi
    def write(self, vals):
        mail_activity_obj = self.env['mail.activity']
        ir_crm_model_rec = self.env['ir.model'].search([('model', '=', 'crm.lead')], limit=1)
        if 'stage_id' in vals:
            for lead in self:
                for activity in self.env['mail.activity'].search(
                        [('res_id', '=', lead.id), ('is_mandatory', '=', True)]):
                    if activity.stage_id == lead.stage_id:
                        if self.env.user.lang == 'en_US':
                            raise UserError(_("Please close this %s activity first before moving to next stage" % activity.summary))
                        elif self.env.user.lang == 'nl_NL':
                            raise UserError(_("Rond eerst deze taak %s voordat je verder gaat " % activity.summary))


            for lead in self:
                for activity_scheduled in self.env['schedule.auto.activity'].search(
                        [('stage_id', '=', vals.get('stage_id'))]):
                    if activity_scheduled:
                        if isinstance(lead.write_date, str):
                            date = datetime.strptime(lead.write_date, DEFAULT_SERVER_DATETIME_FORMAT)
                            date = date + timedelta(days=activity_scheduled.due_day)
                            date = lead.get_next_date_schedule_activit(date)
                        else:
                            date = lead.write_date + timedelta(days=activity_scheduled.due_day)
                            date = lead.get_next_date_schedule_activit(date)

                        mail_activity_info = {'activity_type_id': activity_scheduled.activity_type_id and activity_scheduled.activity_type_id.id or False,
                                              'user_id': self._uid,
                                              'summary': activity_scheduled.name or "",
                                              'is_mandatory': activity_scheduled.is_mandatory or "",
                                              'date_deadline': date,
                                              'note': activity_scheduled.description or "",
                                              'res_id': lead and lead.id or False,
                                              'res_model_id': ir_crm_model_rec and ir_crm_model_rec.id or False,
                                              'stage_id': activity_scheduled.stage_id and activity_scheduled.stage_id.id
                                              or False
                                              }
                        mail_activity_obj.create(mail_activity_info)

        res = super(CRMLead, self).write(vals)

        return res

    def get_next_date_schedule_activit(self, date):
        print("date====", date.weekday())
        if date.weekday() == 6:
            date = date + timedelta(days=1)
        elif date.weekday() == 5:
            date = date + timedelta(days=2)
        return date

    @api.model
    def create(self, vals):

        # Stage = Terugbelverzoeken if lead from Incoming mail Server
        context_value = self.env.context

        _logger.info("Context: {}".format(context_value))
        _logger.info("Values: {}".format(vals))
        
        if 'fetchmail_cron_running' in context_value and 'params' in context_value:
            # is_from_email = context_value.get('fetchmail_cron_running')
            fetchmail_server_id = context_value.get('fetchmail_server_id')
            if fetchmail_server_id:
                mail_server = self.env['fetchmail.server'].search([('id','=',fetchmail_server_id)])
                if mail_server:                   
                    if mail_server.user == 'terugbel@de-zorgcoach.nl':
                        stage_obj = self.env['crm.stage']
                        stage_id = stage_obj.search([('name','=','Terugbelverzoeken')])
                        if not stage_id:
                            stage_id = stage_obj.create({'name':'Terugbelverzoeken'})

                        _logger.info("Stage ID: {}".format(stage_id.id))
                        stage_dict ={'stage_id':stage_id.id}
                        vals.update(stage_dict)        
                        _logger.info("Stage ID: {}".format(stage_id.name)) 

        result = super(CRMLead, self).create(vals)
        if result.campaign_id and result.campaign_id.name == 'ehealth':
            ehealth_stage = self.env['crm.stage'].search([('name', '=', 'eHealth')], limit=1)
            if ehealth_stage:
                result.stage_id = ehealth_stage.id
        if result and result.stage_id.name != "eHealth":
            mail_activity_obj = self.env['mail.activity']
            ir_crm_model_rec = self.env['ir.model'].search([('model', '=', 'crm.lead')], limit=1)
            for  activity_scheduled in self.env['schedule.auto.activity'].search([('stage_id', '=', result.stage_id.id)]):
                if activity_scheduled:
                    if isinstance(result.create_date, str):
                        date = datetime.strptime(result.create_date, DEFAULT_SERVER_DATETIME_FORMAT)
                        date = date + timedelta(days=activity_scheduled.due_day)
                        date = result.get_next_date_schedule_activit(date)
                    else:
                        date = result.create_date + timedelta(days=activity_scheduled.due_day)
                        date = result.get_next_date_schedule_activit(date)

                    mail_activity_info = {'activity_type_id': activity_scheduled.activity_type_id and
                                          activity_scheduled.activity_type_id.id or False,
                                          'user_id': self._uid,
                                          'summary': activity_scheduled.name or "",
                                          'is_mandatory': activity_scheduled.is_mandatory or "",
                                          'date_deadline': date,
                                          'note': activity_scheduled.description or "",
                                          'res_id': result and result.id or False,
                                          'res_model_id': ir_crm_model_rec and ir_crm_model_rec.id or False,
                                          'stage_id': activity_scheduled.stage_id and activity_scheduled.stage_id.id
                                          or False
                                          }
                    mail_activity_obj.create(mail_activity_info)

        


        return result