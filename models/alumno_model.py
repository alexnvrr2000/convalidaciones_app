# -*- coding: utf-8 -*-
from odoo import models, fields, api
from random import choice
from odoo.exceptions import ValidationError


class alumno_model(models.Model):
    _name = 'convalidaciones_app.alumno_model'
    _description = 'convalidaciones_app.alumno_model'

    name = fields.Char(string="Nombre",required=True,index=True,help="Nombre del alumno")
    password = fields.Char(string="Contraseña",required=False,size=10,help="Password del alumno")
    foto = fields.Binary()
    edad = fields.Integer(string="Edad",required=True,help="Edad del alumno")
    localidad = fields.Char(string="Localidad",size=100,required=True,help="Localidad del alumno")
    provincia = fields.Char(string="Provincia",size=100,required=True,help="Provincia del alumno")
    email = fields.Char(string="Email",size=100,required=False,help="Email del alumno")
    convalidaciones = fields.One2many("convalidaciones_app.conva_model","alumno_id",string="Convalidaciones")

    def generarPassword(self):
        self.ensure_one()
        longitud = 10
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        p = ""
        p = p.join([choice(valores) for i in range(longitud)])
        self.password = p
        return True
    
    @api.constrains("edad")
    def _check_edad(self):
        if len(self.edad) < 14:
            raise ValidationError("El alumno debe tener al menos 14 años")
        return True
