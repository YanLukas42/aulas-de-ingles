from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Configure seu token do Mercado Pago aqui
MERCADO_PAGO_ACCESS_TOKEN = os.getenv('MP_ACCESS_TOKEN', 'SEU_TOKEN_AQUI')

@app.route('/create_preference', methods=['POST'])
def create_preference():
    data = request.json
    preference = {
        "items": [
            {
                "title": data.get("title", "Aula de Inglês"),
                "quantity": 1,
                "unit_price": float(data.get("price", 100.0))
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {MERCADO_PAGO_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(
        "https://api.mercadopago.com/checkout/preferences",
        json=preference,
        headers=headers
    )
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
