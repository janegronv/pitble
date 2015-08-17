from django.contrib import admin
from django.contrib.auth import get_user_model

from pitble.pitapp.models import Pitble

# Register your models here.

class PitbleAdmin(admin.ModelAdmin):
     list_display = ('text','owner')
     search_fields = ('text',)

admin.site.register(get_user_model())
admin.site.register(Pitble, PitbleAdmin)