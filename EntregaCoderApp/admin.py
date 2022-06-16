from django.contrib import admin
from EntregaCoderApp.models import Familiar

# Register your models here.
class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad')
admin.site.register(Familiar, FamiliarAdmin)