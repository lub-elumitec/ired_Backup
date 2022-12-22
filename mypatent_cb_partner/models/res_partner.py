from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    salutation_id = fields.Many2one('res.partner.salutation',
                                    string='Salutation', ondelete="restrict")
