from django.contrib import admin

from .models import (
    Student,
    Skill,
    StudentSkill,
    Project,
    Certificate
)

admin.site.register(Student)
admin.site.register(Skill)
admin.site.register(StudentSkill)
admin.site.register(Project)
admin.site.register(Certificate)