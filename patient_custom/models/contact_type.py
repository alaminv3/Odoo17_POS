# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2022 (https://www.bistasolutions.com)
#
##############################################################################

from odoo import fields, models, _

class ContactType(models.Model):
    _name = 'contact.type'
    _description = 'Adds Contacts Types for Contacts'

    name = fields.Char("Contact Type")