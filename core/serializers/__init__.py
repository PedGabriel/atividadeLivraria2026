from .user import UserRegistrationSerializer, UserSerializer
from .autor import AutorSerializer
from .livro import LivroRetriveSerializer, LivroListSerializer, LivroSerializer
from .editora import EditoraSerializer
from .categoria import CategoriaSerializer
from .compra import (
    CompraCreateUpdateSerializer,
    CompraListSerializer, 
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraListSerializer, 
    ItensCompraSerializer,
)