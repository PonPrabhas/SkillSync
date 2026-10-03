from django.urls import path
from . import views
from .views import (
    home,
    register,
    login_view,
    dashboard,
    profile,
    my_skills,
    projects,
    certificates,
    logout_view
)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
path(
    'my-skills/',
    my_skills,
    name='my_skills'
),
path(
    'projects/',
    projects,
    name='projects'
),

path(
    'certificates/',
    certificates,
    name='certificates'
),
path(
    "delete-account/",
    views.delete_account,
    name="delete_account"
),
]