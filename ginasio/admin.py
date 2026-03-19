from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade",)
    ordering = ("nome", "idade",)
    search_fields = ("nome",)

admin.site.register(Cliente, ClienteAdmin)