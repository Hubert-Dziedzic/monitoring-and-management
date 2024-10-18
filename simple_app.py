from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest
import time

app = Flask(__name__)

# Metrics
REQUEST_COUNT = Counter('app_request_total', 'Total number of requests')
REQUEST_LATENCY= Histogram('app_request_latency_seconds', 'Request latency')


@app.route('/')
def hello_world():
    REQUEST_COUNT.inc()
    start_time = time.time()
    response = 'Hellow, World!'
    REQUEST_LATENCY.observe(time.time() - start_time)
    return response


# Endpoint prometheus
@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)