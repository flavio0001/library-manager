from remov import remover

def menu_bibliotecario(biblioteca):
    while True:
        opc = int(input("1 - Adicionar um livro à coleção\n"
                        "2 - Listar o catálogo de livros\n"
                        "3 - Remover um livro da coleção\n"
                        "4 - Verificar lista de empréstimo de livros\n"
                        "5 - Sair\n"
                        "Digite a opção que deseja: "))

        if opc == 1:
            biblioteca.adicionar_livro()
        elif opc == 2:
            biblioteca.listar_catalogo()
        elif opc == 3:
            remover(biblioteca)
        elif opc == 4:
            lista_emprestimos(biblioteca)
        elif opc == 5:
            print("Saindo do menu do bibliotecário...")
            break
