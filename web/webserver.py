from flask import Flask
from flask import render_template
from model.currentPortfolioBased import getCurrentPositions
app=Flask('CryptoServer')


@app.route("/")
def hello():
    return "hello Crypto World"

@app.route('/index')
def serve_crypto_file():
    return render_template('index.html')


@app.route('/positions')
def serve_positions():
    postions=getCurrentPositions()

    return postions

app.run()

