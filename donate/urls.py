from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gallery", views.gallery, name="gallery"),
    path("news", views.news, name="news"),
    path("events", views.events, name="events"),
    path("event/<int:event_id>", views.event, name="event"),
    path("horse/<int:horse_id>", views.horse, name="horse"),
    path("publication/<int:publication_id>", views.publication, name="publication"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)