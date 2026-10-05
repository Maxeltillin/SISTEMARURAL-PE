"""
Procesamiento de Citas usando Programación Funcional (map, filter, reduce)
"""
from functools import reduce

def procesar_citas(citas: list):
    # MAP: Extraer nombres de pacientes
    nombres = list(map(lambda c: c["nombre"], citas))
    
    # FILTER: Aislar citas programadas pendientes
    pendientes = list(filter(lambda c: c["estado"] == "Programada", citas))
    
    # REDUCE: Contar el total de citas completadas
    total_atendidas = reduce(
        lambda cont, c: cont + 1 if c["estado"] == "Completada" else cont,
        citas, 0
    )
    return nombres, pendientes, total_atendidas
