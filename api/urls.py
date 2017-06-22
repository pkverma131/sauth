from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet,fetch

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^fetch/',fetch,name='fetch'),
]