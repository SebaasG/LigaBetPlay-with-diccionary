import os

def limpiarConsola():
    os.system("cls" if os.name == "nt" else "clear")

def validar(opc: int, dir: dict) -> bool:
    if opc not in dir:
        print("Su opción no es válida, escoja otra.")
        input('Presione cualquier tecla para continuar...') 
        limpiarConsola()  
        return False 
    return True
