import Modulos.allMenu as all
import Modulos.utils as ui

def crearMenu():
    valid = True
    while valid:
        try:
            print("*****************************************************")
            print("****               LIGA BETPLAY                  ****")
            print("*****************************************************")
            all.crearMenu(all.menuP)
            
            resul = int(input(":"))
          
            if not ui.validar(resul, all.menuP):  
                continue
            
            valid = False  
        
        except ValueError as e:
            print(f"El dato no es válido: {e}")
            input('Presione cualquier tecla para continuar...')
            ui.limpiarConsola()  
    
    return resul 
