import Modulos.utils as ui
import Modulos.allMenu as all

jugadores = {}
entrenadores = {}
contador = 1

def menuPlantel(equipos:dict):
    ui.limpiarConsola()
    isValid = True
    try:
        while isValid:
            all.crearMenu(all.menuPla)
            opc = int(input(": "))
            if opc == 1:
                validaEquipoDispo(equipos,1)
            elif(opc ==2):
                
                print(f"sus jugadores son los siguientes: {jugadores}")
            elif(opc == 3):
                validaEquipoDispo(equipos,2)
            elif(opc == 4):
                print(f"sus entrenadores son los siguientes: {entrenadores}")
            elif(opc == 5):
                isValid = False
            else:
                print("Opción no válida, intente nuevamente.")
    except ValueError:
        print("Error en la ejecucion del programa")


def registrarJugador (equipo:str):
    global contador
    nom = str(input("Ingrese el nombre del jugador: "))
    dorsal = int(input("Ingrese el dorsal del jugador: "))
    pos = str(input("Ingrese la posición del jugador: "))
    eq = equipo
    jugador = {
        "nombre" : nom,
        "dorsal" : dorsal,
        "posicion": pos,
        "equipo" : eq,
    }
    
    print(f"Se registró con exito a:  {jugador}")
    jugadores[str(contador).zfill(2)] = jugador
    contador += 1


def validaEquipoDispo(equipos:dict, num):
    try:
        info = [info["nombre"] for info in equipos.values()]
        print(info)

        nomEquipo = str(input(": "))
        if(nomEquipo in info):
            print("si está")
        else:
            print("no esta")
        
        
        if(num == 1 ):
            registrarJugador(nomEquipo)
        elif(num == 2):
            registrarEntrenador(nomEquipo)
        return nomEquipo
    except ValueError:
        print("Error en el sistema")


def registrarEntrenador(eq:str):
    global contador
    print(f"Escoja que roll los disponibles son: \n")
    all.crearMenu(all.menuPlaRoll)
    rolEn = int(input(": "))
    nomEn = str(input(f"Nombre: "))
    
    nameRol = all.menuPlaRoll.get(rolEn, "Rol no encontrado")
    
        
    
    entrenador = {
        "nombre" : nomEn,
        "rol" : nameRol,
        "equipo" : eq
    }
    
    entrenadores[str(contador).zfill(1)] = entrenador
    print(f"Se registró con exito a:  {entrenador}")
    contador += 1






    
    
    


    


