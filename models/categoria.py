class Categoria:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao

    def __str__(self):
        return f"{self.id} - {self.descricao}"

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def to_json(self):
        return {"id": self.id, "descricao": self.descricao}

    @staticmethod
    def from_json(dados):
        return Categoria(dados["id"], dados["descricao"])
