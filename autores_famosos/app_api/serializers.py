from rest_framework.serializers import ModelSerializer
from autores.models import Autor

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields =['pk'', nombre','nacionalidad', 'fecha_nacimiento', 'fecha_fallecimiento', 'activo'] 