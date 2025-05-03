import os
from binance.client import Client
from flask import Flask

app = Flask(__name__)

# Configurar as chaves da API
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')

client = Client(api_key, api_secret)

@app.route('/')
def home():
    info = client.get_account()
    return f"Conectado com sucesso! Saldo total: {info['balances']}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
