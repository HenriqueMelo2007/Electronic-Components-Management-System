"""
Data and Classes definitions
"""

from app import truthiness_verification


class ElectronicComponent:
    def __init__(self, name, manufacturer, max_voltage):
        truthiness_verification(max_voltage, "Invalid Max Voltage")
        self._name = name
        self._manufacturer = manufacturer
        self._max_voltage = max_voltage


class Resistor(ElectronicComponent):
    def __init__(self, name, manufacturer, max_voltage, resistance_ohm):
        truthiness_verification(resistance_ohm, "Invalid Resistance")
        super().__init__(name, manufacturer, max_voltage)
        self._resistance_ohm = resistance_ohm


class Capacitor(ElectronicComponent):
    def __init__(self, name, manufacturer, max_voltage, capacitance_farad):
        truthiness_verification(capacitance_farad, "Invalid Capacitance")
        super().__init__(name, manufacturer, max_voltage)
        self._capacitance_farad = capacitance_farad


class Inductor(ElectronicComponent):
    def __init__(self, name, manufacturer, max_voltage, inductance_henry):
        truthiness_verification(inductance_henry, "Invalid Inductance")
        super().__init__(name, manufacturer, max_voltage)
        self._inductance_henry = inductance_henry


class VoltageSource(ElectronicComponent):
    def __init__(self, name, manufacturer, max_voltage, voltage_volts):
        truthiness_verification(voltage_volts, "Invalid Voltage")
        super().__init__(name, manufacturer, max_voltage)
        self._voltage_volts = voltage_volts