from django.contrib import admin
from .models import  Rdv
from collections import OrderedDict
from datetime import date
from rendez_vous.models import Rdv, Heure
# Register your models here.


class RdvAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'date', 'heure')
    search_fields = ('nom', 'prenom')
    fieldsets = (

        ('          ', {
            'fields': [('nom', 'prenom'), ('date', 'heure')]
        }),
    )
    ordering= ('date',)


class HeureAdmin(admin.ModelAdmin):
    ordering=('heure',)

admin.site.register(Rdv, RdvAdmin)
admin.site.register(Heure, HeureAdmin)