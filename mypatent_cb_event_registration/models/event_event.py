from odoo import fields, models


class EventEvent(models.Model):
    _inherit = 'event.event'

    hide_online_registration = fields.Boolean(string='Hide online registration',
                                              default=False)

    def get_selection_values_for_registration(self):
        """ Selection values for the registration form"""
        titles = self.env['res.partner.title'].search([], order='name')
        countries = self.env['res.country'].search([], order='name')
        salutations = self.env['res.partner.salutation'].search([], order='name')
        genders = self.env['res.partner.gender'].search([], order='name')

        return {
            'titles': titles,
            'countries': countries,
            'salutations': salutations,
            'genders': genders,
        }