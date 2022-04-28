from classes.pokemon import * 

class Pokemon_electrico(Pokemon):
    nombre_ataque = "impactrueno"
    
    def eficacias(self, pokemon_2):
        if type(pokemon_2).__name__ == "Pokemon_agua":
            self.attack_rating = self.attack_rating * 2
            if pokemon_2.get_health_points()<0:
                self.attack_rating = self.attack_rating/2
        else:
            pass
        return self.attack_rating
