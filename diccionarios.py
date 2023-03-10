planet = {
    'name' : 'Mars' ,
    'moons' : 2
}

print( f'{planet["name"]} has {planet["moons"]} moon(s)')

#diccionario dentro de otro diccionario
planet['circunference_km'] = {
    'polar' : 6752,
    'equatorial' : 6792
}

print(f'{planet["name"]} has a polar circunference of {planet["circunference_km"] ["equatorial"]} ')

#programacion dinamica
