import Modulos.utils as ui
import Modulos.allMenu as all
from datetime import datetime

# Variable global para almacenar encuentros y contador
encuentros = {}
contador = 1

# Función principal del menú de partidos
def menuPartidos(equipos: dict):
    isValid = True
    try:
        while isValid:
            ui.limpiarConsola()
            all.crearMenu(all.menuPar)
            opc = input("Seleccione una opción: ")

            if opc.isdigit():
                opc = int(opc)
            else:
                print("Debe ingresar un número.")
                input("Presione cualquier tecla para continuar...")
                continue

            if opc == 1:
                ui.limpiarConsola()
                programar(equipos)
                input("Presione una tecla para continuar...")
            elif opc == 2:
                ui.limpiarConsola()
                mostrarPartidos()
                input("Presione una tecla para continuar...")
            elif opc == 3:
                isValid = False
                ui.limpiarConsola()
            else:
                print("Dato no válido, intente con otro.")
                input("Presione cualquier tecla para continuar...")
                ui.limpiarConsola()
    except ValueError as ve:
        print(f"Error en el sistema: {ve}")

    return encuentros

# Función para validar la fecha
def validarFecha(fecha_str: str) -> bool:
    formato = "%Y-%m-%d"
    try:
        fecha = datetime.strptime(fecha_str, formato)
        return True
    except ValueError:
        return False

# Función para programar partidos
def programar(equipos: dict):
    global contador
    nombresEquipos = [equipo["nombre"] for equipo in equipos.values()]

    # Selección del primer equipo
    print(f"Equipos disponibles: {nombresEquipos}")
    equipo1 = input("Ingrese el nombre del primer equipo: ")

    if equipo1 not in nombresEquipos:
        print("El equipo ingresado no está disponible.")
        return

    nombresEquipos.remove(equipo1)

    # Selección del segundo equipo
    print(f"Equipos disponibles: {nombresEquipos}")
    equipo2 = input("Ingrese el nombre del segundo equipo: ")

    if equipo2 not in nombresEquipos:
        print("El equipo ingresado no está disponible.")
        return

    # Programación del encuentro
    print(f"Se ha programado la fecha correctamente entre {equipo1} y {equipo2}")

    # Validación de fecha
    fecha_valida = False
    while not fecha_valida:
        date = input("Ingrese la fecha del encuentro (formato AAAA-MM-DD): ")
        if validarFecha(date):
            fecha_valida = True
        else:
            print("Formato de fecha no válido. Intente nuevamente.")

    # Registro del encuentro
    encuentro = {
        "equipo1": equipo1,
        "equipo2": equipo2,
        "fecha": date
    }

    encuentros[str(contador).zfill(2)] = encuentro
    contador += 1

    print("El encuentro ha sido registrado correctamente.")
    
def mostrarPartidos():
    if not encuentros:
        print("No hay partidos programados.")
        return

    print("== Partidos Programados ==")
    for id_encuentro, datos in encuentros.items():
        equipo1 = datos["equipo1"]
        equipo2 = datos["equipo2"]
        fecha = datos["fecha"]
        print(f"Partido {id_encuentro}:")
        print(f"{equipo1} vs {equipo2}")
        print(f"Fecha: {fecha}")
        print("==========================")
