import os
from person import Pessoa

lista_pessoas = []

iniciar = 1

def adicionar_pessoa(nome: str, idade: int):
  nova = Pessoa(nome, idade)
  nova.faixa_etaria(idade)
  lista_pessoas.append(nova)

adicionar_pessoa("Vinícius", 18)
adicionar_pessoa("Pedro", 22)
adicionar_pessoa("Antônio", 72)
adicionar_pessoa("João", 8)
adicionar_pessoa("Juliana", 24)
adicionar_pessoa("Leticia", 20)
adicionar_pessoa("Viviane", 66)
adicionar_pessoa("Julia", 4)

while (iniciar == 1):

  opcao = input('''MENU
  1 - ADICIONAR PESSOA
  2 - EXCLUIR PESSOA
  3 - LISTAR PESSOAS POR ORDEM ALFABÉTICA
  4 - LISTAR PESSOAS POR IDADE
  5 - SAIR

  ESCOLHA UMA OPÇÃO: ''')

  opcao = opcao.strip()

  if (opcao == "1"):
    os.system('cls' if os.name == 'nt' else 'clear')
    repete = 1
    while (repete == 1):
      try:
        nome = str(input('''(Digite "menu" para voltar ao menu principal)
Digite o nome da pessoa: '''))
        if (nome.upper().replace(" ", "") == "MENU"):
          repete = 0
          input("Pressione ENTER para continuar")
          os.system('cls' if os.name == 'nt' else 'clear')

        elif nome.strip() == (""):
          print("ERRO - O nome não pode estar em branco")
          input("Pressione ENTER para continuar")
          os.system('cls' if os.name == 'nt' else 'clear')
          repete = 1

        else:  
          idade = int(input('''Digite a idade da pessoa: '''))
          if idade < 0:
            print("ERRO - A idade deve ser a partir de 0")
            input("Pressione ENTER para continuar")
            os.system('cls' if os.name == 'nt' else 'clear')
            repete = 1
          else:
            repete = 0
            nome = nome.strip()
            adicionar_pessoa(nome, idade)
            print(f"ADICIONADO: {lista_pessoas[-1]}")
            input("Pressione ENTER para continuar")
            os.system('cls' if os.name == 'nt' else 'clear')
      
      except ValueError:
        print("ERRO - A idade precisa ser um número inteiro")
        input("Pressione ENTER para continuar")
        os.system('cls' if os.name == 'nt' else 'clear')
        repete = 1
    
  elif (opcao == "2"):
    os.system('cls' if os.name == 'nt' else 'clear')
    repete = 1
    while (repete == 1):
      for n in enumerate(lista_pessoas):
        print(n)

      try:
        codigo_escolhido = input('''Qual pessoa você deseja remover da lista?
Digite o número referente à pessoa ou "menu" para voltar ao menu principal: ''')
        codigo_escolhido = int(codigo_escolhido)
        if (codigo_escolhido < len(lista_pessoas) and codigo_escolhido >= 0):
          print(f"REMOVIDO: Usuário - {lista_pessoas[codigo_escolhido]}")
          del lista_pessoas[codigo_escolhido]
          repete = 0
          input("Pressione ENTER para continuar")
          os.system('cls' if os.name == 'nt' else 'clear')

        else:
          print("ERRO - Insira um número inteiro existente na lista")
          input("Pressione ENTER para continuar")
          os.system('cls' if os.name == 'nt' else 'clear')
          repete = 1

      except ValueError:
        codigo_escolhido = codigo_escolhido.upper().replace(" ", "")
        if (codigo_escolhido == "MENU"):
          repete = 0
          input("Pressione ENTER para continuar")
          os.system('cls' if os.name == 'nt' else 'clear')

        else:
          print("ERRO - Insira um número inteiro existente na lista")
          input("Pressione ENTER para continuar")
          os.system('cls' if os.name == 'nt' else 'clear')
          repete = 1

  elif (opcao == "3"):
    os.system('cls' if os.name == 'nt' else 'clear')
    lista_pessoas_nome = sorted(lista_pessoas, key = Pessoa.get_nome)
    for n in lista_pessoas_nome:
      print(n)
    input("Pressione ENTER para continuar")
    os.system('cls' if os.name == 'nt' else 'clear')

  elif (opcao == "4"):
    os.system('cls' if os.name == 'nt' else 'clear')
    lista_pessoas_idade = sorted(lista_pessoas, key = Pessoa.get_idade)
    for n in lista_pessoas_idade:
      print(n)
    input("Pressione ENTER para continuar")
    os.system('cls' if os.name == 'nt' else 'clear')

  elif (opcao == "5"):
    iniciar = 0

  else:
    print("ERRO - Insira um número de 1 a 5")
    input("Pressione ENTER para continuar")
    os.system('cls' if os.name == 'nt' else 'clear')