
def calcular_clasificacion_y_mvp(rounds):
    jugadores_totales = {}

    for ronda_idx, ronda in enumerate(rounds, start=1):
        clasificacion_ronda = {}
        for jugador, stats in ronda.items():
            puntos = stats['kills'] * 3 + stats['assists'] * 1 - (1 if stats['deaths'] else 0)
            clasificacion_ronda[jugador] = puntos

            # Actualizamos estadísticas totales del jugador
            if jugador not in jugadores_totales:
                jugadores_totales[jugador] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'puntos': 0}
            jugadores_totales[jugador]['kills'] += stats['kills']
            jugadores_totales[jugador]['assists'] += stats['assists']
            jugadores_totales[jugador]['deaths'] += 1 if stats['deaths'] else 0
            jugadores_totales[jugador]['puntos'] += puntos

        # Determinamos el MVP de la ronda
        mvp = max(clasificacion_ronda, key=clasificacion_ronda.get)
        jugadores_totales[mvp]['mvps'] += 1

        # Mostramos el ranking de la ronda con puntajes de la ronda
        print(f"Ronda {ronda_idx}:")
        print("Jugador   Kills   Asistencias   Muertes   Puntos")
        print("__________________________________________________")
        for jugador, puntos in sorted(clasificacion_ronda.items(), key=lambda x: x[1], reverse=True):
            print(f"{jugador:<10}{ronda[jugador]['kills']:<8}{ronda[jugador]['assists']:<13}{ronda[jugador]['deaths']:<9}{puntos:<6}")
        print("_________________________________________________")
        print(f"MVP ronda {ronda_idx}: {mvp}\n")

    return jugadores_totales


# Mostramos el ranking final
def mostrar_ranking_final(jugadores_totales):
    print("Ranking final:")
    print("Jugador   Kills   Asistencias   Muertes   MVPs   Puntos")
    print("________________________________________________________")
    for jugador, stats in sorted(jugadores_totales.items(), key=lambda x: x[1]['puntos'], reverse=True):
        print(f"{jugador:<10}{stats['kills']:<8}{stats['assists']:<13}{stats['deaths']:<9}{stats['mvps']:<7}{stats['puntos']:<6}")
    print("________________________________________________________")
