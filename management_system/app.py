"""
Logical Core
"""

from .models import Resistor, Capacitor, Inductor


def component_registrant(user_option):
    try:
        print("\n--- Cadastro de Componente ---")
        name = input("Nome do componente: ")
        manufacturer = input("Fabricante: ")
        max_voltage = float(input("Tensão Máxima (V): "))

        if user_option == "1":
            measurement_value = float(input("Resistência (Ohms): "))
            electronic_component_object = Resistor(
                name, manufacturer, max_voltage, measurement_value
            )
        elif user_option == "2":
            measurement_value = float(input("Capacitância (Farads): "))
            electronic_component_object = Capacitor(
                name, manufacturer, max_voltage, measurement_value
            )
        elif user_option == "3":
            measurement_value = float(input("Indutância (Henries): "))
            electronic_component_object = Inductor(
                name, manufacturer, max_voltage, measurement_value
            )

        print(f"\n{name} adicionado com sucesso!")
        return electronic_component_object

    except ValueError:
        print(
            "\nErro: Por favor, insira valores numéricos válidos para grandezas físicas."
        )


def components_impedance(inventory):
    frequence = float(input("\nInforme a frequência de operação do circuito (Hz): "))
    print(f"\n--- Análise de Circuito em Série (f = {frequence} Hz) ---")

    total_impedance = 0
    circuit_diagram = "[Fonte]--"

    for electronic_component in inventory:
        component_impedance = electronic_component.impedance_calc(frequence)
        total_impedance += component_impedance

        print(f"{electronic_component} |Z|: {component_impedance:.2f} Ω")
        circuit_diagram += f"[{electronic_component._name}]--"
    return circuit_diagram, total_impedance


def list_components(inventory):
    try:
        circuit_diagram, total_impedance = components_impedance(inventory)
        print(f"{circuit_diagram}[GND]")
        print("-" * 50)
        print(f"Impedância Total Estimada: {total_impedance:.2f} Ω")
        print("Nota: Cálculo escalar (soma linear das magnitudes).")

    except ValueError:
        print("\n❌ Erro: Frequência deve ser um número.")
