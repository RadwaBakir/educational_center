from odoo import models, fields, api


class Course(models.Model):
    _name = 'course'
    _description = 'Course'

    name = fields.Char(default="New", required=True)
    description = fields.Text()
    teacher_id = fields.Many2one('teacher', required=True)
    student_ids = fields.Many2many('student')
    student_count = fields.Integer(compute="_compute_student_count")


    @api.depends('student_ids')
    def _compute_student_count(self):
        for rec in self:
            rec.student_count = len(rec.student_ids)
