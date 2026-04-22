"""
Data and Classes definitions
"""

class ElectronicComponent():
  def __init__(self, name, manufacturer, max_voltage):
    self._name = name
    self._manufacturer = manufacturer
    self._max_voltage = max_voltage
    
class Resistor(ElectronicComponent):
  def __init__(self, name, manufacturer, max_voltage, resistance_ohm):
    super().__init__(name, manufacturer, max_voltage)
    self._resistance_ohm = resistance_ohm
    

class Capacitor(ElectronicComponent):
  def __init__(self, name, manufacturer, max_voltage, capacitance_farad):
    super().__init__(name, manufacturer, max_voltage)
    self._capacitance_farad = capacitance_farad
    
class VoltageSource(ElectronicComponent):
  pass

class LED(ElectronicComponent):
  pass