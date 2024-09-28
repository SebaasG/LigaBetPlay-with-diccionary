
import os
import Modulos.utils as me

jugadores = []
entrenadores = []
rol = ["Entrenador", "Asistente Tecnico", "Medico o fisioterapeuta"]

def menuPlantel(equipos:list):
    try:
        
        me.limpiarConsola()
        print("este es el menu del plantel ")
        isValid = True

        while isValid:
            print("1. Registrar Jugadores \n2. Ver jugadores \n3. Registrar entrenador\n4.Ver entrenadores\n5. Volver ")
            opc = int(input(": "))
            if(opc == 1):
                validaEquipoDispo(equipos,1)
            elif(opc ==2):
                
                print(f"sus jugadores son los siguientes: {jugadores}")
            elif(opc == 3):
                validaEquipoDispo(equipos,2)
            elif(opc == 4):
                print(f"sus jugadores son los siguientes: {entrenadores}")
            elif(opc == 5):
                isValid = False
            else:
                print("Opción no válida, intente nuevamente.")
    except ValueError:
        print("Error en la ejecucion del programa")


def registrarJugador (equipo:str):
    
    nom = str(input("Ingrese el nombre del jugador: "))
    dorsal = int(input("Ingrese el dorsal del jugador: "))
    pos = str(input("Ingrese la posición del jugador: "))
    eq = equipo
    player= [nom,dorsal,pos,eq]
    
    print(f"Se registró con exito a:  {player[0]}")
    jugadores.append(player)


def validaEquipoDispo(equipos:list, num):
    try:
        equiposDispo = []
        for i in range(0, len(equipos)):
            equiposDispo.append(equipos[i][0])
        print(f"Ingrese el nombre del equipo, los disponibles son los siguientes: \n{equiposDispo}")
        nomEquipo = str(input(": "))
        if (nomEquipo in equiposDispo):

            if(num == 1 ):
                registrarJugador(nomEquipo)
            elif(num == 2):
                registrarEntrenador(nomEquipo)
        return nomEquipo
    except ValueError:
        print("Error en el sistema")


def registrarEntrenador(eq:str):
    print(f"Escoja que roll los disponibles son: \n{rol}")
    roles = str(input(": ")).lower()
    nomEn = str(input(f"Nombre del {rol}: "))
    equipo = eq
    entrenador  = [nomEn,roles,equipo]
    print(f"Se registró con exito a:  {entrenador[0]}")
    entrenadores.append(entrenador)






    
    
    


    


