from odoo import models, fields


class Course(models.Model):
    _name = 'course'
    _description = 'Course'

    name = fields.Char(default="New", required=True)
    description = fields.Text()
    teacher_id = fields.Many2one('teacher', required=True)
    student_ids = fields.Many2many('student')

    _sql_constraints = [
        ('unique_email', 'unique("email")', 'Email already used')
    ]