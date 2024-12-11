from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Rutas de la API
@app.route('/api/hello', methods=['GET'])
def hello():
    """Endpoint que devuelve un saludo.
    ---
    responses:
      200:
        description: Un mensaje de saludo
        examples:
          application/json: { "message": "Hola, mundo!" }
    """
    return jsonify({"message": "Hola, mundo!"})

# Configuración de Swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
