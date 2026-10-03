from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Opportunity
from student.models import Student


def normalize_skill(skill):
    """
    Convert a skill into a standard form
    so similar skill names can be compared.
    """

    skill = skill.strip().lower()

    replacements = {
        "python programming": "python",
        "python language": "python",

        "javascript programming": "javascript",
        "js": "javascript",

        "html5": "html",
        "css3": "css",

        "mysql": "sql",
        "postgresql": "sql",
        "postgres": "sql",

        "django framework": "django",

        "django rest framework": "rest api",
        "django rest": "rest api",

        "restful api": "rest api",
        "rest api development": "rest api",

        "machine learning": "ml",
        "machine-learning": "ml",

        "git version control": "git",
        "github": "git",
    }

    return replacements.get(skill, skill)


@login_required
def opportunity_list(request):

    student = Student.objects.get(
        user=request.user
    )

    # Get student's skills
    student_skills = set(
        normalize_skill(skill.skill.skill_name)
        for skill in student.student_skills.select_related('skill')
    )

    opportunities = Opportunity.objects.filter(
        is_active=True
    )

    opportunity_data = []

    for opportunity in opportunities:

        # Get required skills
        required_skills = [
            normalize_skill(skill)
            for skill in opportunity.relevant_skills.split(',')
            if skill.strip()
        ]

        # Remove duplicates
        required_skills = list(set(required_skills))

        matched_skills = [
            skill
            for skill in required_skills
            if skill in student_skills
        ]

        if required_skills:
            match_percentage = round(
                (len(matched_skills) / len(required_skills)) * 100
            )
        else:
            match_percentage = 0

        opportunity_data.append({
            'opportunity': opportunity,
            'match_percentage': match_percentage,
            'matched_skills': matched_skills,
        })

    # Highest matching opportunities first
    opportunity_data.sort(
        key=lambda item: item['match_percentage'],
        reverse=True
    )

    return render(
        request,
        'opportunity/opportunity_list.html',
        {
            'opportunity_data': opportunity_data
        }
    )