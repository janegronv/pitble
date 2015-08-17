from django.contrib import admin
from pitble.pitapp.models import Pitble

# Register your models here.
class PitbleAdmin(admin.ModelAdmin):
     list_display = ('text','owner')
     search_fields = ('text',)

admin.site.register(Pitble, PitbleAdmin)