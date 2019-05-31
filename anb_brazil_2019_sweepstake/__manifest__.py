# -*- coding: utf-8 -*-
##############################################################################
#
#    Mandate module for openERP
#    Copyright (C) 2018-TODAY Anubía, soluciones en la nube,SL
#                             (http://www.anubia.es)
#    @author: Juan Formoso Vasco <jfv@anubia.es>,
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

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
    'version': '10.0.0.1',
    'author': 'Anubía Soluciones en la Nube, SL, Juan Formoso Vasco',
    'maintainer': 'Anubía Soluciones en la Nube, SL, Juan Formoso Vasco',
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
