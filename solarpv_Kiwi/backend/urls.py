from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Product', views.ProductView)
router.register('Certificate', views.CertificateView)
router.register('Service', views.ServiceView)

urlpatterns = [
    path('API/', include(router.urls))
]