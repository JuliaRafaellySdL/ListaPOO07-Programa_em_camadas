from models.dao import JSONDAO
from models.produto import Produto


class ProdutoDAO(JSONDAO):
    def __init__(self):
        super().__init__("produtos.json", Produto)
