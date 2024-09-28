
import Modulos.utils as ut
def subMenuEquipo(equipos:list):
    try:
        ut.limpiarConsola()
        isValid =True
        while isValid:
            
            print("1. Registrar equipo \n2. Ver Equipos \n3. Volver ")
            opc = int(input(": "))
            if (opc == 1):
                ut.limpiarConsola()
                regEquipo(equipos)
                print("se ha registrado correctamente su equipo")
                input("Presione cualquier tecla para continuar...")
                ut.limpiarConsola()
            elif (opc == 2):
                 ut.limpiarConsola()
                 if(equipos == []):
                     print("Aun no se han registrado equipos")
                     input('Presione cualquier tecla para continuar...')
                     ut.limpiarConsola()
                 else:
                    equiposDispo = [equipo[0] for equipo in equipos]
                    print(f"Los siguientes son los equipos registrados:\n {equiposDispo}")
                    input('Presione cualquier tecla para continuar...')
                    ut.limpiarConsola()

            elif (opc == 3):
                isValid = False  
                ut.limpiarConsola()
            else:
                print("Opción no válida, intente nuevamente.")
            
    except ValueError:
        print("Hubo un error en el proceso, intente nuevamente.")

def regEquipo(eq:list):
    equipo = pedirDatos()
    eq.append(equipo)

    
def pedirDatos ():

    name = str(input("Ingrese el nombre de su equipo: ")).lower()
    datos = [name, 0, 0,0,0,0,0]
    return datos