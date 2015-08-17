from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from pitble.pitapp.models import Pitble

# Register your models here.
class PitbleAdmin(admin.ModelAdmin):
     list_display = ('text','owner')
     search_fields = ('text',)

admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Pitble, PitbleAdmin)