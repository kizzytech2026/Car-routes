
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'


@app.route('/<model>')
def model(model):
    if model == 'Crossroads':
        return 'Flatiron Crossroads is in our fleet!'
    elif model == 'Beedle':
        return 'Flatiron Beedle is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'


if __name__ == '__main__':
    app.run(debug=True)
