class Livro:
    def __init__(self, titulo, autor, editora, genero, isbn, ano, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.genero = genero
        self.isbn = isbn
        self.ano = ano
        self.disponibilidade = disponibilidade

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nEditora: {self.editora}\nGênero: {self.genero}\nAno de publicação: {self.ano}\nNúmero de identificação do livro: {self.isbn}")

    def emprestar(self):
        if self.disponibilidade:
            self.disponibilidade = False
            print(f"O livro {self.titulo} foi emprestado")
        else:
            print(f"O livro {self.titulo} já está emprestado")

    def devolver(self):
        if not self.disponibilidade:
            self.disponibilidade = True
            print(f"O livro {self.titulo} foi devolvido")
        else:
            print(f"O livro {self.titulo} já está disponível")
