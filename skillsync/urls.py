from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path(
        'recommendation/',
        include('recommendation.urls')
    ),
path(
        'careers/',
        include('career.urls')
    ),
path(
        'opportunities/',
        include('opportunity.urls')
    ),

]