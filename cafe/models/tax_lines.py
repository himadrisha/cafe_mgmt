from odoo import fields, models, api


class TaxInformation(models.Model):
    _name = 'taxlines.taxlines'
    _description = 'tax information'
    _rec_name = 'tax_id'

    tax_id = fields.Many2one('tax.tax', string="Tax")
    b_price = fields.Float(string="Base Price")
    percentage = fields.Float(string="Percentage")
    tax_amount = fields.Float(string="Tax Amount", compute="tax_amount_data")
    sale_id = fields.Many2one('sale.sale', string="Sale Order")




    @api.depends('b_price', 'percentage')
    def tax_amount_data(self):
        for record in self:
            record_tax_amount = (record.b_price * record.percentage)/100
            record.tax_amount = record_tax_amount

