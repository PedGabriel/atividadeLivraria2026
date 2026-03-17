from rest_framework.serializers import ModelSerializer

from core.models import Livro


class LivroSerializer (ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Livro
