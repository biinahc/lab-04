# Arquivo: desafios.py
# Projeto: Mini To-Do List
# Objetivo: completar as funções para que o sistema funcione corretamente
# Dica: use apenas listas, loops e condicionais!
# Lista principal de tarefas
tarefas = []


# Desafio 01: Adicionar uma nova tarefa
def adicionar_tarefa(titulo):
    tarefas.append(titulo)
    print(f"Tarefa {titulo} adicionada com sucesso :D")


# Desafio 02: Listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("A lista de tarefas está vazia.")
        return

    print("\n--- LISTA DE TAREFAS ---")
    for indice, tarefa in enumerate(tarefas):
        print(f"{indice + 1} - {tarefa}")
    print("------------------------")

# Desafio 03: Marcar uma tarefa como concluída
def concluir_tarefa(indice):
    indice_ajustado = indice - 1

    if 0 <= indice_ajustado < len(tarefas):
        tarefa_original = tarefas[indice_ajustado]
        if " - ok" not in tarefa_original:
            tarefas[indice_ajustado] = tarefa_original + " - ok"
            print(f"Tarefa {indice}: '{tarefa_original}' marcada como concluída.")
        else:
            print(f"Tarefa {indice} já está concluída.")
    else:
        print("Índice de tarefa inválido.")


# Desafio 04: Remover uma tarefa
def remover_tarefa(indice):
    indice_ajustado = indice - 1

    if 0 <= indice_ajustado < len(tarefas):
        tarefa_removida = tarefas.pop(indice_ajustado)
        print(f"Tarefa {indice}: '{tarefa_removida}' removida com sucesso.")
    else:
        print("Índice de tarefa inválido.")

# Desafio 05: Buscar tarefa pelo nome
def buscar_tarefa(nome):
    encontrada = False
    
    for indice, tarefa in enumerate(tarefas):
        if nome.lower() in tarefa.lower():
            print(f"Tarefa encontrada no índice {indice + 1}: {tarefa}")
            encontrada = True
    
    if not encontrada:
        print(f"Nenhuma tarefa encontrada contendo '{nome}'.")
    return encontrada 



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

        try:
            if opcao == "1":
                titulo = input("Título da tarefa: ")
                if titulo.strip():
                    adicionar_tarefa(titulo.strip())
                else:
                    print("O título da tarefa não pode ser vazio.")
            elif opcao == "2":
                listar_tarefas()
            elif opcao == "3":
                listar_tarefas()
                if tarefas:
                    indice = int(input("Número da tarefa a concluir: "))
                    concluir_tarefa(indice)
            elif opcao == "4":
                listar_tarefas()
                if tarefas:
                    indice = int(input("Número da tarefa a remover: "))
                    remover_tarefa(indice)
            elif opcao == "5":
                nome = input("Nome ou parte do nome da tarefa para buscar: ")
                buscar_tarefa(nome.strip())
            elif opcao == "0":
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
             print("Entrada inválida. Por favor, digite um número para o índice.")
        except Exception as e:
             print(f"Ocorreu um erro: {e}")

menu()