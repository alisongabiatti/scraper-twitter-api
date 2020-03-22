from app.models import Tweets
from app.config import Config
from datetime import datetime
from app import db,app
import time, base64, requests


base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)


def auth_token():
    key_secret = '{}:{}'.format(Config.CLIENT_KEY, Config.CLIENT_SECRET).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    auth_data = {
        'grant_type': 'client_credentials'
    }

    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

    return auth_resp.json()['access_token']


# Busca a hashtag
def search(querystring):
    search_headers = {
        'Authorization': 'Bearer {}'.format(auth_token())    
    }

    search_params = {
        'q': '#{} -filter:retweets -filter:replies'.format(querystring),
        'tweet_mode': 'extended',
        'count': 100
    }
    search_url = '{}1.1/search/tweets.json'.format(base_url)
    search_resp = requests.get(search_url, headers=search_headers, params=search_params)
    result = [ 
        {   'hashtag': '#{}'.format(querystring),
            'name' : tweet['user']['screen_name'],
            'followers' : tweet['user']['followers_count'],
            'date': datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S %z %Y'),
            'text': str(tweet['full_text']),
            'location': tweet['user']['location'],
            'lang': tweet['user']['lang'],
            'update_time': datetime.now()
            } for tweet in search_resp.json()['statuses'] ]

    result.sort(key=lambda x:x['date'])
    # Novas entradas
    tweets_novos = result.copy()
    # itens atuais
    tweets_armazenados = [items.__dict__ for items in Tweets.query.filter(Tweets.hashtag == '#{}'.format(querystring))]
    # Mapeando as entradas
    banco = [] 
    app.logger.info('Total result inside banco array: {}'.format(len(result)))

    # Checa quantidade de itens armazenados para update
    if len(tweets_novos) < len(tweets_armazenados):
        range_update = len(tweets_novos)
    else:
        range_update = len(tweets_armazenados)

    # Atualiza os existenstes
    for item in range(range_update):
        item_novo = tweets_novos.pop()
        item_id = tweets_armazenados[item]['id']
        app.logger.info('id:{} update_time:{}'.format(item_id, item_novo['update_time']))
        Tweets.query.filter_by(id=item_id).update(item_novo)
        db.session.commit()
        banco.insert(0, item_novo)
    # Adiciona os novos
    for tweets in range(len(tweets_novos)):
        item_novo = tweets_novos.pop()
        banco.insert(0, item_novo)
        t = Tweets(**item_novo)
        db.session.add(t)
        db.session.commit()

    app.logger.info('Total result fim: {}'.format(len(result)))
    app.logger.info('Total de intens adicionados/atualizados: {}'.format(len(banco)))
    return result