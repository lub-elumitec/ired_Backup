from odoo import fields, models


class ResPartnerGender(models.Model):
    _name = 'res.partner.gender'
    _order = 'name'
    _description = "Partner Gender"

    name = fields.Char('Name', required=True, translate=True)
