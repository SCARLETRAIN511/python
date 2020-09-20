import requests
import json


def get_movies_from_tastedive(title):
    endpoint = 'https://tastedive.com/api/similar'
    param = {}
    param['q'] = title
    param['limit'] = 5
    param['type'] = 'movies'

    taste_dive_resp = requests.get(endpoint, params=param)
    return json.loads(taste_dive_resp.text)
    
def extract_movie_titles(data):
    return [i['Name'] for i in data['Similar']['Results']]

def get_related_titles(movie_lst):
    lst=[]
    for i in movie_lst:
        lst.extend(extract_movie_titles(get_movies_from_tastedive(i)))
    return list(set(lst))

def get_movie_data(title):
    base_url="http://www.omdbapi.com/"
    param={}
    param['t']=title
    param['r']='json'
    omdb_resp=requests.get(base_url,params=param)
    return json.loads(omdb_resp.text)

def get_movie_rating(dic):
    ranking=dic["Ratings"]
    point=0
    for i in ranking:
        if i['Source'] == 'Rotten Tomatoes':
            point=int(i['Value'][:-1])
    return point
def get_sorted_recommendations(movie_lst):
    dict = {}
    for title in get_related_titles(movie_lst):
        dict[title] = get_movie_rating(get_movie_data(title))
    return [i[0] for i in sorted(dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]
print(get_sorted_recommendations('Black Panther'))