from classes.pokemon import *
from classes.pokemon_planta import *
from classes.pokemon_electrico import *
from classes.pokemon_agua import *
from classes.pokemon_fuego import *
from combate import *

pokemon_1 = ""
pokemon_2 = ""

def combateconcambio(pokemonentrenador1, pokemonentrenador2):
    i = 0
    j = 0

    if i >= len(pokemonentrenador1):
            pass
    else:
        if pokemonentrenador1[i].get_health_points() <0:
            print("¡CAMBIO DE POKEMON, ENTRA {} Y SALE {}!".format(pokemonentrenador1[i+1].get_pokemon_name(),pokemonentrenador1[i].get_pokemon_name()))
            i = i + 1
    
    if j >= len(pokemonentrenador2):
            pass
    else:
        if pokemonentrenador2[j].get_health_points() <0:
            print("¡CAMBIO DE POKEMON, ENTRA {} Y SALE {}!".format(pokemonentrenador2[i+1].get_pokemon_name(),pokemonentrenador2[i].get_pokemon_name()))
            j = j + 1

    if pokemonentrenador1[i].get_health_points() >0 and pokemonentrenador2[j].get_health_points()>0:
        pokemonentrenador1[i].eficacias(pokemonentrenador2[j])
        pokemonentrenador2[j].eficacias(pokemonentrenador1[i])
        combate(pokemonentrenador1[i], pokemonentrenador2[j])
        
    if pokemonentrenador1[i].get_health_points()>0 or pokemonentrenador2[j].get_health_points()>0:
        try:
            combateconcambio(pokemonentrenador1, pokemonentrenador2)
        except:
            pass
    else:
        pass
