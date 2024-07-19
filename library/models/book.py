from odoo import models, fields

class Book(models.Model):
    _name = 'library.book'
    _rec_name = 'title'
    
    title = fields.Char(required=True, string="Título")
    author = fields.Char(required=True, string="Autor")
    genre = fields.Char(required=True, string="Género")
    pages = fields.Integer(string="Cant. Páginas")
    date_started = fields.Date(string="Fecha Inicio")
    date_finished = fields.Date(string="Fecha Finalización")
