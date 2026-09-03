from flask import Flask, jsonify, request, render_template, redirect
from models.personaje import Personaje

app = Flask(__name__)

lista_personajes = []


@app.route('/personajes', methods=['GET'])
def obtener_personajes():
    return render_template('personajes.html', lista_personajes=lista_personajes)


@app.route('/personajes', methods=['POST'])
def crear_personaje():
    nombre = request.form.get('nombre')
    clase = request.form.get('clase')

    nuevo_heroe = Personaje(nombre, clase)
    lista_personajes.append(nuevo_heroe)

    return redirect('/personajes')


if __name__ == '__main__':
    app.run(debug=True)