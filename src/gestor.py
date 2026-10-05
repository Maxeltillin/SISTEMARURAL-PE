"""
Patrón Singleton: Gestor Central del Sistema de Salud Rural
"""
class GestorSistemaSalud:
    _instancia = None

    def __init__(self):
        if GestorSistemaSalud._instancia is not None:
            raise Exception("Esta clase es un Singleton. Use obtener_instancia().")
        self.pacientes = []
        self.citas = []
        self.inventario_farmacos = {"Paracetamol": 5}  # Stock bajo para pruebas

    @classmethod
    def obtener_instancia(cls):
        if cls._instancia is None:
            cls._instancia = GestorSistemaSalud()
        return cls._instancia

    def validar_unicidad_dni(self, dni: str) -> bool:
        return not any(p._dni == dni for p in self.pacientes)
