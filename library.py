
class livro:
    def __init__(self,titulo,autor,codigo,disponivel):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = disponivel
    def __str__(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nCodigo: {self.codigo}\nDisponivel: {self.disponivel}\n"
def cadastrarLivro(livros):
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    codigo = input("Codigo: ")
    novolivro = livro(titulo,autor,codigo,"True")
    livros.append(novolivro)
    
    
def salvarMudancas(livros):
    arq = open("books.txt","w")
    for x in livros:
        stringfinal = f"{x.titulo},{x.autor},{x.codigo},True\n"
        arq.write(stringfinal)
    print("Salvo com sucesso!")
    
def devolverLivro(livros):
    livroretornado = input("Codigo ou nome do livro que esta retornando: ")
    encontrado = 0
    for x in livros:
        if livroretornado == x.codigo or livroretornado == x.titulo:
            if x.disponivel == "False":
                x.disponivel = "True"
                encontrado = 1
                break
    if encontrado == 0:
        print("LIVRO DESCONHECIDO/NAO CADASTRADO/JA DEVOLVIDO!")
    
def emprestarLivro(livros):
    livropedido = input("Codigo ou nome do livro que quer emprestar: ")
    encontrado = 0
    for x in livros:
        if livropedido == x.codigo or livropedido == x.titulo:
            if x.disponivel == "True":
                x.disponivel = "False"
                encontrado = 1
                break
    if encontrado == 0:
        print("LIVRO DESCONHECIDO/NAO CADASTRADO/JA EMPRESTADO!")
    
def verLivros(livros):
    for x in livros:
        if x.disponivel == "True":
            print(x)
            
livros = []
arq = open("books.txt","r")

for x in arq: ##carregando os livros salvos no txt na lista!
    dadoslivro = x.split(",")
    if "\n" in dadoslivro[3]:
        dadoslivro[3] = dadoslivro[3][:-1]
    print(dadoslivro)
    novolivro = livro(dadoslivro[0],dadoslivro[1],dadoslivro[2],dadoslivro[3])
    livros.append(novolivro)
arq.close()
## menu da biblioteca
select = int(input("Bem vindo ao sistema da biblioteca!\n1- Cadastrar Livro\n2- Devolver Livro\n3- Emprestar Livro\n4- Ver Livros Disponiveis\n5- Salvar para arquivo\n0- Sair\n"))

while select != 0:
    
    match select:
        case 1:
            cadastrarLivro(livros)
        case 2:
            devolverLivro(livros)
        case 3:
            emprestarLivro(livros)
        case 4:
            verLivros(livros)
        case 5:
            salvarMudancas(livros)
            
    select = int(input("Bem vindo ao sistema da biblioteca!\n1- Cadastrar Livro\n2- Devolver Livro\n3- Emprestar Livro\n4- Ver Livros Disponiveis\n5- Salvar para arquivo\n0- Sair\n"))
            
print("Saindo!")

    

