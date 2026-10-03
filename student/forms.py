from django import forms
from .models import (
    Student,
    StudentSkill,
    Skill,
    Project,
    Certificate
)
class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'full_name',
            'email',
            'phone',
            'college',
            'course',
            'year',
            'profile_image'
        ]

        widgets = {
            'full_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),

            'phone': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'college': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'course': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'year': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'profile_image': forms.FileInput(
                attrs={'class': 'form-control'}
            ),
        }



class StudentSkillForm(forms.ModelForm):

    class Meta:
        model = StudentSkill

        fields = [
            'skill',
            'proficiency'
        ]

        widgets = {
            'skill': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'proficiency': forms.Select(
                attrs={'class': 'form-select'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['skill'].queryset = Skill.objects.all()

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            'title',
            'description',
            'technologies',
            'github_link',
            'project_image'
        ]

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),

            'technologies': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Example: Python, Django, SQLite'
                }
            ),

            'github_link': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'https://github.com/...'
                }
            ),

            'project_image': forms.FileInput(
                attrs={'class': 'form-control'}
            ),
        }
class CertificateForm(forms.ModelForm):

    class Meta:
        model = Certificate

        fields = [
            'certificate_name',
            'issuing_organization',
            'issue_date',
            'certificate_file',
            'certificate_link'
        ]

        widgets = {
            'certificate_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'issuing_organization': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'issue_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'certificate_file': forms.FileInput(
                attrs={'class': 'form-control'}
            ),

            'certificate_link': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'https://...'
                }
            ),
        }