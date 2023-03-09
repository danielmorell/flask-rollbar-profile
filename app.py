# Standard Library Imports
from pathlib import Path

# Package Imports
from flask import Flask
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception
from flask import Request, request
from werkzeug.middleware.profiler import ProfilerMiddleware

# Local Imports
from profiler import MyProfilerMiddleware

app = Flask(__name__)
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, profile_dir=str(Path(__file__).parent / 'pstat'))

rollbar.init(
    'fe02cec5448e49b9841f57905dbda24f',
    'production',
    root=str(Path(__file__).parent),
    allow_logging_basic_config=False,
    handler='agent',
    **{'agent.log_file': str(Path(__file__).parent / 'payload' / 'log.rollbar')}
)

got_request_exception.connect(rollbar.contrib.flask.report_exception, app)


class CustomRequest(Request):
    @property
    def rollbar_person(self):
        return {'id': '123', 'username': 'test', 'email': 'test@example.com'}


app.request_class = CustomRequest


@app.route("/", methods=['GET', 'POST'])
def index():
    print('here')
    app_and_things = [app, 'foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'garply', 'waldo', 'fred', 'plugh',
                      'xyzzy', 'thud']
    print(id(app_and_things))

    sub_func(app=app_and_things, extra={'request': request})
    return "<h1>Hello, World!</h1>"


@app.route("/favicon.ico")
def favicon():
    return "favicon"


def sub_func(**kwargs):
    a = kwargs['app']
    print(id(a))

    a_id = id(a)

    app_id = id(app)
    bar = 'im a bar'
    do_foo(kwargs)
