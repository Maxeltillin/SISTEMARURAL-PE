"""
SISTEMARURAL-PE: Módulo de Gestión de Salud Rural
Punto de Entrada Principal
"""
from gestor import GestorSistemaSalud

def main():
    print("=== SISTEMA DE SALUD RURAL 'SAN JUAN DE SURCO' ===")
    gestor = GestorSistemaSalud.obtener_instancia()
    print("Sistema iniciado correctamente en modo offline.")

if __name__ == "__main__":
    main()
