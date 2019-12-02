import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="http://f003c07d43a347eb8f42eb93cf1e83e4@dev.getsentry.net:8000/8",
    environment="this environment",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0
