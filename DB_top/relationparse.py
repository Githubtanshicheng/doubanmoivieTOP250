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

    filmID = df_film['index:ID'].loc[df_film['film'] == film_name].values[0]

    for dir in directorList:
        directorID = df_director['index:ID'].loc[df_director['director']==dir].values[0]
        director_film = [directorID, filmID, '导演', '导演']
        director_films.append(director_film)


    for act in actorList:
        actorID = df_actor['index:ID'].loc[df_actor['actor']==act].values[0]
        actor_film = [actorID, filmID, '出演', '出演']
        actor_films.append(actor_film)

    for dir in directorList:
        directorID = df_director['index:ID'].loc[df_director['director']==dir].values[0]
        for act in actorList:
            actorID = df_actor['index:ID'].loc[df_actor['actor']==act].values[0]
            director_actor = [directorID, actorID, '合作', '合作']
            director_actors.append(director_actor)

    for ty in typeList:
        typeID = df_type['index:ID'].loc[df_type['type']==ty].values[0]
        film_type = [filmID, typeID, '类型', '类型']
        film_types.append(film_type)



df_director_film = pd.DataFrame(data=director_films, columns=[':START_ID', ':END_ID', 'relation', ':TYPE'])
df_director_film.to_csv('relation_director_film.csv', index=False, encoding='utf-8_sig')
print('relation_director_film.csv')


df_actor_film = pd.DataFrame(data=actor_films, columns=[':START_ID', ':END_ID', 'relation', ':TYPE'])
df_actor_film.to_csv('relation_actor_film.csv', index=False, encoding='utf-8_sig')
print('relation_actor_film.csv')


df_director_actor = pd.DataFrame(data=director_actors, columns=[':START_ID', ':END_ID', 'relation', ':TYPE'])
df_director_actor.to_csv('relation_director_actor.csv', index=False, encoding='utf-8_sig')
print('relation_director_actor.csv')


df_film_type = pd.DataFrame(data=film_types, columns=[':START_ID', ':END_ID', 'relation', ':TYPE'])
df_film_type.to_csv('relation_film_type.csv', index=False, encoding='utf-8_sig')
print('relation_film_type.csv')
