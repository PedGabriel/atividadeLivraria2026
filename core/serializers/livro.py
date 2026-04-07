from rest_framework.serializers import ModelSerializer

from core.models import Livro


class LivroRetriveSerializer (ModelSerializer):
    class Meta:
        fields = ('titulo', 'preco', 'id')
        model = Livro


class LivroListSerializer (ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Livro
        depth = 1


class LivroSerializer (ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Livro
