import Modulos.utils as ui

encuentros = []  # Variable global

def menuPartidos(equipos: list):
    try:
        isValid = True
        while isValid:
            ui.limpiarConsola()
            print("1. Programar partido \n2. Ver partidos \n3. Salir")
            opc = int(input(": "))
            print(opc)
            if opc == 1:
                ui.limpiarConsola()
                programar(equipos)
                input("Presione una tecla para continuar...")
            elif opc == 2:
                ui.limpiarConsola()
                print(f"Estos son los partidos programados: {encuentros}")
                input("Presione una tecla para continuar...")
            elif opc == 3:
                isValid = False
                ui.limpiarConsola()
            else:
                print("Dato no válido, intente con otro")
                input("Presione cualquier tecla...")
                ui.limpiarConsola()
    except ValueError:
        print("Error en el sistema")
    
    return encuentros  # Retorna la lista de encuentros

def programar(equipos: list):
    print(f"Estos son los equipos disponibles: {equipos}")
    equiposDispo = [equipo[0] for equipo in equipos]
    
    print(f"Ingrese el nombre del primer equipo, los disponibles son: \n{equiposDispo}")
    nomEquipo = input(": ")

    if nomEquipo not in equiposDispo:
        print("El equipo ingresado no está disponible.")
        return
    
    equiposDispo.remove(nomEquipo)
    
    print(f"Ingrese el nombre del segundo equipo, los disponibles son: \n{equiposDispo}")
    nomEquipo2 = input(": ")

    if nomEquipo2 not in equiposDispo:
        print("El equipo ingresado no está disponible.")
        return
    
    print(f"Se ha programado la fecha correctamente entre {nomEquipo} y {nomEquipo2}")
    
    print("Ingrese la fecha del encuentro")
    date = str(input(": "))
    fecha = [nomEquipo, nomEquipo2, date]
    encuentros.append(fecha)
