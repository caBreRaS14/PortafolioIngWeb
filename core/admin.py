from django.contrib import admin
from .models import Contact, Series, FAQ

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nombre','correo','telefono','creado')
    readonly_fields = ('creado',)

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title','content_type','created_at')
    list_filter = ('content_type',)
    search_fields = ('title','keywords','summary')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'creado')
    search_fields = ('pregunta', 'respuesta')