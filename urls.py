"""maintdx URL Configuration

"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

admin.autodiscover()

urlpatterns = (
    [
        path("", include("maintdx.dashboard.urls")),
        path("admin/", admin.site.urls),
        path(r"graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
