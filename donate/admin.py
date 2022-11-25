from django.contrib import admin
from .models import *

class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "image",)
    readonly_fields = ("note",)

class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "title", "date", "time", "location", "description",)
    readonly_fields = ("note",)

class PublicationAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "headline", "date", "description",)
    readonly_fields = ("note",)

class PeopleAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "name", "title",)
    readonly_fields = ("note",)

class HorseAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "name", "description")
    readonly_fields = ("note",)

admin.site.register(Banner, BannerAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Horse, HorseAdmin)
