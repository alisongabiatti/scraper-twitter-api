from flask import Flask, request, jsonify
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Elastic 
from elasticapm.contrib.flask import ElasticAPM
from elasticapm.handlers.logging import LoggingHandler

# Prometheus exporter
from prometheus_client import make_wsgi_app
from flask_prometheus_metrics import register_metrics

# Werkzeug
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

apm = ElasticAPM(app, server_url=app.config['APM_URL'], service_name='crawler', secret_token='d910fe18cd0fde99ee282685cc7046e14a8491df474b85c8', logging=False )

from app import routes, models
# Prometheus metrics
# Definindo versão da app e environment
register_metrics(app, app_version="v0.1.2", app_config="local")
# WSGI de métricas no app
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})


if __name__ == '__main__':
    # app.run(debug=True)
    run_simple(hostname="0.0.0.0", port=5000, application=dispatcher)

