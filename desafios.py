
tarefas = []


# Desafio 01: Adicionar uma nova tarefa
def adicionar_tarefa(titulo):
    tarefas.append(titulo)


# Desafio 02: Listar todas as tarefas
def listar_tarefas():
    for i, t in enumerate(tarefas):
        print(f"{i} - {t}")


# Desafio 03: Marcar uma tarefa como concluída
def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice] += " - ok "


# Desafio 04: Remover uma tarefa
def remover_tarefa(indice):
     if 0 <= indice < len(tarefas):
        tarefas.pop(indice)


# Desafio 05: Buscar tarefa pelo nome
def buscar_tarefa(nome):
    for t in tarefas:
        if nome in t:
            print("Tarefa encontrada:", t)
            return
    print("Tarefa não encontrada.")

# Desafio 06: Menu interativo (opcional)
def menu():
    while True:
        print("\n--- MENU TO-DO ---")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Buscar tarefa")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            adicionar_tarefa(titulo)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            indice = int(input("Número da tarefa: "))
            concluir_tarefa(indice)
        elif opcao == "4":
            indice = int(input("Número da tarefa: "))
            remover_tarefa(indice)
        elif opcao == "5":
            nome = input("Nome da tarefa: ")
            buscar_tarefa(nome)
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


