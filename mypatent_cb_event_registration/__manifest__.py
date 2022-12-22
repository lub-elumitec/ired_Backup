{
    'name': 'My Patent CB Event Registration',
    'version': '15.0.1.0.0',
    'summary': 'customizations on event registration for my patent',
    'author': 'Cybrosys Techno solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'event',
        'mypatent_cb_partner',
        'website_event',
    ],
    'data': [
        'data/event_mail_template_data.xml',
        'views/event_registration_views.xml',
        'views/event_templates.xml',
        'views/event_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'mypatent_cb_event_registration/static/src/css/event_registration.css',
            'mypatent_cb_event_registration/static/src/js/website_event_tickets.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
