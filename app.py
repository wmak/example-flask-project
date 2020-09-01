from __future__ import absolute_import
import sentry_sdk
import logging
import time
import datetime
import random
import math
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

logger = logging.getLogger(__name__)

sentry_sdk.init(
    dsn="http://3dccbba1a9fb42b98d916994e346438e@dev.getsentry.net:8000/9",
    environment="slow",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
)
start = datetime.datetime(2020, 8, 11, 18, 6, 56)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/query', methods=['POST'])
def query():
    1/0


@app.route('/just_noise2')
def just_noise2():
    with sentry_sdk.configure_scope() as scope:
        import time
        time.sleep(random.random())
        scope.user = {'id': random.randint(1,5), "email": random.choice([
            u"foos@example.\u4e86\0\0\0\0",
            u"bar@example.\u4e86\0\0\0\0",
        ])}
    return 'hi'

@app.route('/just_noise')
def just_noise():
    with sentry_sdk.configure_scope() as scope:
        import time
        time.sleep(random.random())
        scope.user = {'id': random.randint(1,5), "email": random.choice([
            u"foos@example.\u4e86\0\0\0\0",
            u"bar@example.\u4e86\0\0\0\0",
        ])}
    return 'hi'

@app.route('/one_step')
def one_step():
    with sentry_sdk.configure_scope() as scope:
        import time
        hour = 1 if (datetime.datetime.now() - start).total_seconds()/3600 > 6 else 0
        time.sleep(random.random() + hour)
        scope.user = {'id': random.randint(1,5), "email": random.choice([
            u"foos@example.\u4e86\0\0\0\0",
            u"bar@example.\u4e86\0\0\0\0",
        ])}
    return 'hi'

@app.route('/multiple_step')
def multiple_step():
    with sentry_sdk.configure_scope() as scope:
        import time
        hour = math.floor((datetime.datetime.now() - start).total_seconds()/7200.0)
        time.sleep(random.random() + hour)
        scope.user = {'id': random.randint(1,5), "email": random.choice([
            u"foos@example.\u4e86\0\0\0\0",
            u"bar@example.\u4e86\0\0\0\0",
        ])}
    return 'hi'

@app.route('/linear')
def linear():
    with sentry_sdk.configure_scope() as scope:
        import time
        hour = (datetime.datetime.now() - start).total_seconds()/7200.0
        time.sleep(random.random() + hour)
        scope.user = {'id': random.randint(1,5), "email": random.choice([
            u"foos@example.\u4e86\0\0\0\0",
            u"bar@example.\u4e86\0\0\0\0",
        ])}
    return 'hi'

@app.route('/spike')
def spike():
    with sentry_sdk.configure_scope() as scope:
        import time
        hour = 3 if datetime.datetime.now().hour == 7 else 0
        time.sleep(random.random() + hour)
        scope.user = {'id': random.randint(1,5), "email": random.choice([
            u"foos@example.\u4e86\0\0\0\0",
            u"bar@example.\u4e86\0\0\0\0",
        ])}
    return 'hi'


def trigger_inner_error():
    1 / 0
