import Modulos.utils as ut
import Modulos.allMenu as all

contador = 1
def subMenuEquipo(equipos:dict):
    
    ut.limpiarConsola()
    isValid =True
    try:
     
        while isValid:
            all.crearMenu(all.menuEq)
            opc = int(input(": "))
            if (opc == 1):
                ut.limpiarConsola()
                regEquipo(equipos)
                print("se ha registrado correctamente su equipo")
                input("Presione cualquier tecla para continuar...")
                ut.limpiarConsola()
            elif (opc == 2):
                 ut.limpiarConsola()
                 if(equipos == {}):
                     print("Aun no se han registrado equipos")
                     input('Presione cualquier tecla para continuar...')
                     ut.limpiarConsola()
                 else:
                    
                    print(f"Los siguientes son los equipos registrados:\n ")
                    print([a['nombre'] for a in equipos.values()]) 
                    input('Presione cualquier tecla para continuar...')
                    ut.limpiarConsola()

            elif (opc == 3):
                isValid = False  
                ut.limpiarConsola()
            else:
                print("Opción no válida, intente nuevamente.")
            
    except ValueError:
        print("Hubo un error en el proceso, intente nuevamente.")

def regEquipo(eq:dict):
    global contador
    equipo = pedirDatos()
    eq[str(contador).zfill(2)] = equipo
    contador += 1

    
def pedirDatos ():
    name = str(input("Ingrese el nombre de su equipo: ")).lower()
    datos = {
        "nombre" : name,
        "pj" : 0,
        "pg" : 0,
        "pp" : 0,
        "pe" : 0,
        "gf" : 0,
        "gc" : 0,
        
    }
    return datos