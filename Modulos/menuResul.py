import Modulos.utils as ut


def menuResul(fechas:list):
    try:
        isValid = True
        while isValid:
            print("1. Registrar resultados\n2. Ver Registrar\n3.Salir")
            opc = int(input(": "))
            if(opc ==1):
                regiResul(fechas)
            elif(opc == 2):
                pass
            elif(opc ==3):
                isValid = False
            else:
                print("Escogió un valor invalido")
                input("Presione cualquier tecla para continuar...")
                ut.limpiarConsola()
    except ValueError:
        print("Error en el sistema")
    
    
def regiResul(fechas):
    
    print("¿A qué encuentro le quiere registrar el resultado?")
    for index, fecha in enumerate(fechas):
        print(f"{index + 1}. {fecha}")
    opc = int(input(": "))
    
    print(len(fechas))

def resultado(numFecha):

    int(print("Cuantos goles "))
    