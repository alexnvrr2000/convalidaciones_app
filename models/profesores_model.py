# -*- coding: utf-8 -*-
from odoo import models, fields, api
from random import choice
from odoo.exceptions import ValidationError


class profesor_model(models.Model):
    _name='convalidaciones_app.profesor_model'
    _description = 'Modelo de Profesores'


    name =fields.Char(string="Nombre",required=True,index=True,help="Nombre")
    apellidos =fields.Char(string="Apellidos",required=True,index=True,help="Apellidos")
    foto=fields.Binary()
    dni=fields.Char(string="DNI",required=True,size=9,help="DNI")
    alumnos = fields.Many2many("convalidaciones_app.alumno_model",string="Alumnos")
    numAlumnos=fields.Integer(string="Numero Alumnos:",compute="_calcAlumnos")

    @api.depends("alumnos")
    def _calcAlumnos(self):
        self.alumnos=len(self.alumnos)
    
    @api.constrains("dni")
    def _validaDNI(self):
        letras="TRWAGMYFPDXBNJZSQVHLCKE"
        letra=self.dni[-1]
        num=int(self.dni[:-1])
        if letras[num%23]!=letra:
            raise ValidationError("DNI no valido")
