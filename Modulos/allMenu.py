menuP = {
    1 : "Equipos torneo",
    2 : "Plantel equipos",
    3 : "Programar partidos",
    4 : "Resultado fecha",
    5 : "Salir"
}   

menuEq = {
    1 : "Registrar equipo",
    2 : "Ver Equipos",
    3 : "Volver",
}

menuPla = {
    1 : "Registrar Jugadores",
    2 : "Ver jugadores",
    3 : "Registrar entrenador",
    4 : "Ver entrenadores",
    5 : "Volver"
}

menuPlaRoll = {
    1: "Entrenador",
    2: "Asistente tecnico",
    3: "Medico o fisioterapeuta"
}


def crearMenu(dir: dict):
    for key, value in dir.items():
        print(f"{key}) {value}")


