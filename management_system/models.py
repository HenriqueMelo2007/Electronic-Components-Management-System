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
    
class Inductor(ElectronicComponent):
  def __init__(self, name, manufacturer, max_voltage, inductance_henry):
    super().__init__(name, manufacturer, max_voltage)
    self._inductance_henry = inductance_henry
    
class VoltageSource(ElectronicComponent):
  def __init__(self, name, manufacturer, max_voltage, voltage_volts):
    super().__init__(name, manufacturer, max_voltage)
    self._voltage_volts = voltage_volts
    
class Switch(ElectronicComponent):
  def __init__(self, name, manufacturer, max_voltage, initial_state):
    super().__init__(name, manufacturer, max_voltage)
    self._initial_state = initial_state

class Diode(ElectronicComponent):
  def __init__(self, name, manufacturer, max_voltage, driving_direction):
    super().__init__(name, manufacturer, max_voltage)
    self._driving_direction = driving_direction

class LED(Diode):
  def __init__(self, name, manufacturer, max_voltage, driving_direction, color):
    super().__init__(name, manufacturer, max_voltage, driving_direction)
    self._color = color