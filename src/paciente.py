"""
Módulo de Gestión de Pacientes y Cifrado (Ley N.º 29733)
"""
from cryptography.fernet import Fernet

class Paciente:
    def __init__(self, dni: str, nombre: str, telefono: str, clave_cifrado: bytes):
        self._dni = dni
        self.nombre = nombre
        self._f = Fernet(clave_cifrado)
        # Cifrado de dato sensible en reposo (RD-01)
        self._telefono_cifrado = self._f.encrypt(telefono.encode())

    def obtener_telefono(self) -> str:
        return self._f.decrypt(self._telefono_cifrado).decode()
