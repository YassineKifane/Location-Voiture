# -*- coding: utf-8 -*-
from odoo import api, fields, models

import datetime


class locationvoiture(models.Model):
    _name = "location.voiture"
    _description = "Location des voitures"

    client_name = fields.Many2one('voiture.client', string='Client')
    identite_client = fields.Char(string='Matricule', related="client_name.identite", tracking=True)
    mail_client = fields.Char(string='Email', related="client_name.email", tracking=True)
    mobile_client = fields.Char(string='Mobile', related="client_name.mobile", tracking=True)

    voiture_name = fields.Many2one('voiture.cars', string='Voiture')
    matricule = fields.Char(string='Matricule', related="voiture_name.matricule", tracking=True)
    transmission = fields.Selection(string='Transmission', related="voiture_name.energie", tracking=True)
    energie = fields.Selection(string='Energie', related="voiture_name.transmission", tracking=True)
    prix_parjr = fields.Char(string='Prix Jour/DH', related="voiture_name.prix", tracking=True)

    jours_de_debut = fields.Date(string="Début de la location")
    jours_de_fin = fields.Date(string="Fin de la Location")
    nbrjourlocation = fields.Char(string='Nombre Jour de Location', compute="_compute_nbrjourlocation_")
    prixtotal = fields.Char(string='Prix', compute="_compute_prix_")

    def print_traitement(self):
        return self.env.ref('Location_Voiture.facturation').report_action(self)

    def _compute_nbrjourlocation_(self):
        for a in self:
            if a.jours_de_debut and a.jours_de_fin:
                date_de_debut = fields.Datetime.to_datetime(a.jours_de_debut).date()
                date_de_fin = fields.Datetime.to_datetime(a.jours_de_fin).date()
                t = str(int((date_de_fin - date_de_debut).days))
                a.nbrjourlocation = t + ' Jours'

            else:
                a.nbrjourlocation = " "

    def _compute_prix_(self):
        for a in self:
            if a.jours_de_debut and a.jours_de_fin and a.prix_parjr:
                date_de_debut = fields.Datetime.to_datetime(a.jours_de_debut).date()
                date_de_fin = fields.Datetime.to_datetime(a.jours_de_fin).date()
                t = int((date_de_fin - date_de_debut).days)
                z= str(t* int(a.prix_parjr))
                a.prixtotal = z +' MAD'

            else:
                a.prixtotal = " "


