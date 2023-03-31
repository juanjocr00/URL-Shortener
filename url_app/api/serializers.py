from rest_framework.serializers import ModelSerializer
from url_app.models import shorterURL

class shorterURLSerializer(ModelSerializer):
    class Meta:
        model=shorterURL
        fields = ['original_url', 'shorter_url', 'visit_count', 'private', 'username']
