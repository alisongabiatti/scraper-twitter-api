from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import sqlalchemy
from app.utils import auth_token, search
from app.models import Tweets
from app import app, db
import sys
import time


# Home
@app.route('/')
@app.route('/index')
def index():
    return render_template('interface.html')

# Realiza a busca de todas as hashtags e popula o banco
@app.route('/populate')
def searchht():
    try:
        populate = [
            'apifirst',
            'openbanking',
            'devops',
            'cloudfirst',
            'microservices ',
            'apigateway',
            'oauth',
            'swagger',
            'raml',
            'openapis',
        ]
        for hashtag in populate:
            search(hashtag)

        return jsonify({'status': 'success'})
    except:
        e = sys.exc_info()[0]
        return jsonify({'status': '{}'.format(e)})


# Exibe os maiores seguidores
@app.route('/top')
def tops():
    tops = [ {'name': tweet.name, 'followers': tweet.followers} for tweet in db.session.query(Tweets.name, Tweets.followers).distinct().order_by(Tweets.followers.desc()).limit(5)]
    return jsonify(tops)

# Agrupada por hora
@app.route('/tweets')
def tweets():
    tweets = [ {'timestamp': tweet.date, 'tweet': tweet.text}  for tweet in db.session.query(Tweets.date, Tweets.text).distinct().order_by(Tweets.date.desc())]
    return jsonify(tweets)

# Total de publicacao por hashtag em cada pais ou região.
@app.route('/total')
def total():
    hashtags = [ {'count': tweet.count_id, 'hashtag': tweet.hashtag, 'lang': tweet.lang, 'location': tweet.location } for tweet in db.session.query(Tweets.hashtag, Tweets.lang, Tweets.location, sqlalchemy.func.count(Tweets.id).label('count_id')).group_by(Tweets.hashtag, Tweets.lang, Tweets.location)]
    return jsonify(hashtags)