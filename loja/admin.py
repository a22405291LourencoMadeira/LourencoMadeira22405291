from django.contrib import admin

from .models import Produto

class LojaAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco",)
    ordering = ("nome", "preco",)
    search_fields = ("nome",)

admin.site.register(Produto, LojaAdmin)
