from odoo import fields, models


class ResPartnerSalutation(models.Model):
    _name = 'res.partner.salutation'
    _order = 'name'
    _description = "Partner Salutation"

    name = fields.Char('Name', required=True, translate=True)
