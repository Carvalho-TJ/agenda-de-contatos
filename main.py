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
  # elif opcao == "2":
  # elif opcao == "3":
  # elif opcao == "4":
  # elif opcao == "5":
  # elif opcao == "6":
  elif opcao == "7":
    print("Saindo da agenda de contatos...")
    break