import requests
from decouple import config


class AMSService:
    def __init__(self):
        self.url = 'https://advanced-movie-search.p.rapidapi.com'
        self.headers = {
            f"X-RapidAPI-Key": config("RAPID_API_KEY"),
            f"X-RapidAPI-Host": config("RAPID_API_HOST")
        }

    def get_movie_id(self, movie_name):
        url = self.url + "/search/movie"
        querystring = {
            "query": movie_name
        }
        response = requests.get(url, headers=self.headers, params=querystring)
        results = response.json().get('results')
        return results[0].get('id')


if __name__ == "__main__":
    service = AMSService()
    print(service.get_movie_id("Interstellar"))
