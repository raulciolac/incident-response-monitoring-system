from flask import Flask, Response
import random
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUESTS = Counter('requests_total', 'Total requests')
ERRORS = Counter('errors_total', 'Total errors')

@app.route("/")
def home():
    REQUESTS.inc()
    if random.random() < 0.3:
        ERRORS.inc()
        return "Error!", 500
    return "OK"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

app.run(host="0.0.0.0", port=5000)
