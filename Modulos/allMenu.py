menuP = {
    1 : "Equipos torneo",
    2 : "Plantel equipos",
    3 : "Programar partidos",
    4: "Resultado fecha",
    5 : "Salir"
}   

menuEq = {
    1 : "Registrar equipo",
    2 : "Ver Equipos",
    3 : "Volver",
}


def crearMenu(dir: dict):
    for key, value in dir.items():
        print(f"{key}) {value}")


