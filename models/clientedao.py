from models.cliente import Cliente
from models.dao import JSONDAO


class ClienteDAO(JSONDAO):
    def __init__(self):
        super().__init__("clientes.json", Cliente)
