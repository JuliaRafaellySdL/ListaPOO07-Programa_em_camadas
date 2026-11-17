from models.categoria import Categoria
from models.dao import JSONDAO


class CategoriaDAO(JSONDAO):
    def __init__(self):
        super().__init__("categorias.json", Categoria)
