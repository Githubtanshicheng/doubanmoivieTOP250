import pandas as pd
import re

df = pd.read_csv('douban.csv', encoding='utf-8')

df_film = df['电影名称']
df_director = df['导演']
df_actor = df['演员']
df_type = df['类型']

filmID, directorID, actorID, typeID = [], [], [], []

filmList = list(df_film)
film_cnt = len(filmList)
df_film_name = pd.DataFrame(data=filmList, columns=['filmName'])

directorList = []
for dir in df_director:
    dirList = dir.split('/')
    for x in dirList:
        new = x.strip()
        directorList.append(new)
directorList = list(set(directorList))
director_cnt = len(directorList)
df_director_name = pd.DataFrame(data=directorList, columns=['directorName'])

actorList = []
for act in df_actor:
    actList = act.split('/')
    for x in actList:
        new = x.strip()
        actorList.append(new)
actorList = list(set(actorList))
actor_cnt = len(actorList)
df_actor_name = pd.DataFrame(data=actorList, columns=['actorName'])

typeList = []
for ty in df_type:
    reg = re.compile(r'\[|\]')
    ty = reg.sub('', ty)
    ty = re.split(r'[\s\,]+', ty)
    typeList.extend(ty)
typeList = list(set(typeList))
type_cnt = len(typeList)
df_type_name = pd.DataFrame(data=typeList, columns=['typeName'])


for i in range(10001, 10001 + film_cnt):
    filmID.append(i)
df_film_ID = pd.DataFrame(data=filmID, columns=['filmID'])

for i in range(20001, 20001 + director_cnt):
    directorID.append(i)
df_director_ID = pd.DataFrame(data=directorID, columns=['directorID'])

for i in range(30001, 30001 + actor_cnt):
    actorID.append(i)
df_actor_ID = pd.DataFrame(data=actorID, columns=['actorID'])

for i in range(40001, 40001 + type_cnt):
    typeID.append(i)
df_type_ID = pd.DataFrame(data=typeID, columns=['typeID'])



film = pd.concat([df_film_ID,df_film_name],axis=1)
film['label'] = '电影'

director = pd.concat([df_director_ID,df_director_name], axis=1)
director['label'] = '导演'

actor = pd.concat([df_actor_ID, df_actor_name], axis=1)
actor['label'] = '演员'

type = pd.concat([df_type_ID, df_type_name], axis=1)
type['label'] = '类型'



film.columns = ['index:ID', 'film', ':LABEL']
film.to_csv('film.csv', index = False, encoding='utf-8_sig')
print('电影节点导出成功')


director.columns = ['index:ID', 'director', ':LABEL']
director.to_csv('director.csv', index = False, encoding='utf-8_sig')
print('director节点导出成功')

actor.columns = ['index:ID', 'actor', ':LABEL']
actor.to_csv('actor.csv', index = False, encoding='utf-8_sig')
print('actor节点导出成功')

type.columns = ['index:ID', 'type', ':LABEL']
type.to_csv('type.csv', index = False, encoding='utf-8_sig')
print('type节点导出成功')