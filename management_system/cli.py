"""
Input management
"""

from .app import component_registrant, list_components
from .models import Circuit


def header():
    print("-" * 50)
    print(f"{'Sistema de Gerenciamento de Componentes Eletrônicos'}")
    print("Bem-vindo")
    print("-" * 50)


def menu():
    print("\n[1] Adicionar Resistor")
    print("[2] Adicionar Capacitor")
    print("[3] Adicionar Indutor")
    print("[4] Listar Componentes e Calcular Impedâncias")
    print("[0] Sair do Sistema")
    print("-" * 50)
    
def circuit_voltage_definition():
  circuit_voltage = float(input("Defina a Tensão do Circuito em VOLTS o qual será utilizada como parâmetro de tolerância para todos os componentes posteriormente adicionados: "))
  circuit = Circuit(circuit_voltage)
  print(f"{circuit} criado com sucesso!")
  return circuit


def main():
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
