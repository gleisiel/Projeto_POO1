from livro import *
from membro import *

class Biblioteca:
    def __init__(self,nome):
        self.nome = nome
        self.catalogo = []
        self.membros= []
       

    def add_livros(self,titulo,autor,id):
      livro1= Livro(id,titulo,autor)
      self.catalogo.append(livro1)
      print(f'Novo livro ao catalago:{livro1.titulo}')

    def add_membro(self,nome,numero):
        membro1= Membro(nome,numero)
        self.catalogo.append(membro1)
        print(f'Novo membro adicionado {membro1.nome}')

    def listar_livros(self):
        for livro in self.catalogo:
            print(livro.titulo)
    def listar_membro(self):
        for membro in self.registro:
            print(membro.titulo)
    def emprestar_livros(self,id,numero):
        resposta = ''
        for livro in self.catalogo:
            if livro.id == id:
                if livro.status == 'disponivel':
                    livro.status = 'emprestado'
                    for membro in self.membros:
                        if membro.numero == numero:
                            membro.historico.append(livro.titulo)
                            resposta=f'Livro "{livro.titulo}"'
                        break
                else:
                    resposta=f'Livro "{livro.titulo}" já está emprestado'
            return resposta

    def devolver_livros(self,id):
        resposta = ''
        for livro in self.catalogo:
            if livro.id == id:
                livro.status = 'disponível'
                resposta = f'Livro "{livro.titulo}" devolvidoo'
                break
            else:
               resposta = f'Livro "{livro.titulo}" não estava emprestado'
        return resposta


while True:
    print("----------------------------------")
    print("------------BIBLIOTECA------------")
    print("----------------------------------")
    print("Digite 1 para adicionar livros")
    print("Digite 2 para adicionar membro")
    print("Digite 3 para listar os livros")
    print("Digite 4 para listar os membros")
    print("Digite 5 para emprestar livros")
    print("Digite 6 para devolver livros")
    print("Digite 0 para encerrar")
    print("----------------------------------")



    opcao = int(input("Digite a opcao desejada-->"))
    if opcao == 0:
        print("\n... Encerrando a biblioteca")
        break
    elif opcao == 1:
        titulo = input("Digite o titulo do livro: ")
        autor = input("Digite o autor do livro: ")
        id = input("Digite o id do livro: ")
        Biblioteca.add_livros(titulo,autor,id)
    elif opcao == 2:
        nome = input("Digite o nome do membro: ")
        numero = input("Digite o numero de membro: ")
        Biblioteca.add_membro(nome,numero)
    elif opcao == 3:
        Biblioteca.listar_livros()
    elif opcao == 4:
        Biblioteca.listar_membro()
    elif opcao == 5:
        Biblioteca.emprestar_livros()
    elif opcao == 6:
        Biblioteca.devolver_livros()





    



