# Arquivo: desafios.py
# Projeto: Mini To-Do List
# Objetivo: completar as funções para que o sistema funcione corretamente
# Dica: use apenas listas, loops e condicionais!
# Lista principal de tarefas
tarefas = []


# Desafio 01: Adicionar uma nova tarefa
def adicionar_tarefa(titulo):
    """
    Adiciona uma nova tarefa à lista.
    Dica: use append() para inserir o título na lista 'tarefas'.
    """
    # TODO: implemente aqui lógica de adicionar tarefa
    tarefas.append(titulo)
    print(f"Tarefa '{titulo}' adicionada com sucesso.")


# Desafio 02: Listar todas as tarefas
def listar_tarefas():
    """
    Exibe todas as tarefas da lista numeradas.
    Dica: use um for com enumerate() para mostrar o índice e o nome.
    """
    # TODO: implementar lógica de listagem
    if not tarefas:
        print("A lista de tarefas está vazia.")
        return

    print("\n--- LISTA DE TAREFAS ---")
    # enumerate() retorna o índice (começando em 0) e o valor
    for indice, tarefa in enumerate(tarefas):
        # Para o usuário, a numeração deve começar em 1, então usamos (indice + 1)
        print(f"{indice + 1} - {tarefa}")
    print("------------------------")


# Desafio 03: Marcar uma tarefa como concluída
def concluir_tarefa(indice):
    """
    Marca uma tarefa como concluída.
    Dica: você pode alterar o texto da tarefa adicionando um 'ok' no início.
    Exemplo: 'Estudar Git' → 'Estudar Git - ok'
    """
    # TODO: implementar lógica de conclusão de tarefa
    # Ajuste o índice para o índice real da lista (começa em 0)
    indice_ajustado = indice - 1

    # Verificação de índice válido
    if 0 <= indice_ajustado < len(tarefas):
        tarefa_original = tarefas[indice_ajustado]
        # Verifica se já está marcada como concluída para evitar duplicidade
        if " - ok" not in tarefa_original:
            tarefas[indice_ajustado] = tarefa_original + " - ok"
            print(f"Tarefa {indice}: '{tarefa_original}' marcada como concluída.")
        else:
            print(f"Tarefa {indice} já está concluída.")
    else:
        print("Índice de tarefa inválido.")


# Desafio 04: Remover uma tarefa
def remover_tarefa(indice):
    """
    Remove uma tarefa pelo índice.
    Dica: use pop() para remover da lista.
    """
    # TODO: implementar lógica de remoção
    # Ajuste o índice para o índice real da lista (começa em 0)
    indice_ajustado = indice - 1

    # Verificação de índice válido
    if 0 <= indice_ajustado < len(tarefas):
        # pop() remove e retorna o item no índice
        tarefa_removida = tarefas.pop(indice_ajustado)
        print(f"Tarefa {indice}: '{tarefa_removida}' removida com sucesso.")
    else:
        print("Índice de tarefa inválido.")


# Desafio 05: Buscar tarefa pelo nome
def buscar_tarefa(nome):
    """
    Busca uma tarefa pelo nome e retorna se ela existe ou não.
    Dica: use um loop para percorrer a lista e comparar strings.
    """
    # TODO: implementar lógica de busca
    encontrada = False
    
    # Loop para percorrer a lista
    for indice, tarefa in enumerate(tarefas):
        # Convertendo para minúsculas para uma busca que ignore caixa (case-insensitive)
        if nome.lower() in tarefa.lower():
            print(f"Tarefa encontrada no índice {indice + 1}: {tarefa}")
            encontrada = True
            # Continuamos o loop para mostrar todas as ocorrências
    
    if not encontrada:
        print(f"Nenhuma tarefa encontrada contendo '{nome}'.")
    return encontrada # Retorna True ou False conforme o desafio


# Desafio 06: Menu interativo (opcional)
def menu():
    """
    Exibe um menu simples para testar o programa.
    Dica: use um while True e input() para ler opções do usuário.
    """
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
                # Garante que o título não é vazio
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

# Descomente a linha abaixo para testar o menu interativo:
# menu()