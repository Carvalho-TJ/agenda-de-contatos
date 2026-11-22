def adicionar_contato(lista_contatos, nome, telefone, email, favorito):
  contato = {
    "nome": nome,
    "telefone": telefone,
    "email": email,
    "favorito": False
  }
  lista_contatos.append(contato)
  print(f"Contato {nome} adicionado com sucesso!")
  return

def visualizar_contatos(lista_contatos):
  print("\nLista de Contatos:")
  for indice, contato in enumerate(lista_contatos, start=1):
    favorito = "★ " if contato["favorito"] else " "
    print(f"{indice}. [{favorito}] Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
  return

def atualizar_contato(lista_contatos, indice_contato, novo_nome, novo_telefone, novo_email):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(lista_contatos):
    lista_contatos[indice_contato_ajustado]["nome"] = novo_nome
    lista_contatos[indice_contato_ajustado]["telefone"] = novo_telefone
    lista_contatos[indice_contato_ajustado]["email"] = novo_email
    print(f"Contato {indice_contato} atualizado com sucesso!")
  else:
    print("Índice de contato inválido.")
  return

def marcar_favorito(lista_contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(lista_contatos):
    contato = lista_contatos[indice_contato_ajustado]
    contato["favorito"] = not contato["favorito"]
    status = "marcado como favorito" if contato["favorito"] else "desmarcado como favorito"
    print(f"Contato {indice_contato} {status}.")
  else:
    print("Índice de contato inválido.")
  return

def visualizar_favoritos(lista_contatos):
  print("\nLista de Contatos Favoritos:")
  for indice, contato in enumerate(lista_contatos, start=1):
    if contato["favorito"]:
      print(f"{indice}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
  return

def deletar_contato(lista_contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(lista_contatos):
    contato = lista_contatos.pop(indice_contato_ajustado)
    print(f"Contato {contato['nome']} deletado com sucesso!")
  else:
    print("Índice de contato inválido.")
  return

lista_contatos = []
while True:
  print("\n********************************************")
  print("Menu Agenda de Contatos:")
  print("1. Adicionar contato")
  print("2. Visualizar lista de contatos")
  print("3. Atualizar/Editar contato")
  print("4. Marcar/Desmarcar contato como favorito")
  print("5. Visualizar lista de contatos favoritos")
  print("6. Deletar contato")
  print("7. Sair")
  print("********************************************\n")

  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    favorito = input("Deseja marcar como favorito? (s/n): ").lower() == "s"
    adicionar_contato(lista_contatos, nome, telefone, email, favorito)
  elif opcao == "2":
    visualizar_contatos(lista_contatos)
  elif opcao == "3":
    visualizar_contatos(lista_contatos)
    indice_contato = input("Digite o índice do contato a ser atualizado: ")
    novo_nome = input("Digite o novo nome do contato: ")
    novo_telefone = input("Digite o novo telefone do contato: ")
    novo_email = input("Digite o novo email do contato: ")
    atualizar_contato(lista_contatos, indice_contato, novo_nome, novo_telefone, novo_email)
  elif opcao == "4":
    visualizar_contatos(lista_contatos)
    indice_contato = input("Digite o índice do contato a ser marcado/desmarcado como favorito: ")
    marcar_favorito(lista_contatos, indice_contato)
  elif opcao == "5":
    visualizar_favoritos(lista_contatos)
  elif opcao == "6":
    visualizar_contatos(lista_contatos)
    indice_contato = input("Digite o índice do contato a ser deletado: ")
    deletar_contato(lista_contatos, indice_contato)
  elif opcao == "7":
    print("Saindo da agenda de contatos...")
    break