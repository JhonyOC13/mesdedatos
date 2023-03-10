planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets.append ("Pluto")

print("There are ", len(planets), "planets")
print(planets[-1])

#Listas con numeros 
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
user_planet = input("Please enter the name of the planet (with a capital letter to start)")

planet_index = planets.index(user_planet)

print("Estos son los planetas que están más cerca que " + user_planet)
print(planets[0:planet_index])
