# -*- coding: utf-8 -*-
from odoo import api, fields, models

import datetime


class voitureClient(models.Model):
    _name = "voiture.client"
    _description = "Client Page"
    _inherits = {'res.partner': 'partnerkey'}
    age = fields.Char(string="Age", compute="_compute_age_")
    identite = fields.Char(string="Matricule")
    date_de_naissance = fields.Date(string="Date de Naissance")
    genre = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    ], required=False)

    Type = fields.Selection([('client','Client'),
                               ('assurance','Assurance'), ('societe','Societe'),
                               ], required=False, default='client')

    region = fields.Selection([('Tanger-Tétouan-Al Hoceïma', 'Tanger-Tétouan-Al Hoceïma'), ('Oriental', 'Oriental'),
                               ('Fès-Meknès', 'Fès-Meknès'),
                               ('Rabat-Salé-Kénitra', 'Rabat-Salé-Kénitra'),
                               ('Béni Mellal-Khénifra', 'Béni Mellal-Khénifra'),
                               ('Casablanca-Settat', 'Casablanca-Settat'),
                               ('Marrakech-Safi', 'Marrakech-Safi'),
                               ('Drâa-Tafilalet', 'Drâa-Tafilalet'),
                               ('Souss-Massa', 'Souss-Massa'),
                               ('Guelmim-Oued Noun', 'Guelmim-Oued Noun'),
                               ('Laâyoune-Sakia El Hamra', 'Laâyoune-Sakia El Hamra'),
                               ('Dakhla-Oued Ed Dahab', 'Dakhla-Oued Ed Dahab'),
                               ], required=False, default='')

    def _compute_age_(self):
        today_date = datetime.date.today()
        for a in self:
            if a.date_de_naissance:
                date_de_naissance = fields.Datetime.to_datetime(a.date_de_naissance).date()
                t = str(int((today_date - date_de_naissance).days / 365))
                a.age = t + ' ans'

            else:
                a.age = " "
