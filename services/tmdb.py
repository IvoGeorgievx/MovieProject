import requests
from decouple import config
from werkzeug.exceptions import BadRequest


class TMDBService:

    def __init__(self):
        self.url = 'https://api.themoviedb.org/3'
        self.headers = {
            "Authorization": f'Bearer {config("TMDB_KEY")}',
            "Content-Type": "application/json;charset=utf-8",
        }

    def get_movie_id(self, query):
        url = self.url + f'/search/movie?api_key={config("TMDB_KEY")}&language=en-US&query={query}&page=1&include_adult=false'
        try:
            response = requests.get(url)
            result = response.json()['results']
            movie_id = result[0]["id"]
            return movie_id
        except Exception as e:
            raise BadRequest("There is no such movie in our database.")

    def get_movie_details(self, movie_id):
        url = self.url + f'/movie/{movie_id}?api_key={config("TMDB_KEY")}&language=en-US'
        response = requests.get(url)
        return response.json()

    def get_upcoming_movies(self):
        url = self.url + f'/movie/upcoming?api_key={config("TMDB_KEY")}&language=en-US&page=1'
        response = requests.get(url)
        return response.json()
