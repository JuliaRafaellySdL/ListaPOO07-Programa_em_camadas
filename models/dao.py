import json
from pathlib import Path

class JSONDAO:

    def __init__(self, arquivo, classe):
        self._arquivo = Path(__file__).resolve().parent.parent / arquivo
        self._classe = classe
        self._objetos = []

    def inserir(self, obj):
        self._abrir()
        proximo_id = max((item.get_id() for item in self._objetos), default=0) + 1
        obj.set_id(proximo_id)
        self._objetos.append(obj)
        self._salvar()
        return obj

    def listar(self):
        self._abrir()
        return list(self._objetos)

    def listar_id(self, id):
        self._abrir()
        return next((obj for obj in self._objetos if obj.get_id() == id), None)

    def atualizar(self, obj):
        self._abrir()
        for indice, atual in enumerate(self._objetos):
            if atual.get_id() == obj.get_id():
                self._objetos[indice] = obj
                self._salvar()
                return True
        return False

    def excluir(self, id):
        self._abrir()
        for indice, obj in enumerate(self._objetos):
            if obj.get_id() == id:
                del self._objetos[indice]
                self._salvar()
                return True
        return False

    def _abrir(self):
        if not self._arquivo.exists():
            self._objetos = []
            return
        with self._arquivo.open(encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        self._objetos = [self._classe.from_json(item) for item in dados]

    def _salvar(self):
        with self._arquivo.open("w", encoding="utf-8") as arquivo:
            json.dump([obj.to_json() for obj in self._objetos], arquivo,
                      ensure_ascii=False, indent=2)
