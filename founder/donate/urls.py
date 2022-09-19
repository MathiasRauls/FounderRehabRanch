from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gallery", views.gallery, name="gallery"),
    path("horse/<int:horse_id>", views.horse, name="horse"),
    path("publication/<int:publication_id>", views.publication, name="publication"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)