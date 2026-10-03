from django.urls import path

from .views import opportunity_list


urlpatterns = [
    path(
        '',
        opportunity_list,
        name='opportunity_list'
    ),
]