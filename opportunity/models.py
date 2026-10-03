from django.db import models


class Opportunity(models.Model):

    TYPE_CHOICES = [
        ('Internship', 'Internship'),
        ('Job', 'Job'),
        ('Graduate', 'Graduate'),
        ('Multiple', 'Multiple'),
    ]

    company_name = models.CharField(
        max_length=150
    )

    opportunity_type = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES
    )

    description = models.TextField()

    relevant_skills = models.CharField(
        max_length=500,
        blank=True,
        help_text="Example: Python, Django, SQL, Git"
    )

    relevant_careers = models.CharField(
        max_length=500,
        blank=True,
        help_text="Example: Python Developer, Full Stack Developer"
    )

    locations = models.CharField(
        max_length=300,
        blank=True,
        help_text="Example: Chennai, Bengaluru, Hyderabad, Remote"
    )

    official_url = models.URLField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Opportunity"
        verbose_name_plural = "Opportunities"

    def __str__(self):
        return self.company_name