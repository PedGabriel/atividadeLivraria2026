from .user import UserRegistrationSerializer, UserSerializer
from .autor import AutorSerializer
from .livro import (
    LivroMaisVendidoSerializer, 
    LivroAjustarEstoqueSerializer,
    LivroAlterarPrecoSerializer,
    LivroListSerializer,
    LivroRetrieveSerializer,
    LivroSerializer,
)
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