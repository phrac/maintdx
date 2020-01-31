"""maintdx URL Configuration

"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rest_framework import routers
from maintdx.assets import views as asset_views
from maintdx.workorders import views as workorder_views
from maintdx.parts import views as part_views
from maintdx.users import views as user_views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'assets', asset_views.AssetViewSet)
router.register(r'categories', asset_views.CategoryViewSet)
router.register(r'category_properties', asset_views.CategoryPropertyViewSet)
router.register(r'departments', asset_views.DepartmentViewSet)
router.register(r'locations', asset_views.LocationViewSet)

router.register(r'work_orders', workorder_views.WorkOrderViewSet)
router.register(r'work_order_types', workorder_views.WorkOrderTypeViewSet)

router.register(r'parts', part_views.PartViewSet)
router.register(r'users', user_views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
