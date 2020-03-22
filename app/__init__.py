from flask import Flask, request, jsonify
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Elastic 
from elasticapm.contrib.flask import ElasticAPM
from elasticapm.handlers.logging import LoggingHandler
import redis

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
redis_host = redis.Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
# apm = ElasticAPM(app, server_url=app.config['APM_URL'], service_name='crawler', secret_token='d910fe18cd0fde99ee282685cc7046e14a8491df474b85c8', logging=False )

from app import routes, models

if __name__ == '__main__':
    app.run(debug=True)
