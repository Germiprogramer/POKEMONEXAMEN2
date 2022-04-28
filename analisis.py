import pandas as pd

notas = pd.read_csv("pokemon_stats (1).csv", header=0)

#CREAMOS EL DICCIONARIO A PARTIR DE LOS DATOS DEL DATASET

health_points = list(notas["HP"])
attack_rating = list(notas["Attack"])
defense_rating = list(notas["Defense"])
SpAttack = list(notas["SpAttack"])
SpDefense = list(notas["SpDefense"])
speed = list(notas["Speed"])
total = list(notas["Total"])

l = len(health_points)

#1. Cantidad de observaciones

print("- CANTIDAD DE OBSERVACIONES -")
print("Cantidad de observaciones = {}".format(l))

#2. Valores mínimos y máximos

print("- VALORES MÁXIMOS -")
max_value = None

for num in health_points:
    if (max_value is None or num > max_value):
        max_value = num

print('Mejor HP:', max_value)

for num in attack_rating:
    if (max_value is None or num > max_value):
        max_value = num

print('Mejor Ataque:', max_value)

for num in defense_rating:
    if (max_value is None or num > max_value):
        max_value = num

print("Mejor Defensa:" , max_value)

for num in SpAttack:
    if (max_value is None or num > max_value):
        max_value = num

print('Mejor SpAtaque:', max_value)

for num in SpDefense:
    if (max_value is None or num > max_value):
        max_value = num

print('Mejor SpDefensa:', max_value)

for num in speed:
    if (max_value is None or num > max_value):
        max_value = num

print('Mejor nota velocidad:', max_value)

print(" -VALORES MÍNIMOS- ")

min_value = None

for num in health_points:
    if (min_value is None or num > min_value):
        min_value = num

print('Mejor HP:', min_value)

for num in attack_rating:
    if (min_value is None or num > min_value):
        min_value = num

print('Mejor Ataque:', max_value)

for num in defense_rating:
    if (min_value is None or num > min_value):
        min_value = num

print("Mejor Defensa:" , max_value)

for num in SpAttack:
    if (min_value is None or num > min_value):
        min_value = num

print('Mejor SpAtaque:', min_value)

for num in SpDefense:
    if (min_value is None or num > min_value):
        min_value = num

print('Mejor SpDefensa:', min_value)

for num in speed:
    if (min_value is None or num > min_value):
        min_value = num

# 3. MEDIA ARITMÉTICA
#a partir de aqui se analizaran solo HP, attack, defense

print("- NOTAS MEDIAS -")
suma_hp = sum(health_points)
media_hp = suma_hp / l
print("La media de hp es {}".format(media_hp))

print("- NOTAS MEDIAS -")
suma_attack = sum(attack_rating)
media_attack = suma_attack / l
print("La media de ataque es {}".format(media_attack))

suma_defensa = sum(defense_rating)
media_defensa = suma_defensa / l
print("La media de defensa es {}".format(media_defensa))

# 4. MEDIANA
print("- MEDIANA -")
valor_medio = int(l/2)

mediana_health = (health_points[valor_medio] + health_points[valor_medio + 1])/2
print("La mediana de las notas de mates es: {}".format(mediana_health))

mediana_attack = (attack_rating[valor_medio] + attack_rating[valor_medio + 1])/2
print("La mediana de las notas de lectura es: {}".format(mediana_attack))

mediana_defense = (defense_rating[valor_medio] + defense_rating[valor_medio + 1])/2
print("La mediana de las notas de escritura  es: {}".format(mediana_defense))

#