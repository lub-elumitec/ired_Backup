{
    'name': 'My Patent CB Font Tstar Website',
    'version': '15.0.1.0.0',
    'summary': 'added tstar fonts to the front end',
    'author': 'Cybrosys Techno solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'website',
    ],
    'data': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'assets': {
        'web.assets_frontend': [
            'mypatent_cb_font_tstar/static/src/scss/font_tstar.scss'
        ],
        'web._assets_primary_variables': [
            ("prepend", "mypatent_cb_font_tstar/static/src/scss/primary_variables.scss"),
        ],
    },
}
