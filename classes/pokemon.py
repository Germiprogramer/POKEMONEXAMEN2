class Pokemon():
    def __init__(self, ID, pokemon_name, health_points, attack_rating, defense_rating, speed_rating):
        self.ID = ID
        self.pokemon_name = pokemon_name
        self.health_points = health_points
        self.attack_rating = attack_rating
        self.defense_rating = defense_rating
        self.speed_rating = speed_rating
        
    def get_ID(self):
        return self.ID

    def set_ID(self, a):
        self.ID = a
    
    def get_pokemon_name(self):
        return self.pokemon_name

    def set_pokemon_name(self, a):
        self.pokemon_name = a

    def get_health_points(self):
        return self.health_points

    def set_health_points(self, a):
        self.health_points = a
    
    def get_attack_rating(self):
        return self.attack_rating

    def set_attack_rating(self, a):
        self.attack_rating = a
    
    def get_defense_rating(self):
        return self.defense_rating

    def set_defense_rating(self, a):
        self.defense_rating = a

    def get_speed_rating(self):
        return self.speed_rating

    def set_speed_rating(self, a):
        self.speed_rating = a

    def attack(self, pokemon_2):
        ataque = self.attack_rating-(pokemon_2.get_defense_rating()%2)
        vida = pokemon_2.get_health_points() - ataque
        print("¡{} usa {}!".format(self.pokemon_name, self.nombre_ataque))
        print("¡{} ahora tiene {} puntos de vida!".format(pokemon_2.get_pokemon_name(), vida))
        print("")
        return pokemon_2.set_health_points(vida)

