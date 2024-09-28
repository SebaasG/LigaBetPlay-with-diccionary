import os

def crearMenu():
    options = [1, 2, 3, 4, 5]
    valid = True
    while valid:
        try:
            print("*****************************************************")
            print("****               LIGA BETPLAY                  ****")
            print("*****************************************************")
            menu = (
                "1. Equipos torneo \n"
                "2. Plantel equipos \n"
                "3. Programar partidos \n"
                "4. Resultado fecha \n"
                "5. Salir \n"
            )
            print(menu)
            resul = int(input(":"))
            if resul not in options:
                print("Su opción no es válida, escoja otra.")
                print('Presione cualquier tecla para continuar...')
                os.system("cls" if os.name == "nt" else "clear")
                continue

        except ValueError as e:
            print(f"El dato no es válido: {e}")
            print('Presione cualquier tecla para continuar...')
            os.system("cls" if os.name == "nt" else "clear")
        
        else:
            valid = False
            return resul