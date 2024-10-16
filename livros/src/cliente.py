def menu_cliente(biblioteca):
    while True:
        opc = int(input("1 - Ver catálogo de livros disponíveis\n"
                        "2 - Solicitar empréstimo de um livro\n"
                        "3 - Devolver um livro\n"
                        "4 - Sair\n"
                        "Digite a opção que deseja: "))

        if opc == 1:
            ver_catalogo_disponivel(biblioteca)
        elif opc == 2:
            solicitar_emprestimo(biblioteca)
        elif opc == 3:
            devolver_livro(biblioteca)
        elif opc == 4:
            print("Saindo do menu do cliente...")
            break

def ver_catalogo_disponivel(biblioteca):
    livros_disponiveis = [livro for livro in biblioteca.lista_livros if livro.disponibilidade]
    if livros_disponiveis:
        for livro in livros_disponiveis:
            livro.exibir_detalhes()
            print("-------------------------------")
    else:
        print("Nenhum livro disponível.")

def solicitar_emprestimo(biblioteca):
    titulo_do_livro = input("Digite o título do livro livro: ")
    for livro in biblioteca.lista_livros:
        if livro.titulo == titulo_do_livro and livro.disponibilidade:
            livro.emprestar()
            break
    else:
        print("Livro não disponível ou não encontrado.")

def devolver_livro(biblioteca):
    titulo_do_livro = input("Digite o título do livro: ")
    for livro in biblioteca.lista_livros:
        if livro.titulo == titulo_do_livro and not livro.disponibilidade:
            livro.devolver()
            break
    else:
        print("Livro não encontrado ou já disponível.")
