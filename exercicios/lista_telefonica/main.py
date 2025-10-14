listaTelefonica = {}

def exibirLista():
  if not listaTelefonica:
    mensagemListaVazia()
  else:
    for nome, numero in listaTelefonica.items():
      print(nome, numero)
       
def exibirTodosContatos():
  if not listaTelefonica:
    mensagemListaVazia()
  else:
    print("Nomes Salvos\n")
    for nome in listaTelefonica:
      print(nome)

def adicionarContato(nome, numero):
  if contatoExiste(nome):
    print(f"O contato {nome} já existe!")
  else:
    listaTelefonica[nome] = numero
    print("O contato foi adicionado com sucesso!")

def removerContato(nome):
  if nome in listaTelefonica:
    listaTelefonica.pop(nome)
    print("Contato removido!")
  else:
    print(f"O nome {nome} não existe na lista telefônica")

def atualizarNumero(nome, numeroNovo):
  if contatoExiste(nome):
    listaTelefonica[nome] = numeroNovo
    print("O número foi atualzado com sucesso!")
  else:
    print("Só é possível atualizar números de contatos existentes")

def procurarContato(nomeContatoProcurado):
  if contatoExiste(nomeContatoProcurado):
    numeroContatoProcurado = listaTelefonica[nomeContatoProcurado]
    print(f"O número de {nomeContatoProcurado} está salvo como {numeroContatoProcurado}")
  else:
    print(f"O contato {nomeContatoProcurado} não existe na lista telefônica")

def normalizarString(string):
  return string.strip().upper()

def contatoExiste(nomeContatoProcurado):
  return nomeContatoProcurado in listaTelefonica
    
def mensagemListaVazia():
  print("Lista telefônica vazia! Nenhum contato ainda foi adicionado!")

def opcaoEscolhidaValidada():
  entrada = input("\nDigite o número associado a opção desejada: ")
  while(not(entrada.isdigit()) and ((int(entrada))<1 or (int(entrada))>7)):
    print("Informe apenas números associado com as opções mostradas")
    entrada = int(input("\nDigite o número associado a opção desejada: "))

  return int(entrada)

def exibirMenu():
  print("- - - - - - - - - - Menu de Seleção - - - - - - - - - -")
  opcoesMenu = ["Ver lista telefônica (nomes e números)", "Ver todos os contatos (nomes)", "Adicionar contato", "Remover contato", "Procurar contato", "Atualizar contato", "Sair"]
  for index, element in enumerate(opcoesMenu):
    print(index+1, "-", element)

print("Seja bem vindo(a) a sua lista telefônica!\n")

exibirMenu()
opcaoEscolhida = opcaoEscolhidaValidada()

while(opcaoEscolhida!=7):
  if opcaoEscolhida == 1:
    exibirLista()
  elif opcaoEscolhida == 2:
    exibirTodosContatos()    
  elif opcaoEscolhida == 3:
    nome = normalizarString(input("Informe o nome: "))
    numero = normalizarString(input("Informe o número: "))
    adicionarContato(nome, numero)
  elif opcaoEscolhida == 4:
    if not listaTelefonica:
      mensagemListaVazia()
    else:
      nome = normalizarString(input("Informe o nome do contato: "))
      removerContato(nome)
  elif opcaoEscolhida == 5:
    if not listaTelefonica:
      mensagemListaVazia()
    else:
      nome = normalizarString(input("Informe o nome do contato: "))
      procurarContato(nome)
  elif opcaoEscolhida == 6:
    if not listaTelefonica:
      mensagemListaVazia()
    else:
      nome = normalizarString(input("Informe o nome do contato: "))
      novoNumero = normalizarString(input("Informe o novo número: "))
      atualizarNumero(nome, novoNumero)

  exibirMenu()
  opcaoEscolhida = opcaoEscolhidaValidada()

print("Programa encerrado!")