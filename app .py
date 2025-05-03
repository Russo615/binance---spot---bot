from flask import Flask, request, jsonify
from binance.client import Client
import os

app = Flask(__name__)

# Pegando as variáveis de ambiente (API key e secret)
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')
client = Client(api_key, api_secret)

@app.route('/')
def home():
    return 'Binance Spot Bot está rodando!'

@app.route('/preco/<symbol>', methods=['GET'])
def preco(symbol):
    try:
        ticker = client.get_symbol_ticker(symbol=symbol.upper())
        return jsonify(ticker)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/comprar', methods=['POST'])
def comprar():
    data = request.json
    symbol = data['symbol']
    quantity = data['quantity']
    try:
        order = client.order_market_buy(symbol=symbol.upper(), quantity=quantity)
        return jsonify(order)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/vender', methods=['POST'])
def vender():
    data = request.json
    symbol = data['symbol']
    quantity = data['quantity']
    try:
        order = client.order_market_sell(symbol=symbol.upper(), quantity=quantity)
        return jsonify(order)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
