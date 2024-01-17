from odoo import fields, models, api


class SaleInformation(models.Model):
    _name = 'sale.sale'
    _description = 'sale information'
    _rec_name = 'customer'

    customer = fields.Many2one('res.partner', string="Customer")
    date = fields.Date(string="Date")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('canceled', 'Canceled')], default="draft", string="State")
    order_ids = fields.One2many('orderlines.orderlines', 'sale_id', string="Order Lines", ondelete='cascade')
    tax_ids = fields.One2many('taxlines.taxlines', 'sale_id', string="Tax Lines")
    untaxed = fields.Float(string="Untaxed Amount", related="order_ids.sub_total")
    tax = fields.Float(string="Tax Amount", compute="tax_total")
    total = fields.Float(string="Total Amount", compute="total_amount_count")
    himadri = fields.Char(string="Himadri", index=True)


    def confirm_data(self):
        for sale in self:
            sale.state = 'confirmed'

    def draft_data(self):
        for sale in self:
            sale.state = 'draft'

    def done_data(self):
        for sale in self:
            sale.state = 'done'

        return {
            'effect': {
                'fadeout': 'slow',
                'type': 'rainbow_man',
            }
        }
        return True

    def cancel_data(self):
        for sale in self:
            sale.state = 'draft'


    def delete_data(self):
        order_line = self.mapped('order_ids')
        order_line.unlink()
        return super(SaleInformation, self).unlink()

    @api.depends('tax_ids.tax_amount')
    def tax_total(self):
        for record in self:
            tax_amount = record.tax_ids.mapped('tax_amount')
            total_tax = sum(tax_amount)
            record.tax = total_tax



    @api.depends('untaxed', 'tax')
    def total_amount_count(self):
        for rec in self:
            total_tax_amount = rec.untaxed + rec.tax
            rec.total = total_tax_amount


    # @api.constrains('state')
    # def confirmed_state(self):
    #     for record in self:
    #         if record.state == 'confirmed':
    #             raise  ValidationError('you can not Edit Your Sale Order because you confirmed the Sale...')
    #         else:
    #             pass
    # @api.constrains('state')
    # def check_state(self):
    #     for record in self:
    #         if record.state != 'draft':
    #             raise ValidationError('You are not in Draft State, so you can not Edit the form.....')
    #
    #     return record
