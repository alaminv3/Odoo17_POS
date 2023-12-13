# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2022 (https://www.bistasolutions.com)
#
##############################################################################

from odoo import fields, models, _

class RCPPrograms(models.Model):
    _name = 'rcp.program'
    _description = 'Adds RCP Programs for Contacts'

    name = fields.Char("Program")