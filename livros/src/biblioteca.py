from livro import Livro
import random

class Biblioteca:
    def __init__(self):
        self.lista_livros = []

    def gerar_isbn(self):
        return str(random.randint(100000, 999999))

    def adicionar_livro(self):
        titulo = input("Digite o nome do livro: ")
        autor = input("Informe o nome do autor: ")
        editora = input("Informe o nome da editora: ")
        genero = input("Informe o gênero do livro: ")
        isbn = self.gerar_isbn()
        ano = input("Informe o ano de publicação: ")

        livro = Livro(titulo, autor, editora, genero, isbn, ano, True)

        self.lista_livros.append(livro)
        print("Livro adicionado com sucesso.")

    def listar_catalogo(self):
        if not self.lista_livros:
            print("Nenhum livro cadastrado")
        else:
            for livro in self.lista_livros:
                livro.exibir_detalhes()
                print("-------------------------------")
