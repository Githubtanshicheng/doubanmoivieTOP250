import pandas as pd
import re

df = pd.read_csv('douban.csv', encoding='utf-8')
df_film = pd.read_csv('film.csv', encoding='utf-8')
df_director = pd.read_csv('director.csv', encoding='utf-8')
df_actor = pd.read_csv('actor.csv', encoding='utf-8')
df_type = pd.read_csv('type.csv', encoding='utf-8')




director_films, actor_films, director_actors, film_types = [], [], [], []

for index, row in df.iterrows():

    film_name = row['电影名称']
    director = row['导演']
    actor = row['演员']
    type = row['类型']
    typeList, directorList, actorList = [], [], []

    direList = director.split('/')
    for d in direList:
        d = d.strip()
        directorList.append(d)
    actList = actor.split('/')
    for d in actList:
        d = d.strip()
        actorList.append(d)

    reg = re.compile(r'\[|\]')
    type = reg.sub('', type)
    type = re.split(r'[\s\,]+', type)
    typeList = []
    typeList.extend(type)

    print(typeList)
    print(directorList)
    print(actorList)