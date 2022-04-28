import matplotlib.pyplot as plt
from analisis import attack_rating, defense_rating, health_points, media_attack, media_defensa, media_hp
from dispersion import q1_health, q1_attack, q1_defense, q3_health, q3_attack, q3_defense, mediana_health, mediana_attack, mediana_defense

class Grafico():
    def __init__(self, lista, media, mediana, cuartil_1, cuartil_2, cuartil_3):
        self.lista = lista
        self.media = media
        self.mediana = mediana
        self.cuartil_1 = cuartil_1
        self.cuartil_2 = cuartil_2
        self.cuartil_3 = cuartil_3

    def visualizacion(self):  
  
        plt.subplot(2, 2, 1)  
        plt.hist(self.lista)  
        plt.title("Histograma y media")  
        plt.axvline(self.media, color='red', linestyle='dashed',  
        linewidth=1,label = str(self.media))  
        plt.legend(loc='upper right')  
        
        plt.subplot(2, 2, 2)  
        plt.hist(self.lista)  
        plt.title("Histograma y mediana")  
        plt.axvline(self.mediana, color='green', linestyle='dashed',  
        linewidth=1,label = str(self.mediana))  
        plt.legend(loc='upper right')  
        
        plt.subplot(2, 2, 3)  
        plt.hist(self.lista)  
        plt.title("Histograma y cuartiles")  
        plt.axvline(self.cuartil_1, color='orange', linestyle='dashed',  
        linewidth=1,label = "Q1: "+str(self.cuartil_1))  
        plt.axvline(self.cuartil_2, color='orange', linestyle='dashed',  
        linewidth=1,label = "Q2: "+str(self.cuartil_2))  
        plt.axvline(self.cuartil_3, color='orange', linestyle='dashed',  
        linewidth=1,label = "Q3: "+str(self.cuartil_3))  
        plt.legend(loc='upper right')  
        
        plt.subplot(2, 2, 4)  
        plt.boxplot(self.lista)  
        plt.title("Diagrama de caja y bigotes")  
        plt.show() 

grafico_health = Grafico(health_points, media_hp, mediana_health, q1_health, mediana_health, q3_health)

grafico_health.visualizacion()

grafico_attack = Grafico(attack_rating, media_attack, mediana_attack, q1_attack, mediana_attack, q3_attack)

grafico_attack.visualizacion()

grafico_defense = Grafico(defense_rating, media_defensa, mediana_defense, q1_defense, mediana_defense, q3_defense)

grafico_defense.visualizacion()