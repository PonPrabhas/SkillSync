from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from student.models import Student
from .models import Career


@login_required
def career_explorer(request):

    student = Student.objects.get(
        user=request.user
    )

    careers = Career.objects.prefetch_related(
        'required_skills__skill'
    ).all()

    student_skill_names = set(
        student.student_skills.values_list(
            'skill__skill_name',
            flat=True
        )
    )

    career_data = []

    for career in careers:

        required_skills = []

        for career_skill in career.required_skills.all():

            skill_name = career_skill.skill.skill_name

            required_skills.append({
                'name': skill_name,
                'importance': career_skill.get_importance_display(),
                'has_skill': skill_name in student_skill_names
            })

        career_data.append({
            'career': career,
            'required_skills': required_skills
        })

    return render(
        request,
        'career/career_explorer.html',
        {
            'career_data': career_data
        }
    )
@login_required
def career_detail(request, career_id):

    student = Student.objects.get(
        user=request.user
    )

    career = Career.objects.prefetch_related(
        'required_skills__skill'
    ).get(
        id=career_id
    )

    student_skill_names = set(
        student.student_skills.values_list(
            'skill__skill_name',
            flat=True
        )
    )

    skills_have = []
    skills_missing = []

    for career_skill in career.required_skills.all():

        skill_name = career_skill.skill.skill_name

        skill_data = {
            'name': skill_name,
            'importance': career_skill.get_importance_display()
        }

        if skill_name in student_skill_names:
            skills_have.append(skill_data)
        else:
            skills_missing.append(skill_data)

    return render(
        request,
        'career/career_detail.html',
        {
            'career': career,
            'skills_have': skills_have,
            'skills_missing': skills_missing,
        }
    )