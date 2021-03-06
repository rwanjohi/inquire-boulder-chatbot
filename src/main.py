#!/bin/python3
print('Waking up...\n')

from BotServer import BotServer
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    This route at the home page renders the index.html template with blank
    variables.
    """
    return render_template('index.html', query='', answer='')


@app.route('/dialog', methods=['POST'])
def dialog():
    """
    This route uses the POST method to take user request and return the result
    of passing it to the BotServer similarity matching function.
    """
    return bot.bot_dialog(request)


if __name__ == '__main__':
    """
    Default Python entrypoint creates Botserver object and runs Flask app.
    """
    bot = BotServer('data/faq-text-separated.csv')

    app.run(host='0.0.0.0', port=8080, debug=False)
