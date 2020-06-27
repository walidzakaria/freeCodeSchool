from rest_framework import serializers, viewsets
from .models import Certificate


# Create your views here.
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
