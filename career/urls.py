from django.urls import path

from .views import (
    career_explorer,
    career_detail
)


urlpatterns = [
    path(
        '',
        career_explorer,
        name='career_explorer'
    ),

    path(
        '<int:career_id>/',
        career_detail,
        name='career_detail'
    ),
]