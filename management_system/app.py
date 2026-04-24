"""
Núcleo Lógico

Este módulo centraliza as operações de negócio da aplicação, incluindo a
instanciação de componentes eletrônicos com validação de parâmetros físicos
e o processamento matemático de grandezas elétricas em regime senoidal.
"""

from .models import Resistor, Capacitor, Inductor


def component_registrant(user_option, circuit):
    """
    Realiza o registro de um componente eletrônico através da entrada de dados.

    Implementa a lógica de validação de segurança elétrica, garantindo que a
    tensão máxima nominal do componente seja superior ou igual à tensão de
    operação do circuito. Utiliza recursão para tratar entradas inválidas.

    Args:
        user_option (str): Identificador do tipo de componente (1: Resistor, 2: Capacitor, 3: Indutor).
        circuit (Circuit): Instância do circuito para validação de limites de tensão.

    Returns:
        Union[Resistor, Capacitor, Inductor]: Instância do componente eletrônico criado.

    Raises:
        ValueError: Disparado caso os valores numéricos sejam inválidos ou a tensão
                    máxima do componente seja inferior à tensão do circuito.
    """
    try:
        print("\n--- Cadastro de Componente ---")
        name = input("Nome do componente: ")
        manufacturer = input("Fabricante: ")
        max_voltage = float(input("Tensão Máxima (V): "))

        if max_voltage < circuit._voltage:
            raise ValueError

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
        return electronic_component_object  # type: ignore

    except ValueError:
        print(
            "\nErro: Por favor, insira valores numéricos válidos para grandezas físicas ou um valor de tensão máxima compatível."
        )
    return component_registrant(user_option, circuit)


def components_impedance(inventory):
    """
    Calcula a impedância individual de cada componente baseada em uma frequência operacional.

    Itera sobre o inventário de componentes, invocando os métodos polimórficos de
    cálculo de impedância (reatâncias capacitiva, indutiva ou resistência pura).

    Args:
        inventory (list): Coleção de objetos derivados da classe base de componentes.

    Returns:
        tuple: (str, float) Contendo a representação visual da topologia do circuito
               em série e a magnitude da impedância total escalonada.
    """
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
    """
    Coordena a exibição dos resultados da análise do circuito e do inventário.

    Interface de saída que apresenta o diagrama esquemático textual, as impedâncias
    individuais e a impedância total estimada, tratando exceções de entrada de dados.

    Args:
        inventory (list): Lista de componentes a serem processados e listados.
    """
    try:
        circuit_diagram, total_impedance = components_impedance(inventory)
        print(f"{circuit_diagram}[GND]")
        print("-" * 50)
        print(f"Impedância Total Estimada: {total_impedance:.2f} Ω")
        print("Nota: Cálculo escalar (soma linear das magnitudes).")

    except ValueError:
        print("\nErro: Frequência deve ser um número.")
