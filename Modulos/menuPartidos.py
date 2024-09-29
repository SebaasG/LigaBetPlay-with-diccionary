import Modulos.utils as ui
import Modulos.allMenu as all

encuentros = {}

def menuPartidos(equipos: dict):
    isValid = True
    try:
    
        while isValid:
            ui.limpiarConsola()
            all.crearMenu(all.menuPar)
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
    
    info = [info["nombre"] for info in equipos.values()]
    print(f"Ingrese el nombre del primer equipo, los disponibles son: \n{info}")
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
