from service import Service


class UI:
    @staticmethod
    def main():
        while True:
            try:
                op = UI.menu()
                if op == 14:
                    print("Aplicação finalizada.")
                    break
                operacoes = {
                    1: UI.cliente_inserir,
                    2: UI.cliente_listar,
                    3: UI.cliente_atualizar,
                    4: UI.cliente_excluir,
                    5: UI.categoria_inserir,
                    6: UI.categoria_listar,
                    7: UI.categoria_atualizar,
                    8: UI.categoria_excluir,
                    9: UI.produto_inserir,
                    10: UI.produto_listar,
                    11: UI.produto_atualizar,
                    12: UI.produto_excluir,
                    13: UI.produto_reajustar,
                }
                acao = operacoes.get(op)
                if acao is None:
                    print("Opção inválida. Escolha uma opção de 1 a 14.")
                    continue
                acao()
            except (ValueError, TypeError) as erro:
                print(f"Entrada inválida: {erro}")
            except OSError as erro:
                print(f"Não foi possível acessar os arquivos de dados: {erro}")

    @staticmethod
    def menu():
        print("\n=== Sistema de Comércio Eletrônico ===")
        print("Clientes:  1 - Inserir | 2 - Listar | 3 - Atualizar | 4 - Excluir") #clientes
        print("Categorias: 5 - Inserir | 6 - Listar | 7 - Atualizar | 8 - Excluir") #categorias
        print("Produtos:   9 - Inserir | 10 - Listar | 11 - Atualizar | 12 - Excluir") #produtos
        print("13 - Reajustar preços | 14 - Finalizar")
        return int(input("Informe a opção: "))

    @staticmethod
    def _ler_id(tipo):
        return int(input(f"Informe o id do {tipo}: "))

    @staticmethod
    def _mostrar_lista(objetos, tipo):
        if not objetos:
            print(f"Nenhum {tipo} cadastrado.")
            return False
        for objeto in objetos:
            print(objeto)
        return True

    @staticmethod
    def _confirmar_resultado(sucesso, tipo, acao):
        if sucesso:
            print(f"{tipo} {acao} com sucesso.")
        else:
            print(f"Não foi possível: registro não encontrado.")

    @staticmethod
    def cliente_inserir():
        nome = input("Informe o nome: ").strip()
        email = input("Informe o e-mail: ").strip()
        fone = input("Informe o fone: ").strip()
        Service.cliente_inserir(nome, email, fone)
        print("Cliente inserido com sucesso.")

    @staticmethod
    def cliente_listar():
        UI._mostrar_lista(Service.cliente_listar(), "cliente")

    @staticmethod
    def cliente_atualizar():
        UI.cliente_listar()
        id = UI._ler_id("cliente")
        if Service.cliente_listar_id(id) is None:
            print("Cliente não encontrado.")
            return
        nome = input("Informe o novo nome: ").strip()
        email = input("Informe o novo e-mail: ").strip()
        fone = input("Informe o novo fone: ").strip()
        UI._confirmar_resultado(Service.cliente_atualizar(id, nome, email, fone), "Cliente", "atualizado")

    @staticmethod
    def cliente_excluir():
        UI.cliente_listar()
        id = UI._ler_id("cliente")
        UI._confirmar_resultado(Service.cliente_excluir(id), "Cliente", "excluído")

    @staticmethod
    def categoria_inserir():
        descricao = input("Informe a descrição da categoria: ").strip()
        Service.categoria_inserir(descricao)
        print("Categoria inserida com sucesso.")

    @staticmethod
    def categoria_listar():
        UI._mostrar_lista(Service.categoria_listar(), "categoria")

    @staticmethod
    def categoria_atualizar():
        UI.categoria_listar()
        id = UI._ler_id("categoria")
        if Service.categoria_listar_id(id) is None:
            print("Categoria não encontrada.")
            return
        descricao = input("Informe a nova descrição: ").strip()
        UI._confirmar_resultado(Service.categoria_atualizar(id, descricao), "Categoria", "atualizada")

    @staticmethod
    def categoria_excluir():
        UI.categoria_listar()
        id = UI._ler_id("categoria")
        UI._confirmar_resultado(Service.categoria_excluir(id), "Categoria", "excluída")

    @staticmethod
    def produto_inserir():
        descricao = input("Informe a descrição do produto: ").strip()
        preco = float(input("Informe o preço: ").replace(",", "."))
        estoque = int(input("Informe a quantidade em estoque: "))
        UI.categoria_listar()
        id_categoria = UI._ler_id("da categoria do produto")
        if Service.categoria_listar_id(id_categoria) is None:
            print("Categoria não encontrada. Produto não foi inserido.")
            return
        Service.produto_inserir(descricao, preco, estoque, id_categoria)
        print("Produto inserido com sucesso.")

    @staticmethod
    def produto_listar():
        UI._mostrar_lista(Service.produto_listar(), "produto")

    @staticmethod
    def produto_atualizar():
        UI.produto_listar()
        id = UI._ler_id("produto")
        if Service.produto_listar_id(id) is None:
            print("Produto não encontrado.")
            return
        descricao = input("Informe a nova descrição: ").strip()
        preco = float(input("Informe o novo preço: ").replace(",", "."))
        estoque = int(input("Informe a nova quantidade em estoque: "))
        UI.categoria_listar()
        id_categoria = UI._ler_id("da categoria do produto")
        if Service.categoria_listar_id(id_categoria) is None:
            print("Categoria não encontrada. Produto não foi atualizado.")
            return
        UI._confirmar_resultado(
            Service.produto_atualizar(id, descricao, preco, estoque, id_categoria),
            "Produto", "atualizado")

    @staticmethod
    def produto_excluir():
        UI.produto_listar()
        id = UI._ler_id("produto")
        UI._confirmar_resultado(Service.produto_excluir(id), "Produto", "excluído")

    @staticmethod
    def produto_reajustar():
        percentual = float(input("Informe o percentual (positivo para reajuste, negativo para promoção): ").replace(",", "."))
        Service.produto_reajustar(percentual)
        print("Preços dos produtos reajustados com sucesso.")


if __name__ == "__main__":
    UI.main()
