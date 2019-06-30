import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

#打开url文件
csvurl = pd.read_csv('../url.csv')
urls = csvurl['url']
head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

#设置cookie
cookietxt = 'bid=D41fqW3H5VM; _vwo_uuid_v2=D90879F06FB05E0FFBBE32151E0F37130|a3596255904259e36d1d87b069e05f40; gr_user_id=42418a56-407c-4bf6-9113-18d89a557eb5; ll="108297"; ps=y; viewed="3639345_1082154_30423376"; __yadk_uid=QAKnWEeeGOgk3Bz59RrWijEPRBXLunu4; __gads=ID=a334a7a90bd05d9d:T=1559526042:S=ALNI_MZ4pT3iTWmZqjAbqZzBX-YxQ9m61A; push_noty_num=0; push_doumail_num=0; douban-fav-remind=1; __utmc=30149280; __utmc=223695111; trc_cookie_storage=taboola%2520global%253Auser-id%3Da68c9abe-1ec4-42c4-8c1e-0e2b30fce007-tuct3c17a89; dbcl2="136984130:3l2pcLeScVI"; ck=j68C; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1561439495%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fredir%3Dhttps%253A%252F%252Fm.douban.com%252Fmovie%252Fsubject%252F1292052%252F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1715913790.1558929441.1561433279.1561439495.20; __utmb=30149280.0.10.1561439495; __utmz=30149280.1561439495.20.6.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utma=223695111.1875081626.1559525882.1561433279.1561439495.16; __utmb=223695111.0.10.1561439495; __utmz=223695111.1561439495.16.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; _pk_id.100001.4cf6=6f12b3bafef8beee.1559525882.16.1561440810.1561435168.'
cookie = {}
for line in cookietxt.split(';'):
    name,value = line.strip().split('=',1)
    cookie[name] = value

results = []
i=0
for url in urls:
    res = requests.get(url, head, cookies=cookie)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    #去掉html标签
    reg = re.compile('<[^>]*>')

    film = soup.find_all('h1')[0].find_all('span', property='v:itemreviewed')[0]

    film = reg.sub('',str(film)).replace('\n','')


    x = soup.find_all('div', id='info')[0]

    director = x.find_all('span')[0].find_all('span', class_='attrs')[0]
    director = reg.sub('',str(director)).replace('\n','')

    #因为actor有为空的
    try:
        actor = x.find_all('span', class_='actor')[0].find_all('span', class_='attrs')[0]
    except BaseException:
        actor = ''
    else:
        actor = reg.sub('', str(actor)).replace('\n', '')

    type = x.find_all('span', property='v:genre')
    type = reg.sub('',str(type)).replace('\n','')


    result = [film, director, actor, type]
    results.append(result)
    i += 1
    print('第%d条提取成功' % i)

#导入到csv
print('导入到csv.....')
df = pd.DataFrame(data=results, columns=['电影名称', '导演', '演员', '类型'])
df.to_csv('douban.csv', index=False, encoding='utf-8_sig')
print('导入到csv成功！')





