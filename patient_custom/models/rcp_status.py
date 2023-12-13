# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2022 (https://www.bistasolutions.com)
#
##############################################################################

from odoo import fields, models, _

class RCPStatus(models.Model):
    _name = 'rcp.status'
    _description = 'Adds RCP Status for Contacts'

    name = fields.Char("Status")