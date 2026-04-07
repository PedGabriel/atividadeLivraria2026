from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from core.models import Livro


class LivroListSerializer (ModelSerializer):
    class Meta:
        fields = ('titulo', 'preco', 'id')
        model = Livro


class LivroRetriveSerializer (ModelSerializer):
    capa = ImageSerializer(required=False)
    class Meta:
        fields = '__all__'
        model = Livro
        depth = 1


class LivroSerializer (ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source='capa',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    class Meta:
        fields = '__all__'
        model = Livro
