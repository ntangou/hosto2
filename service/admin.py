from django.contrib import admin
from .models import Service, Titre, Personnel

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom_service', 'specialisteM', 'specialisteF')
    fields = [('image_service', 'nom_service'), ('specialisteM', 'specialisteF'), ]
    ordering = ('nom_service',)


class TitreAdmin(admin.ModelAdmin):
    list_display = ('titre',)
    ordering = ('titre',)

class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('titre', 'nom_personnel', 'prenom_personnel', 'sexe', 'service')
    fieldsets = (
        ('   ', {
            'fields': [('nom_personnel', 'prenom_personnel', 'sexe')]
        }),

        ('   ', {
            'fields': [('titre', 'service', 'photo_personnel')]
        }),
    )
    ordering = ('nom_personnel',)

admin.site.register(Titre, TitreAdmin)
admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Service, ServiceAdmin)
