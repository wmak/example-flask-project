import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="http://bf78a364097540c4b535c73bf598b9fb@localhost:8000/1",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0
