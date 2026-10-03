from django.urls import path

from .views import career_prediction


urlpatterns = [
    path(
        '',
        career_prediction,
        name='career_prediction'
    ),
]