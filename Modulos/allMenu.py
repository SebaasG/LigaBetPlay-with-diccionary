menuP = {
    1 : "Equipos torneo",
    2 : "Plantel equipos",
    3 : "Programar partidos",
    4 : "Resultado fecha",
    5 : "Estadisticas",
    6 : "Información general",
    7 : "Salir"
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
    1: "Tecnico",
    2: "Asistente tecnico",
    3: "Preparador fisico",
    4: "Cuerpo medico"
}

menuPar = {
    1 : "Programar partido",
    2 : "Ver partidos",
    3 : "Volver"
}

menuEstad = {
    1 : "Registar estadistica jugador",
    2 : "Ver estadisticas de jugadores",
    3 : "Jugador que más falta ha cometido",
    4 : "Jugador con más tarjetas amarillas",
    5 : "Volver"
}

menuResul = {
    1 : "Registrar resultados",
    2 : "Ver resultados",
    3 : "Ver tabla de posiciones",
    4 : "Volver"
}


def crearMenu(dir: dict):
    for key, value in dir.items():
        print(f"{key}) {value}")


