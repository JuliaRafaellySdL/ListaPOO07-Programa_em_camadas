class Produto:
    def __init__(self, id, descricao, preco, estoque, idCategoria):
        self.id = id
        self.descricao = descricao
        self.preco = float(preco)
        self.estoque = int(estoque)
        self.idCategoria = int(idCategoria)

    def __str__(self):
        return (f"{self.id} - {self.descricao} - R$ {self.preco:.2f} - "
                f"Estoque: {self.estoque} - Categoria: {self.idCategoria}")

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def to_json(self):
        return {"id": self.id, "descricao": self.descricao,
                "preco": self.preco, "estoque": self.estoque,
                "idCategoria": self.idCategoria}

    @staticmethod
    def from_json(dados):
        return Produto(dados["id"], dados["descricao"], dados["preco"],
                       dados["estoque"], dados["idCategoria"])
