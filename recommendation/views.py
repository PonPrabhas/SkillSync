from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from student.models import Student

from .ml_model import (
    predict_careers,
    get_skill_gap,
    get_skill_recommendations
)


@login_required
def career_prediction(request):

    student = Student.objects.get(
        user=request.user
    )

    predictions = predict_careers(student)

    top_career = predictions[0]['career']

    skills_have, skills_missing = get_skill_gap(
        student,
        top_career
    )

    recommendations = get_skill_recommendations(
        skills_missing
    )

    return render(
        request,
        'recommendation/career_prediction.html',
        {
            'student': student,
            'predictions': predictions,
            'top_career': top_career,
            'skills_have': skills_have,
            'skills_missing': skills_missing,
            'recommendations': recommendations,
        }
    )