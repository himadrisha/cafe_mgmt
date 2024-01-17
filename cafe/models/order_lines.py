from odoo import fields, models, api


class OrderInformation(models.Model):
    _name = 'orderlines.orderlines'
    _description = 'order information'
    _rec_name = 'product_id'

    product_id = fields.Many2one('product.product', string="Product")
    quyt = fields.Float(string="Quantity")
    price = fields.Float(string="Price")
    tax_amount = fields.Float(string="Tax Amount", compute="order_tax")
    taxes = fields.Many2many('taxlines.taxlines', string="Taxes")
    sub_total = fields.Float(string="Sub Total", compute="sub_total_data")
    total = fields.Float(string="Total", compute="total_order_data")
    sale_id = fields.Many2one('sale.sale', string="Sale Order", ondelete='cascade')
    tax_id = fields.Many2one('taxlines.taxlines', string="Tax")
    # • Product(M2O),
    # • Quantity(Float),
    # • Price(Float),
    # • Sub Total(Float, Quantity * Price)
    # • Taxes (M2M)
    # • Tax Amount (Float, Calculated from selected taxes)
    # • Total (Float Sub Total + Tax Amount)

    @api.depends('quyt', 'price')
    def sub_total_data(self):
        for record in self:
            sub_total = record.quyt * record.price
            record.sub_total = sub_total

    @api.depends('taxes')
    def order_tax(self):
        for record in self:
            tex_order_amount = record.taxes.mapped('tax_amount')
            record.tax_amount = sum(tex_order_amount)


    @api.depends('tax_amount', 'sub_total')
    def total_order_data(self):
        for rec in self:
            rec.total = rec.tax_amount + rec.sub_total
