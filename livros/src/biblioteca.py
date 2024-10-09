from livro import Livro
import random

class Biblioteca:
    def __init__(self):
        self.lista_livros = []

    def gerar_isbn(self):
        return str(random.randint(100000, 999999))

    def adicionar_livro(self):
        while True:
            title_livros = input("Digite o nome do livro: ")
            autor_livro = input("Informe o nome do autor: ")
            editora_livro = input("Informe o nome da editora: ")
            genero_livro = input("Informe o gênero do livro: ")
            isbn_livro = self.gerar_isbn()
            ano_livro = input("Informe o ano de publicação: ")

            livro = Livro(title_livros, autor_livro, editora_livro, genero_livro, isbn_livro, ano_livro, True)

            while True:
                salvar = input("Deseja adicionar este livro à coleção? Digite (S/N): ").strip().upper()
                if salvar == 'S':
                    self.lista_livros.append(livro)
                    print("Livro salvo com sucesso.")
                    break
                elif salvar == 'N':
                    print("Livro não salvo.")
                    break
                else:
                    print("Por favor, apenas digite S ou N.")

            continuar = input("Deseja adicionar outro livro? Digite (S/N): ").strip().upper()
            if continuar == 'N':
                break

    def listar_catalogo(self):
        if not self.lista_livros:
            print("Nenhum livro cadastrado")
        else:
            for livro in self.lista_livros:
                livro.exibir_detalhes()
                print("-------------------------------")
