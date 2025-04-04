rounds = [
{'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}},

{'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}},

{'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}},

{'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}},

{'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}}
]

#queremos saber la clasificacion de cada jugador en cada ronda con base a sus kills, assists y deaths las kills vale 3, los assists 1 y las deaths -1 para ver el MVP de cada ronda
#la clasificacion de cada jugador es la suma de sus kills, assists y deaths en cada ronda
# El MVP es el jugador con la mejor clasificación en cada ronda
def calcular_clasificacion_y_mvp(rounds):
    clasificaciones = []
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

        clasificaciones.append({'clasificacion': clasificacion_ronda, 'mvp': mvp})

        # Mostramos el ranking de la ronda
        print(f"Ranking de la ronda {ronda_idx}:")
        print("Jugador   Kills   Asistencias   Muertes   MVPs   Puntos")
        print("--------------------------------------------------------")
        for jugador, puntos in sorted(clasificacion_ronda.items(), key=lambda x: x[1], reverse=True):
            print(f"{jugador:<10}{jugadores_totales[jugador]['kills']:<8}{jugadores_totales[jugador]['assists']:<13}{jugadores_totales[jugador]['deaths']:<9}{jugadores_totales[jugador]['mvps']:<7}{jugadores_totales[jugador]['puntos']:<6}")
        print("--------------------------------------------------------\n")

    return clasificaciones, jugadores_totales


# Mostramos el ranking final
def mostrar_ranking_final(jugadores_totales):
    print("Ranking final:")
    print("Jugador   Kills   Asistencias   Muertes   MVPs   Puntos")
    print("--------------------------------------------------------")
    for jugador, stats in sorted(jugadores_totales.items(), key=lambda x: x[1]['puntos'], reverse=True):
        print(f"{jugador:<10}{stats['kills']:<8}{stats['assists']:<13}{stats['deaths']:<9}{stats['mvps']:<7}{stats['puntos']:<6}")
    print("--------------------------------------------------------")


# Ejecutamos las funciones
clasificaciones, jugadores_totales = calcular_clasificacion_y_mvp(rounds)
mostrar_ranking_final(jugadores_totales)





 
