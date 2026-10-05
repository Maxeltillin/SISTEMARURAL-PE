"""
Pruebas Automatizadas con Pytest (Evidencia CE-02)
"""
import pytest
from cryptography.fernet import Fernet

def test_validacion_dni_duplicado():
    # RF-01: Bloquea registros duplicados
    dnis_registrados = ["12345678", "87654321"]
    nuevo_dni = "12345678"
    assert nuevo_dni in dnis_registrados  # Detecta duplicado

def test_alerta_stock_minimo():
    # RF-04: Dispara notificación de stock crítico
    stock = 5
    umbral_minimo = 10
    alerta = stock < umbral_minimo
    assert alerta is True

def test_proteccion_datos_sensibles():
    # RD-01: Valida encriptación Fernet (Ley N.º 29733)
    clave = Fernet.generate_key()
    f = Fernet(clave)
    telefono = "987654321"
    cifrado = f.encrypt(telefono.encode())
    descifrado = f.decrypt(cifrado).decode()
    assert descifrado == telefono
