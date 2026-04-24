"""
Definições de Modelos e Entidades

Este módulo define a estrutura de dados e o comportamento físico dos componentes
eletrônicos e do circuito, utilizando herança e polimorfismo para o cálculo de
reatâncias e impedâncias.
"""

from math import pi


PI = pi


def truthiness_verification(measurement, message):
    """
    Valida se uma grandeza física é numérica e estritamente positiva.

    Args:
        measurement (any): O valor a ser validado.
        message (str): Mensagem de erro a ser incluída na exceção.

    Raises:
        ValueError: Se o valor não for int/float ou for menor ou igual a zero.
    """
    if not (isinstance(measurement, (int, float)) and measurement > 0):
        raise ValueError(f"{message}")
    return


class Circuit:
    """
    Representa o domínio de operação do sistema elétrico.

    Atributos:
        _voltage (float): Tensão nominal de operação do circuito.
    """

    def __init__(self, voltage):
        truthiness_verification(voltage, "Invalid Voltage")
        self._voltage = voltage

    def __str__(self):
        return f"Circuito {self._voltage}V"


class ElectronicComponent:
    """
    Classe base abstrata para modelagem de dispositivos eletrônicos.

    Define os atributos comuns a todos os componentes e a interface para
    o cálculo de impedância.

    Atributos:
        _name (str): Identificador do componente.
        _manufacturer (str): Nome do fabricante.
        _max_voltage (float): Limite de tensão de segurança.
    """

    def __init__(self, name, manufacturer, max_voltage):
        truthiness_verification(max_voltage, "Invalid Max Voltage")
        self._name = name
        self._manufacturer = manufacturer
        self._max_voltage = max_voltage

    def impedance_calc(self, frequence):
        pass


class Resistor(ElectronicComponent):
    """
    Representa um componente resistivo ideal.

    A impedância de um resistor é independente da frequência e equivalente
    à sua resistência ôhmica nominal.
    """

    def __init__(self, name, manufacturer, max_voltage, resistance_ohm):
        truthiness_verification(resistance_ohm, "Invalid Resistance")
        super().__init__(name, manufacturer, max_voltage)
        self._resistance_ohm = resistance_ohm

    def __str__(self):
        return f"ID: {self._name} | Tipo: {self.__class__.__name__} | Fabricante: {self._manufacturer} |"

    def impedance_calc(self, frequence):
        return self._resistance_ohm


class Capacitor(ElectronicComponent):
    """
    Representa um componente capacitivo.

    Implementa o cálculo da reatância capacitiva (Xc). Em corrente contínua
    (f=0), retorna um valor de magnitude infinita para simular circuito aberto.
    """

    def __init__(self, name, manufacturer, max_voltage, capacitance_farad):
        truthiness_verification(capacitance_farad, "Invalid Capacitance")
        super().__init__(name, manufacturer, max_voltage)
        self._capacitance_farad = capacitance_farad

    def __str__(self):
        return f"ID: {self._name} | Tipo: {self.__class__.__name__} | Fabricante: {self._manufacturer} |"

    def impedance_calc(self, frequence):
        if frequence == 0:
            return 9999999999999999999
        return 1 / (2 * PI * frequence * self._capacitance_farad)


class Inductor(ElectronicComponent):
    """
    Representa um componente indutivo.

    Implementa o cálculo da reatância indutiva (Xl), cuja magnitude é
    diretamente proporcional à frequência de operação.
    """

    def __init__(self, name, manufacturer, max_voltage, inductance_henry):
        truthiness_verification(inductance_henry, "Invalid Inductance")
        super().__init__(name, manufacturer, max_voltage)
        self._inductance_henry = inductance_henry

    def __str__(self):
        return f"ID: {self._name} | Tipo: {self.__class__.__name__} | Fabricante: {self._manufacturer} |"

    def impedance_calc(self, frequence):
        return 2 * PI * frequence * self._inductance_henry
