'''
crear generos

ejecutar:

python manage.py shell < datos/crear_generos.py
'''

from django.utils.text import slugify
import json
import os

from videojuegos.models import Genre, Videojuego

#lista de películas del json
if os.path.exists("videojuegos/juegos.csv"):
    videojueos = json.load(open("videojuegos/juegos.csv"))
else:
    videojuegos = json.load(open("videojuegos/juegos.csv"))

# recorre datos del json
for p in videojuegos:
    slug = slugify(f'{p["titulo"]}')
    videojuego = Videojuego.objects.get(slug=slug)  # recupera película por su slug
    generos = p.get('genre')  # géneros de la película (lista en el json)
    for genero in generos:
        genobj, created = Genre.objects.get_or_create(nombre=genero) # Recupera o crea el género si no existe
        videojuego.generos.add(genobj) # añade la relación m2m
