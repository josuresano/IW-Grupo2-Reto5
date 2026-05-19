from rest_framework import serializers
from .models import NoConformidad, AccionCorrectiva, Responsable

class NoConformidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoConformidad
        fields = '__all__'

class AccionCorrectivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccionCorrectiva
        fields = '__all__'

class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = '__all__'