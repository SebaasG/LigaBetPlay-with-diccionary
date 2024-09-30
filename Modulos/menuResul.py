import Modulos.utils as ut
import Modulos.allMenu as all

# Diccionario global para almacenar los resultados de los partidos
resultados = {}

def menuResul(fechas: dict, equipos: dict):
    isValid = True
    ut.limpiarConsola() 
    try:
        while isValid:
            print(fechas)  # Mostrar fechas
            all.crearMenu(all.menuResul)  
            opc = int(input(": "))  

            if opc == 1:
                regiResul(fechas, equipos)  
            elif opc == 2:
                verResultados()  # Opción para ver resultados
            elif opc == 3:
                verResultados() 
            elif opc == 4:
                isValid = False  
            else:
                print("Escogió un valor inválido")
                input("Presione cualquier tecla para continuar...")
                ut.limpiarConsola()

    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
        input("Presione cualquier tecla para continuar...")
        ut.limpiarConsola()

# Función para registrar el resultado de un encuentro en una fecha
def regiResul(fechas, equipos):
    if not fechas:
        print("No hay fechas disponibles.")
        input("Presione cualquier tecla para continuar...")
        return

    print("¿A qué encuentro le quiere registrar el resultado?")
    for index, fecha in enumerate(fechas.keys()):  
        print(f"{index + 1}. {fecha}")
    
    try:
        opc = int(input(": ")) - 1
        if opc < 0 or opc >= len(fechas):
            print("Escogió un valor inválido.")
            input("Presione cualquier tecla para continuar...")
            return
        
        numFecha = list(fechas.keys())[opc]  # Obtener la clave correspondiente
        resultado(numFecha, equipos)

    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
        input("Presione cualquier tecla para continuar...")

def resultado(numFecha, equipos):
    try:
        golesEq1 = int(input(f"¿Cuántos goles anotó el {equipos['01']['nombre']}?: "))
        golesEq2 = int(input(f"¿Cuántos goles anotó el {equipos['02']['nombre']}?: "))

        # Guardar el resultado en el diccionario global
        resultados[numFecha] = {
            "equipo1": equipos['01']['nombre'],
            "golesEq1": golesEq1,
            "golesEq2": golesEq2,
            "equipo2": equipos['02']['nombre']
        }

        actualizar("01", golesEq1, golesEq2, equipos)
        actualizar("02", golesEq2, golesEq1, equipos)

        print(f"Resultado registrado para la fecha {numFecha}:")
        print(f"{equipos['01']['nombre']} {golesEq1} - {golesEq2} {equipos['02']['nombre']}")
        input("Presione cualquier tecla para continuar...")

    except ValueError:
        print("Error: Ingrese un número válido para los goles.")
        input("Presione cualquier tecla para continuar...")

def actualizar(idEquipo, golesFavor, golesContra, equipos):
    equipos[idEquipo]['gf'] += golesFavor
    equipos[idEquipo]['gc'] += golesContra
    equipos[idEquipo]['pj'] += 1 

    if golesFavor > golesContra:
        equipos[idEquipo]['pg'] += 1  
        equipos[idEquipo]['pt'] += 3  
    elif golesFavor < golesContra:
        equipos[idEquipo]['pp'] += 1  
    else:
        equipos[idEquipo]['pe'] += 1 
        equipos[idEquipo]['pt'] += 1  

    # Mostrar datos actualizados del equipo
    print(f"\nDatos actualizados de {equipos[idEquipo]['nombre']}:")
    for key, value in equipos[idEquipo].items():
        print(f"{key}: {value}")

def verResultados():
    if not resultados:
        print("No hay resultados registrados.")
        input("Presione cualquier tecla para continuar...")
        return

    print("== Resultados Registrados ==")
    for fecha, resultado in resultados.items():
        print(f"Fecha: {fecha}")
        print(f"{resultado['equipo1']} {resultado['golesEq1']} - {resultado['golesEq2']} {resultado['equipo2']}")
        print("=============================")
    input("Presione cualquier tecla para continuar...")
    
    
def mostrarTablaPosiciones(equipos: dict):
    print("\n== Tabla de Posiciones ==")
    print(f"{'Equipo':<20} {'PJ':<5} {'PG':<5} {'PP':<5} {'PE':<5} {'GF':<5} {'GC':<5} {'PT':<5}")
    print("="*50)

    for idEquipo, datos in equipos.items():
        print(f"{datos['nombre']:<20} {datos['pj']:<5} {datos['pg']:<5} {datos['pp']:<5} {datos['pe']:<5} {datos['gf']:<5} {datos['gc']:<5} {datos['pt']:<5}")

    input("Presione cualquier tecla para continuar...")

