from odoo import http, _
from odoo.addons.website_event.controllers.main import WebsiteEventController


class WebsiteEventController(WebsiteEventController):
    @http.route()
    def registration_confirm(self, event, **post):
        if 'same_tickets' in post:
            del post['same_tickets']
        if 'terms' in post:
            del post['terms']
        res = super(WebsiteEventController, self).registration_confirm(event,
                                                                       **post)
        return res
