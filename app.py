from flask import Flask, jsonify, request
from models.personaje import Personaje

app = Flask(__name__)

lista_personajes = []


@app.route('/personajes', methods=['GET'])
def obtener_personajes():
    personajes_dict = [p.to_dict() for p in lista_personajes]
    return jsonify(personajes_dict)


@app.route('/personajes', methods=['POST'])
def crear_personaje():
    datos = request.get_json()
    
    nombre = datos.get('nombre')
    clase = datos.get('clase')
    
    nuevo_heroe = Personaje(nombre, clase)
    lista_personajes.append(nuevo_heroe)
    
    return jsonify({
        "mensaje": "Personaje creado con éxito",
        "personaje": nuevo_heroe.to_dict()
    }), 201


if __name__ == '__main__':
    app.run(debug=True)