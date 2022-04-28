from analisis import attack_rating, defense_rating, health_points, max_value_hp, min_value_health, max_value_attack, min_value_attack, max_value_defense, min_value_defense, l, media_attack, media_defensa, media_hp

# 1. EL RANGO
print("1. RANGO")

print("El rango de hp {}".format(max_value_hp - min_value_health))
print("El rango de attack {}".format(max_value_attack - min_value_attack))
print("El rango de defense {}".format(max_value_defense - min_value_defense))

# 2. DESVIACIÓN TÍPICA
print("2. DESVIACIÓN TÍPICA")

lista_var_hp = []

for i in range(l):
    lista_var_hp.append((health_points[i] - media_hp)**2)
print("La varianza de los hp es {}".format((sum(health_points)/l)))

print("La desviación típica de hp es {}".format((sum(lista_var_hp)/l)**0.5))

print("En base al rango, se puede ver que los puntos estan bastante dispersos")

lista_var_attack = []

for i in range(l):
    lista_var_attack.append((attack_rating[i] - media_attack)**2)
print("La varianza de ataque es {}".format((sum(lista_var_attack)/l)))

print("La desviación típica de ataqures {}".format((sum(lista_var_attack)/l)**0.5))

print("En base al rango, se puede ver que los puntos estan bastante dispersos")

lista_var_defense = []

for i in range(l):
    lista_var_defense.append((defense_rating[i] - media_defensa)**2)
print("La varianza de las notas de defense es {}".format((sum(lista_var_defense)/l)))

print("La desviación típica de las defensas es {}".format((sum(lista_var_defense)/l)**0.5))

print("En base al rango, se puede ver que los puntos estan bastante dispersos")

# 3. CUARTILES Y RANGO INTERCUARTILICO

print(" 3.1 CUARTILES")
valor_q1 = int(l/4)
valor_q3 = int(3*l/4)
valor_medio = int(l/2)

q1_health = (health_points[valor_q1] + health_points[valor_q1 + 1])/2
mediana_health = (health_points[valor_medio] + health_points[valor_medio + 1])/2
q3_health = (health_points[valor_q3] + health_points[valor_q3 + 1])/2

print("El 25% de hp son menores que {}".format(q1_health))
print("El 50% de los hp son menores que {}".format(media_hp))
print("El 75% de los hp son menores que {}".format(q3_health))

q1_attack = (attack_rating[valor_q1] + attack_rating[valor_q1 + 1])/2
mediana_attack = (attack_rating[valor_medio] + attack_rating[valor_medio + 1])/2
q3_attack = (attack_rating[valor_q3] + attack_rating[valor_q3 + 1])/2

print("El 25% de los valores de ataque son menores que {}".format(q1_attack))
print("El 50% de los valores de staque son menores que {}".format(media_attack))
print("El 75% de los valores de ataque son menores que {}".format(q3_attack))

q1_defense = (defense_rating[valor_q1] + defense_rating[valor_q1 + 1])/2
mediana_defense = (defense_rating[valor_medio] + defense_rating[valor_medio + 1])/2
q3_defense = (defense_rating[valor_q3] + defense_rating[valor_q3 + 1])/2

print("El 25% de los valores de defensa son menores que {}".format(q1_defense))
print("El 50% de los valores de defensa son menores que {}".format(media_defensa))
print("El 75% de los valores de defensa son menores que {}".format(q3_defense))

print("3.2 RANGO INTERCUARTILICO")

print("Rango intercuartílico hp = {}".format(q3_health-q1_health))
print("Rango intercuartílico attaque = {}".format(q3_attack-q1_attack))
print("Rango intercuartílico defensa = {}".format(q3_defense-q1_defense))

# 4. OUTLIERS
limiteInferior_hp = q1_health - (1.5 * (q3_health-q1_health))  
limiteSuperior_hp = q3_health + (1.5 * (q3_health-q1_health))

outliers_hp = []

for i in range(l):
    if health_points[i] < limiteInferior_hp or health_points[i] > limiteSuperior_hp:
        outliers_hp.append(health_points[i])

print("Los outliers de hp son:")
print(outliers_hp)

limiteInferior_lectura = q1_attack - (1.5 * (q3_attack-q1_attack))  
limiteSuperior_lectura = q3_attack + (1.5 * (q3_attack-q1_attack))

print("Los outliers de ataque son:")
outliers_attack = []

for i in range(l):
    if attack_rating[i] < limiteInferior_lectura or attack_rating[i] > limiteSuperior_lectura:
        outliers_attack.append(attack_rating[i])

print(outliers_attack)

print("Los outliers de defensa son:")

limiteInferior_escritura = q1_defense - (1.5 * (q3_defense-q1_defense))  
limiteSuperior_escritura = q3_defense + (1.5 * (q3_defense-q1_defense))

outliers_escritura = []

for i in range(l):
    if defense_rating[i] < limiteInferior_escritura or defense_rating[i] > limiteSuperior_escritura:
        outliers_escritura.append(defense_rating[i])

print(outliers_escritura)


