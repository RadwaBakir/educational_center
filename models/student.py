from odoo import models, fields


class Student(models.Model):
    _name = 'student'
    _description = 'Student'

    name = fields.Char(default="Name", required=True)
    email = fields.Char()
    phone = fields.Char()
    course_ids = fields.Many2many('course')

    _sql_constraints = [
        ('unique_email', 'unique("email")', 'Email already used')
    ]