from django.contrib import admin
from pitble.pitapp.models import Pitble

# Register your models here.
class PitbleAdmin(admin.ModelAdmin):
     pass

admin.site.register(Pitble, PitbleAdmin)