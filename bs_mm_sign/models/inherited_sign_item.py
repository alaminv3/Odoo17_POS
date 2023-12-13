# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError, AccessError
from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT

# This is the list of supported field types and their corresponding classes. Many2many will be added later if needed.
PRIMARY_FIELD_TYPE = {
    'boolean': bool,
    'float': float,
    'integer': int,
    'monetary': float,
}
STR_FIELD_TYPE = {
    'char': str,
    'date': str,
    'datetime': str,
    'many2one': str,
    'text': str,
    'selection': str
}

def check_date_value(value):
    # Attempt to create a datetime object from the input value.
    try:
        date_obj = datetime.strptime(value, DEFAULT_SERVER_DATE_FORMAT)
        return True
    except ValueError:
        return False


class InheritedSignRequest(models.Model):
    _inherit = 'sign.request'

    def write(self, vals):
        if 'state' in vals and vals.get('state', False) == 'signed':
            sign_request_items = self.request_item_ids.filtered(lambda item: item.state == 'completed')
            for sign_request_item in sign_request_items:
                data_model = {}
                related_partner = sign_request_item.partner_id
                item_values = sign_request_item.sign_item_value_ids
                for item_value in item_values.filtered(lambda item: item.model_id and item.field_id):
                    model_name = item_value.model_id.model
                    field_name = item_value.field_id.name
                    field_type = item_value.field_id.ttype
                    field_action = item_value.field_action
                    value = item_value.value
                    model_obj = None

                    # Set a flag got_error. And at last check for it. If it's true, then set value blank instead of throwing an error
                    got_error = False

                    # CHeck if we can handle this kind of fields or not
                    if field_type not in PRIMARY_FIELD_TYPE.keys() and field_type not in STR_FIELD_TYPE.keys():
                        # raise ValidationError(f'{field_type} type field is not supported in signed document.')
                        got_error = True

                    # IF Field type is from primary fields, then only check if value type is same or not
                    if field_type in PRIMARY_FIELD_TYPE.keys() and not isinstance(value, PRIMARY_FIELD_TYPE[field_type]):
                        # raise ValidationError(f'Field {field_name} should receive {field_type} type data.')
                        got_error = True

                    # If field_type is from str fields, then check separately. Try to convert first to it's actual type.
                    if field_type in STR_FIELD_TYPE and isinstance(value, str):
                        # Check if the field is relational and corresponding value exist or not
                        if field_type == 'many2one':
                            model_of_field = item_value.field_id.relation
                            domain = [('name', '=', value)] if field_action == 'exact_match' else [('name', 'ilike', value)]
                            model_obj = self.env[model_of_field].search(domain, limit=1)
                            if not model_obj:
                                # raise ValidationError(f'Field {field_name} has no value like {value}.')
                                got_error = True

                        # If a field is date/datetime, then try to convert it to a date/datetime, if it fails, then value is not correct.
                        elif field_type in ['date', 'datetime'] and not check_date_value(value):
                            # raise ValidationError(f'Date/Datetime value is not correct of field {field_name}.')
                            got_error = True
                        else:
                            pass

                    # Check if any error occurs so far. It any, then set the value blank and continue
                    if got_error:
                        item_value.value = None
                        continue

                    if model_name in data_model.keys():
                        data_model[model_name][field_name] = model_obj.id if field_type == 'many2one' and model_obj else value
                    else:
                        data_model[model_name] = {
                            field_name: model_obj.id if field_type == 'many2one' and model_obj else value
                        }
                # print(data_model)
                try:
                    if data_model:
                        if related_partner and 'res.partner' in data_model.keys():
                            related_partner.sudo().write(data_model['res.partner'])
                        for model in data_model.keys():
                            # TODO: Here we need add some validations like if all required fields value are available or not
                            if model != 'res.partner':
                                new_model_obj = self.env[model].sudo().create(data_model[model])

                # These Exceptions should be removed in order to give a smooth experience to the end user. But For now it's for checking purpose
                except AccessError:
                    raise ValidationError('This user is not allowed to modify the specified records/fields.')
                except ValidationError:
                    raise ValidationError('There are some invalid values for one or more fields.')
                except ValueError:
                    raise ValidationError('There must be a field name specified in the create values that does not exist.')
                except UserError:
                    raise ValidationError('A loop is created in a hierarchy of objects such as setting an object as its own parent.')

        return super(InheritedSignRequest, self).write(vals)


class InheritedSignItem(models.Model):
    _inherit = 'sign.item'

    model_id = fields.Many2one('ir.model')
    field_id = fields.Many2one('ir.model.fields', domain="[('model_id', '=', model_id)]")
    field_action = fields.Selection([
        ('exact_match', 'Exact Match'),
        ('partial_match', 'Partial Match'),
    ], default='exact_match')


class InheritedSignRequestItemValue(models.Model):
    _inherit = 'sign.request.item.value'

    model_id = fields.Many2one('ir.model', related='sign_item_id.model_id', store=True)
    field_id = fields.Many2one('ir.model.fields', related='sign_item_id.field_id', store=True)
    field_action = fields.Selection([
        ('exact_match', 'Exact Match'),
        ('partial_match', 'Partial Match'),
    ], related='sign_item_id.field_action')
