from odoo import api, fields, models


class MypatentEventMailRegistration(models.Model):
    _inherit = 'event.mail.registration'

    def execute(self):
        now = fields.Datetime.now()
        todo = self.filtered(lambda reg_mail:
                             not reg_mail.mail_sent and \
                             reg_mail.registration_id.state in ['open',
                                                                'done'] and \
                             (
                                         reg_mail.scheduled_date and reg_mail.scheduled_date <= now) and \
                             reg_mail.scheduler_id.notification_type == 'mail'
                             )
        for reg_mail in todo:
            organizer = reg_mail.scheduler_id.event_id.organizer_id
            company = self.env.company
            author = self.env.ref('base.user_root')
            if organizer.email:
                author = organizer
            elif company.email:
                author = company.partner_id
            elif self.env.user.email:
                author = self.env.user

            email_values = {
                'author_id': author.id,
            }
            reg_mail.scheduler_id.template_ref.send_mail(
                reg_mail.registration_id.id, email_values=email_values)
        todo.write({'mail_sent': True})
