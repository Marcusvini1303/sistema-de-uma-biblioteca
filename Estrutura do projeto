class Livro:
    def __init__(self, titulo, autor, isbn, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"'{self.titulo}' emprestado com sucesso.")
        else:
            print(f"'{self.titulo}' está indisponível.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"'{self.titulo}' devolvido com sucesso.")
        else:
            print(f"'{self.titulo}' já está disponível.")

    def __str__(self):
        return f"{self.titulo} - {self.autor} | {'Disponível' if self.disponivel else 'Emprestado'}"

class Cliente():
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

biblioteca = Biblioteca()

# Exemplo: carregando alguns dados iniciais (opcional)
cliente1 = Cliente("João", "1")
cliente2 = Cliente("Maria", "2")
livro1 = Livro("O Senhor dos Anéis", "Tolkien", "123")
livro2 = Livro("Harry Potter", "J.K. Rowling", "456")
biblioteca.cadastrar_cliente(cliente1)
biblioteca.cadastrar_cliente(cliente2)
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

while True:
    print("\n--- Bem-vindo à Biblioteca do Marcus ---")
    print("Menu:")
    print("1. Cadastrar Cliente")
    print("2. Remover Cliente")
    print("3. Adicionar Livro")
    print("4. Remover Livro")
    print("5. Buscar Livro")
    print("6. Listar Livros Disponíveis")
    print("7. Listar Livros Emprestados")
    print("8. Empréstimo de Livro")
    print("9. Devolução de Livro")
    print("10. Sair")

    try:
        menu = int(input("Digite o número correspondente à opção desejada: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if menu == 1:
        nome = input("Nome do cliente: ")
        id_cliente = input("ID do cliente: ")
        novo_cliente = Cliente(nome, id_cliente)
        biblioteca.cadastrar_cliente(novo_cliente)

    elif menu == 2:
        id_cliente = input("ID do cliente para remover: ")
        cliente_remover = next((c for c in biblioteca.clientes_cadastrados if c.id == id_cliente), None)
        if cliente_remover:
            biblioteca.remover_cliente(cliente_remover)
        else:
            print("Cliente não encontrado.")

    elif menu == 3:
        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")
        isbn = input("ISBN do livro: ")
        novo_livro = Livro(titulo, autor, isbn)
        biblioteca.adicionar_livro(novo_livro)

    elif menu == 4:
        titulo = input("Título do livro a remover: ")
        livro_remover = biblioteca.buscar_livro(titulo)
        if livro_remover:
            biblioteca.remover_livro(livro_remover)

    elif menu == 5:
        titulo = input("Digite o título do livro a buscar: ")
        biblioteca.buscar_livro(titulo)

    elif menu == 6:
        biblioteca.listar_livros_disponiveis()

    elif menu == 7:
        biblioteca.listar_livros_emprestados()

    elif menu == 8:
        id_cliente = input("ID do cliente que vai pegar o livro: ")
        cliente = next((c for c in biblioteca.clientes_cadastrados if c.id == id_cliente), None)
        if cliente:
            titulo = input("Título do livro para emprestar: ")
            livro = biblioteca.buscar_livro(titulo)
            if livro:
                cliente.pegar_emprestado(livro)
        else:
            print("Cliente não encontrado.")

    elif menu == 9:
        id_cliente = input("ID do cliente que vai devolver o livro: ")
        cliente = next((c for c in biblioteca.clientes_cadastrados if c.id == id_cliente), None)
        if cliente:
            titulo = input("Título do livro a devolver: ")
            livro = next((l for l in cliente.livros_emprestados if l.titulo.lower() == titulo.lower()), None)
            if livro:
                cliente.devolver_livro(livro)
            else:
                print("Esse cliente não possui esse livro.")
        else:
            print("Cliente não encontrado.")

    elif menu == 10:
        print("Saindo da biblioteca. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
