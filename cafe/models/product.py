from odoo import fields, models, api


class ProductInformation(models.Model):
    _name = 'product.product'
    _description = 'product information'

    name = fields.Char(string='Product Name ')
    code = fields.Integer(string='Product Code')
    image = fields.Binary(string='Image')
    cost_price = fields.Float(string="Cost Price")
    sale_price = fields.Float(string="Sale Price")
    gpm = fields.Float(string="GPM", compute="total_gpm")
    taxes = fields.Many2many('tax.tax', string="Taxes")

    @api.depends('cost_price', 'sale_price')
    def total_gpm(self):
        for record in self:
            total_price = record.cost_price + record.sale_price
            record.gpm = total_price
