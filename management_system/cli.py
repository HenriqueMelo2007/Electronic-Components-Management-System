"""
Input management
"""

from .app import component_registrant


def header():
    print("-" * 50)
    print(f"{'Sistema de Gerenciamento de Componentes Eletrônicos':^50}")
    print("Bem-vindo")
    print("-" * 50)


def menu():
    print("\n[1] Adicionar Resistor")
    print("[2] Adicionar Capacitor")
    print("[3] Adicionar Indutor")
    print("[4] Listar Componentes e Calcular Impedâncias")
    print("[0] Sair do Sistema")
    print("-" * 50)


def main():
    inventory = []

    header()
    while True:
        menu()
        user_option = input("Selecione uma opção: ").strip()

        if user_option == "0":
            print("\nEncerrando sistema...")
            break

        if user_option in ["1", "2", "3"]:
            inventory.append(component_registrant(user_option))

        elif user_option == "4":
            if not inventory:
                print("\nO inventário está vazio.")
                continue

            try:
                freq = float(
                    input("\nInforme a frequência de operação do circuito (Hz): ")
                )
                print(f"\n--- Análise de Circuito Série (f = {freq} Hz) ---")

                impedancia_total = 0
                # Visualização do circuito
                circuito_visual = "[Fonte]--"

                for c in inventory:
                    z = c.impedance_calc(freq)
                    impedancia_total += z
                    tipo = c.__class__.__name__

                    print(f"ID: {c._name:10} | Tipo: {tipo:10} | |Z|: {z:,.2f} Ω")
                    circuito_visual += f"[{c._name}]--"

                print(f"{circuito_visual}[GND]")
                print("-" * 50)
                print(f"Impedância Total Estimada: {impedancia_total:,.2f} Ω")
                print("Nota: Cálculo escalar (soma linear das magnitudes).")

            except ValueError:
                print("\n❌ Erro: Frequência deve ser um número.")

        else:
            print("\nOpção inválida. Tente novamente.")
