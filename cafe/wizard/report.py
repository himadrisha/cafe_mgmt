from  odoo import fields, models, api


class ReportValue(models.TransientModel):
   _name = "report.wizard"
   _description = "report value wizard"


   start_date = fields.Date(string="Start Date")
   end_date = fields.Date(string="End Date")

   def select_record(self):
      return {
         'type': 'ir.actions.act_window',
         'context': "{'create' : False}",
         'name': 'Sale',
         'view_mode': 'tree',
         'res_model': 'sale.sale',
         'domain': [('date', '>=', self.start_date), ('date', '<=', self.end_date)]

      }
