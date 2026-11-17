from models.categoria import Categoria
from models.categoriadao import CategoriaDAO
from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.produto import Produto
from models.produtodao import ProdutoDAO


class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        return ClienteDAO().inserir(Cliente(0, nome, email, fone))

    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        return ClienteDAO().atualizar(Cliente(id, nome, email, fone))

    @staticmethod
    def cliente_excluir(id):
        return ClienteDAO().excluir(id)

    @staticmethod
    def categoria_inserir(descricao):
        return CategoriaDAO().inserir(Categoria(0, descricao))

    @staticmethod
    def categoria_listar():
        return CategoriaDAO().listar()

    @staticmethod
    def categoria_listar_id(id):
        return CategoriaDAO().listar_id(id)

    @staticmethod
    def categoria_atualizar(id, descricao):
        return CategoriaDAO().atualizar(Categoria(id, descricao))

    @staticmethod
    def categoria_excluir(id):
        return CategoriaDAO().excluir(id)

    @staticmethod
    def produto_inserir(descricao, preco, estoque, idCategoria):
        return ProdutoDAO().inserir(Produto(0, descricao, preco, estoque, idCategoria))

    @staticmethod
    def produto_listar():
        return ProdutoDAO().listar()

    @staticmethod
    def produto_listar_id(id):
        return ProdutoDAO().listar_id(id)

    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, idCategoria):
        return ProdutoDAO().atualizar(Produto(id, descricao, preco, estoque, idCategoria))

    @staticmethod
    def produto_excluir(id):
        return ProdutoDAO().excluir(id)

    @staticmethod
    def produto_reajustar(percentual):
        dao = ProdutoDAO()
        for produto in dao.listar():
            produto.preco *= 1 + percentual / 100
            dao.atualizar(produto)
