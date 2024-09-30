import Modulos.menu as index
import Modulos.menuEquipos as menuE
import Modulos.menuPlantel as menuP
import Modulos.menuPartidos as MenuPar
import Modulos.menuResul as menuRes
import Modulos.estadisticas as menuEstad

def main():
    equipos = {}
    jugadores = {}
    encuentros = {}
    activeMenu = True
    
    while activeMenu:
        res = index.crearMenu()
        
        if res == 1:
            try:
                menuE.subMenuEquipo(equipos)
            except ValueError:
                print("Ha ocurrido un error, intente más tarde.")
                
        elif res == 2:
            try:
                menuP.menuPlantel(equipos, jugadores)
            except ValueError:
                print("Ocurrió un error al acceder al menú del plantel.")
                
        elif res == 3:
            resul = MenuPar.menuPartidos(equipos, encuentros)
        elif res == 4:
            res = menuRes.menuResul(encuentros, equipos)
            
        
        elif res == 5:
            menuEstad.subMenuEquipo(jugadores)
        elif res == 6:
            pass
        elif res == 7:
            activeMenu = False
            
if __name__ == "__main__":
    main()
