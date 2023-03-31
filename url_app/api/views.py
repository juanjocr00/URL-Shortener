from rest_framework.viewsets import ModelViewSet
from url_app.models import shorterURL
from url_app.api.serializers import shorterURLSerializer

class shorterURLApiViewSet(ModelViewSet):
    serializer_class = shorterURLSerializer
    queryset = shorterURL.objects.all()
