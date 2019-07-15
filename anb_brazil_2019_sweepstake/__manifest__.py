# -*- coding: utf-8 -*-
# Copyright 2019-TODAY Juan Formoso Vasco <jfv@anubia.es>
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Brazil American Cup 2019 Sweepstake',
    'summary': 'The American Cup 2019 sweepstake game for Odoo users',
    'description': """Description in HTML file.
- Sweepstake American Sweepstake
- Sweepstake Brazil Sweepstake
- Sweepstake Cup Sweepstake
- Game
- Gamification
- Anubia Soluciones en la Nube, S.L.
""",
    'category': 'Extra Tools',
    'version': '11.0.0.1',
    'author': 'Anubía Soluciones en la Nube, S.L.',
    'maintainer': 'Anubía Soluciones en la Nube, S.L.',
    'contributors': [
        'Juan Formoso Vasco <jfv@anubia.es>',
    ],
    'website': 'http://www.anubia.es',
    'depends': [
        'base',
    ],
    'data': [
        'data/teams_data.xml',
        'data/matches_data.xml',
        'security/security_data.xml',
        'security/ir.model.access.csv',
        'views/sweepstake_admin_view.xml',
        'views/sweepstake_view.xml',
        'views/anb_brazil_2019_sweepstake.xml',
    ],
    'demo': [],
    'test': [],
    'images': [
        'static/description/main_screenshot.png',
        'static/description/main_1.png',
        'static/description/main_2.png',
        'static/description/main_3.png',
        'static/description/main_4.png',
        'static/description/main_5.png',
        'static/description/anubia-logo.png',
        'static/description/bac-logo.png',
        'static/description/flags/spain-flag.png',
        'static/description/flags/uk-flag.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': 'EUR',
}
