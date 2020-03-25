from app import dispatcher
from werkzeug.serving import run_simple
run_simple(hostname="0.0.0.0", port=5000, application=dispatcher)