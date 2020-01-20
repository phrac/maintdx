"""maintdx URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from maintdx.assets import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'assets', views.AssetViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'locations', views.LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
