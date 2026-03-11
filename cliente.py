class Cliente:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.livros_emprestados = []

    def pegar_emprestado(self, livro):
        if livro.disponivel:
            livro.emprestar()
            self.livros_emprestados.append(livro)
            print(f"{self.nome} pegou '{livro.titulo}' emprestado.")
        else:
            print(f"{self.nome} tentou pegar '{livro.titulo}', mas está indisponível.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            print(f"{self.nome} devolveu '{livro.titulo}'.")
        else:
            print(f"{self.nome} não possui o livro '{livro.titulo}'.")
