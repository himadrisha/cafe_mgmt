from odoo import fields, models, api


class TaxInformation(models.Model):
    _name = 'tax.tax'
    _description = 'tax information'

    name = fields.Char(string="Tax Name")
    code = fields.Char(string="Tax Code")
