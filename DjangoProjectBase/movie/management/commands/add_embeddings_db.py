from django.core.management.base import BaseCommand
from movie.models import Movie
import json
import os
import numpy as np

class Command(BaseCommand):
    help = 'Modify path of images'

    def handle(self, *args, **kwargs):
        # Ajustar la ruta relativa al archivo JSON
        json_file_path = 'movie/movie_descriptions_embeddings.json'
        
        # Cargar datos desde el archivo JSON
        with open(json_file_path, 'r') as file:
            movies = json.load(file)       

        # Iterar sobre las películas y actualizar los embeddings en la base de datos
        for movie in movies:
            emb = movie['embedding']
            emb_binary = np.array(emb).tobytes()
            item = Movie.objects.filter(title=movie['title']).first()
            item.emb = emb_binary
            item.save()
        
        self.stdout.write(self.style.SUCCESS(f'Successfully updated item embeddings'))
