from django.contrib import admin
from contacts.models import Contact

@admin.register(Contact)
class AdSpaceAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','age','phone_number']
    search_fields = ['first_name','last_name','email','phone_number']
    list_filter = ['first_name','last_name','phone_number']
