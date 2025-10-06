from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Teacher(models.Model):
    _name = 'teacher'
    _description = 'Teacher'

    name = fields.Char(default="Name", required=True)
    email = fields.Char()
    phone = fields.Char()
    course_ids = fields.One2many('course', 'teacher_id')

    _sql_constraints = [
        ('unique_email', 'unique("email")', 'Email already used')
    ]

    @api.constrains('course_ids')
    def _check_course_limit(self):
        for rec in self:
            if len(rec.course_ids) > 2:
                raise ValidationError("A teacher can teach a maximum of 2 courses.")