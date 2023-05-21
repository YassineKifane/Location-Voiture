# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Location Voiture',
    'version': '1.0.0',
    'category': 'Location Voiture/location',
    'summary': 'Gestion de Location des Voitures',
    'description': """Gestion de Location des Voitures""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/locationpage.xml',
        'views/Voiture.xml',
        'views/client.xml',
        'views/clientpage.xml',
        'views/assurancepage.xml',
        'views/entreprisepage.xml',
        'report/facturation.xml',
        'report/report.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
