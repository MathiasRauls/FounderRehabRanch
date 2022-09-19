from django.contrib import admin
from .models import *

class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "image",)
    readonly_fields = ("note",)

class PublicationAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "headline", "description",)
    readonly_fields = ("note",)

class PeopleAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "name", "title",)
    readonly_fields = ("note",)

class HorseAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "name", "description")
    readonly_fields = ("note",)

admin.site.register(Banner, BannerAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Horse, HorseAdmin)
