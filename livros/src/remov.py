def remover(biblioteca):
    if not biblioteca.lista_livros:
        print("Nenhum livro cadastrado.")
        return

    entrada = input("Digite o título ou o ISBN do livro para remover: ").strip()
    livro_removido = None

    for livro in biblioteca.lista_livros:
        if livro.isbn == entrada or livro.titulo.lower() == entrada.lower():
            livro_removido = livro
            break

    if livro_removido:
        biblioteca.lista_livros.remove(livro_removido)
        print(f"Livro '{livro_removido.titulo}' removido com sucesso.")
    else:
        print("Livro não encontrado.")
