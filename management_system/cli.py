"""
Módulo de interface de linha de comando (CLI) para interação com o usuário.

Este módulo provê as funções de entrada e saída (I/O) necessárias para a
gestão de inventário de componentes eletrônicos e configuração de circuitos,
atuando como a camada de visão e controle imediato do sistema.
"""

from .app import component_registrant, list_components
from .models import Circuit


def header():
    """
    Exibe o cabeçalho estilizado do sistema no terminal.
    """
    print("-" * 50)
    print(f"{'Sistema de Gerenciamento de Componentes Eletrônicos'}")
    print("Bem-vindo")
    print("-" * 50)


def menu():
    """
    Exibe as opções operacionais disponíveis para o usuário, incluindo
    cadastro de componentes passivos e listagem de dados.
    """
    print("\n[1] Adicionar Resistor")
    print("[2] Adicionar Capacitor")
    print("[3] Adicionar Indutor")
    print("[4] Listar Componentes e Calcular Impedâncias")
    print("[0] Sair do Sistema")
    print("-" * 50)


def circuit_voltage_definition():
    """
    Solicita a tensão nominal via entrada padrão e instancia um objeto Circuit.

    O valor fornecido estabelece o referencial de tensão para o cálculo de
    conformidade e tolerância de todos os componentes vinculados a este circuito.

    Returns:
        Circuit: Instância da classe Circuit configurada com a tensão informada.
    """
    circuit_voltage = float(
        input(
            "Defina a Tensão do Circuito em VOLTS o qual será utilizada como parâmetro de tolerância para todos os componentes posteriormente adicionados: "
        )
    )
    circuit = Circuit(circuit_voltage)
    print(f"{circuit} criado com sucesso!")
    return circuit


def main():
    """
    Ponto de entrada do programa que gerencia o loop principal de execução.

    Coordena o fluxo de estados da aplicação: inicializa o inventário,
    instancia o circuito global, processa as escolhas do menu e despacha
    as requisições para os módulos de registro e listagem.
    """
    inventory = []

    header()
    circuit = circuit_voltage_definition()
    while True:
        menu()
        user_option = input("Selecione uma opção: ").strip()

        if user_option == "0":
            print("\nEncerrando sistema...")
            break

        if user_option in ["1", "2", "3"]:
            inventory.append(component_registrant(user_option, circuit))

        elif user_option == "4":
            if not inventory:
                print("\nO inventário está vazio.")
                continue

            list_components(inventory)

        else:
            print("\nOpção inválida. Tente novamente.")
