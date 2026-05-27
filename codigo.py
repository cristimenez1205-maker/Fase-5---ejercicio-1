#PROBLEMA 1 - FASE 5 - CRISTIAN JIMENEZ
# Aquí definimos la matriz con los datos iniciales de las sesiones.
# Cada fila tiene la estructura fija: [ID_Cliente, Tiempo_Segundos, Numero_Clics]
matriz_clientes = [
    [10, 230, 9],  # Cumple ambos: >180s y >8 clics - Alto
    [20, 31, 6],    # Al durar menos de 60s ya es - Bajo
    [30, 140, 2],   # Aunque tiene buen tiempo, sus clics son <3 - Bajo
    [40, 119, 4],   # Caso intermedio que no cae en los extremos - Medio
    [50, 390, 1],   # Dura bastante, pero al tener <3 clics cae en - Bajo
    [60, 180, 8]    # Cumple ambas entradas - Alto
]


def evaluar_sesion(tiempo, clics):
    """
    Función encargada de ejecutar la lógica de negocio de la guía
    para clasificar el nivel de interacción del cliente.
    
    Args:
        tiempo (int): Duración total de la sesión en segundos.
        clics (int): Cantidad de clics hechos por el usuario.
        
    Returns:
        str: El resultado de la clasificación ("Alto", "Bajo", "Medio").
    """
    # Condición para nivel alto: Se deben cumplir los dos requisitos obligatoriamente
    if tiempo > 180 and clics > 8:
        return "Alto"
        
    # Condición para nivel bajo: Con que falle una de las dos variables es suficiente
    elif tiempo < 60 or clics < 3:
        return "Bajo"
        
    # Condición para nivel medio: Cualquier otro registro intermedio
    else:
        return "Medio"


def imprimir_reporte(datos_matriz):
    """
    Módulo que recorre la matriz bidimensional de forma secuencial
    para procesar los datos y mostrar el informe final por consola.
    
    Args:
        datos_matriz (list): La matriz que contiene toda la información.
    """
    # Interfaz visual para la presentación del programa
    print("=" * 60)
    print("REPORTE DE NIVEL DE COMPROMISO DE LOS CLIENTES")
    print("=" * 60)
    print(f"{'ID CLIENTE':<15}{'DURACIÓN':<15}{'CLICS':<12}{'COMPROMISO':<15}")
    print("-" * 60)

    # Ciclo para recorrer cada cliente en la matriz y procesar sus datos
    for cliente in datos_matriz:
        # Extraigo las variables usando las posiciones de los índices
        id_usuario = cliente[0]
        segundos = cliente[1]
        toques_clic = cliente[2]
        
        # Envío los datos a la función lógica para obtener la etiqueta
        resultado_final = evaluar_sesion(segundos, toques_clic)
        
        # Muestro el resultado formateado en columnas limpias
        print(f"{id_usuario:<15}{segundos:<15}{toques_clic:<12}{resultado_final:<15}")
        
    print("=" * 60)


# Bloque principal para ejecutar el programa
if __name__ == "__main__":
    imprimir_reporte(matriz_clientes)
