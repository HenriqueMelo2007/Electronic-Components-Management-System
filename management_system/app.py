"""
Logical Core
"""
def truthiness_verification(measurement, message):
    if not (isinstance(measurement, (int, float)) and measurement > 0):
      raise ValueError(f"{message}")
    return 