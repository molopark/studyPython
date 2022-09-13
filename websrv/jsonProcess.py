import requests
import json
from Movie import Movie

def getMovie(page):
    url = "https://yts.am/api/v2/list_movies.json?sort_by=ratings&limit=20&page=1"

    response = requests.get(url=url)

    html = json.loads(response.text)
    
    data = html['data']
    
    movies = data['movies']

    list = []
    for i in movies:
        m = Movie(
            i['rating'],
            i['title'],
            i['synopsis'],
            i['medium_cover_image'],
            i['url']            
        )
        list.append(m)
    return list
