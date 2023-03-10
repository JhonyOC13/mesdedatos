first_planet_input = input('Inserte la distancia del sol al primer planeta en km')
second_planet_input = input('inserte la distancia del sol al segundo planeta en km')

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distance_km = first_planet - second_planet
print(abs(distance_km))