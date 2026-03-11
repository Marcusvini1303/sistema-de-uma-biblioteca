class Biblioteca:
    def __init__(self):
        self.acervo = []
        self.clientes_cadastrados = []

    def cadastrar_cliente(self, cliente):
        self.clientes_cadastrados.append(cliente)
        print("Cliente cadastrado com sucesso")

    def remover_cliente(self, cliente):
        if cliente in self.clientes_cadastrados:
            self.clientes_cadastrados.remove(cliente)
            print("Cliente removido com sucesso")
        else:
            print("Cliente não encontrado na lista")

    def adicionar_livro(self, livro):
        self.acervo.append(livro)
        print("Livro adicionado com sucesso!")

    def remover_livro(self, livro):
        if livro in self.acervo:
            self.acervo.remove(livro)
            print(f"Livro '{livro.titulo}' removido com sucesso!")
        else:
            print("Livro não encontrado no acervo.")

    def buscar_livro(self, titulo):
        for livro in self.acervo:
            if livro.titulo.lower() == titulo.lower():
                print(f"Livro encontrado: {livro}")
                return livro
        print("Livro não encontrado!")
        return None

    def listar_livros_disponiveis(self):
        print(" Livros disponíveis:")
        for livro in self.acervo:
            if livro.disponivel:
                print(" -", livro)

    def listar_livros_emprestados(self):
        print(" Livros emprestados:")
        for livro in self.acervo:
            if not livro.disponivel:
                print(" -", livro)
