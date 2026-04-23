"""
Logical Core
"""

from .models import Resistor, Capacitor, Inductor


def truthiness_verification(measurement, message):
    if not (isinstance(measurement, (int, float)) and measurement > 0):
        raise ValueError(f"{message}")
    return


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
        return electronic_component_object # type: ignore

    except ValueError:
        print(
            "\n❌ Erro: Por favor, insira valores numéricos válidos para grandezas físicas."
        )
