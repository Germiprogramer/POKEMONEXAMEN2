from classes.pokemon import *
from classes.pokemon_planta import *
from classes.pokemon_electrico import *
from classes.pokemon_agua import *
from classes.pokemon_fuego import *

def orden(pokemon_1, pokemon_2):
    if pokemon_1.speed_rating >= pokemon_2.speed_rating:
        pokemon_1.attack(pokemon_2)
        pokemon_2.attack(pokemon_1)
    else:
        pokemon_2.attack(pokemon_1)
        pokemon_1.attack(pokemon_2)

def combate(pokemon_1, pokemon_2):
    orden(pokemon_1, pokemon_2)
    if pokemon_1.get_health_points() >0 and pokemon_2.get_health_points()>0:
        combate(pokemon_1, pokemon_2)
    else:
        if pokemon_1.get_health_points() <=0:
            print("{} se ha debilitado, la victoria es para {}".format(pokemon_1.get_pokemon_name(),pokemon_2.get_pokemon_name()))
        if pokemon_2.get_health_points() <=0:
            print("{} se ha debilitado, la victoria es para {}".format(pokemon_2.get_pokemon_name(),pokemon_1.get_pokemon_name()))
