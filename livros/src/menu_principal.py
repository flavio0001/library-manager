from biblioteca import Biblioteca

def menu_principal():
    biblioteca = Biblioteca()

    while True:
        try:
            opc = int(input("1 - Adicionar um livro à coleção\n"
                            "2 - Listar o catálogo de livros\n"
                            "3 - Remover um livro da coleção\n"
                            "4 - Liberar livro para um cliente\n"
                            "6 - Sair\n"
                            "Digite a opção que deseja: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if opc == 1:
            biblioteca.adicionar_livro()
        elif opc == 2:
            biblioteca.listar_catalogo()
        elif opc == 6:
            print("Saindo do sistema...")
            break
        else:
            print("Opção não implementada ou inválida.")

# Adicione isso no final do arquivo:
if __name__ == "__main__":
    menu_principal()
