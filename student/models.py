from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    college = models.CharField(max_length=150, blank=True)
    course = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=20, blank=True)

    profile_image = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Programming', 'Programming'),
        ('Web Development', 'Web Development'),
        ('Database', 'Database'),
        ('Data Science', 'Data Science'),
        ('Machine Learning', 'Machine Learning'),
        ('Cloud', 'Cloud'),
        ('DevOps', 'DevOps'),
        ('Cybersecurity', 'Cybersecurity'),
        ('Soft Skill', 'Soft Skill'),
        ('Other', 'Other'),
    ]

    skill_name = models.CharField(
        max_length=100,
        unique=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    def __str__(self):
        return self.skill_name


class StudentSkill(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='student_skills'
    )

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE
    )

    proficiency = models.IntegerField(
        default=1,
        choices=[
            (1, 'Beginner'),
            (2, 'Intermediate'),
            (3, 'Advanced'),
            (4, 'Expert'),
        ]
    )

    def __str__(self):
        return f"{self.student.full_name} - {self.skill.skill_name}"


class Project(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    title = models.CharField(max_length=150)

    description = models.TextField()

    technologies = models.CharField(
        max_length=300,
        help_text="Example: Python, Django, SQLite"
    )

    github_link = models.URLField(
        blank=True,
        null=True
    )

    project_image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Certificate(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='certificates'
    )

    certificate_name = models.CharField(
        max_length=150
    )

    issuing_organization = models.CharField(
        max_length=150
    )

    issue_date = models.DateField(
        blank=True,
        null=True
    )

    certificate_file = models.FileField(
        upload_to='certificates/',
        blank=True,
        null=True
    )

    certificate_link = models.URLField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.certificate_name