from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})  # Ajusta el origen según la configuración de tu aplicación React

def procesar_mensaje(mensaje):
    if 'horario' in mensaje.lower():
        return 'Nuestro horario de atención es de lunes a viernes de 9 AM a 6 PM.'

    if 'ubicacion' in mensaje.lower():
        return 'Estamos ubicados en Tecamac, EDO.MEX.'

    return 'Gracias por contactarnos. ¿En qué más puedo ayudarte?'

@app.route('/api/message', methods=['POST'])
def get_message():
    data = request.get_json()
    message = data['message']

    reply = procesar_mensaje(message)

    response = {'reply': reply}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)