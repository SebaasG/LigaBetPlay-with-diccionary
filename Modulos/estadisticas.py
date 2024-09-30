import Modulos.utils as ut
import Modulos.allMenu as all

contador = 1

def subMenuEquipo(jugadores: dict):
    ut.limpiarConsola()
    isValid = True

    while isValid:
        all.crearMenu(all.menuEstad)
        try:
            opc = int(input(": "))
            if opc == 1:
                ut.limpiarConsola()
                regEstadistica(jugadores)
                print("Se ha registrado correctamente las estadisticas.")
                input("Presione cualquier tecla para continuar...")
                ut.limpiarConsola()
            elif opc == 2:
                ut.limpiarConsola()
                mostrarJugador(jugadores)
                input("Presione una tecla para continuar")
            elif opc == 3:
                pass
            elif opc == 4:
                isValid = False  
                pass
            elif opc == 5:
                isValid = False  
                ut.limpiarConsola()
            else:
                print("Opción no válida, intente nuevamente.")
        except ValueError:
            print("Hubo un error en el proceso, intente nuevamente.")

def regEstadistica(jugadores: dict):
    print("Escoja a que jugador le va a registrar las estadisticas: ")
    for idJugador, datosJugador in jugadores.items():
        print(f"ID: {idJugador}, Nombre: {datosJugador['nombre']}, Equipo: {datosJugador['equipo']}")
    
    opc = input(": ").zfill(2)
    
    if opc in jugadores:
        goles = input("Ingrese goles anotados: ")
        tarAmar = input("Ingrese tarjetas amarillas: ")
        tarRoja = input("Ingrese tarjetas rojas: ")
        falcom = input("Ingrese faltas cometidas: ")
        
        jugadores[opc]['golAn'] = int(goles)
        jugadores[opc]['tarjeAma'] = int(tarAmar)
        jugadores[opc]['tarjeRoja'] = int(tarRoja)
        jugadores[opc]['FalCome'] = int(falcom)
    else:
        print("No disponible en la lista")

def mostrarJugador(jugadores):
    for idJugador, datosJugador in jugadores.items():
        print(f"ID: {idJugador}")
        print(f"Nombre: {datosJugador['nombre']}")
        print(f"Equipo: {datosJugador['equipo']}")
        print(f"Dorsal: {datosJugador['dorsal']}")
        print(f"Posición: {datosJugador['posicion']}")
        print(f"Goles anotados: {datosJugador['golAn']}")
        print(f"Tarjetas amarillas: {datosJugador['tarjeAma']}")
        print(f"Tarjetas rojas: {datosJugador['tarjeRoja']}")
        print(f"Faltas cometidas: {datosJugador['FalCome']}")
        print("-" * 30)  