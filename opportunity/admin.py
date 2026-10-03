from django.contrib import admin

from .models import Opportunity


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):

    list_display = (
        'company_name',
        'opportunity_type',
        'locations',
        'is_active',
    )

    list_filter = (
        'opportunity_type',
        'is_active',
    )

    search_fields = (
        'company_name',
        'relevant_skills',
        'relevant_careers',
    )