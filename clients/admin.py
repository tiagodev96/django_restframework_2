from django.contrib import admin
from clients.models import Client, Case


class Clients(admin.ModelAdmin):
    list_display = ("id", "name", "email", "document", "phone", "is_active")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("is_active",)
    list_editable = ("is_active",)
    list_per_page = 10
    ordering = ("name",)


admin.site.register(Client, Clients)


class Cases(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_per_page = 10
    ordering = ("name",)


admin.site.register(Case, Cases)
