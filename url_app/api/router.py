from rest_framework.routers import DefaultRouter
from url_app.api.views import shorterURLApiViewSet

router_url_app = DefaultRouter()
router_url_app.register(prefix='url_app', basename='url_app', viewset=shorterURLApiViewSet)