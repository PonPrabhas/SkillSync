from django.db import models
from student.models import Skill


class Career(models.Model):
    career_name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField()

    def __str__(self):
        return self.career_name


class CareerSkill(models.Model):
    career = models.ForeignKey(
        Career,
        on_delete=models.CASCADE,
        related_name='required_skills'
    )

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='career_requirements'
    )

    importance = models.IntegerField(
        default=1,
        choices=[
            (1, 'Basic'),
            (2, 'Important'),
            (3, 'Essential'),
        ]
    )

    def __str__(self):
        return f"{self.career.career_name} - {self.skill.skill_name}"