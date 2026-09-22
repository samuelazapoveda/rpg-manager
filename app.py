from flask import Flask, jsonify, request, render_template, redirect
from models.personaje import Personaje
from services.personaje_service import validar_personaje

app = Flask(__name__)

lista_personajes = []

@app.route('/personajes', methods=['GET'])
def obtener_personajes():
    return render_template('personajes.html', lista_personajes=lista_personajes)


@app.route('/personajes', methods=['POST'])
def crear_personaje():
    nombre = request.form.get('nombre')
    clase = request.form.get('clase')
    nivel = request.form.get('nivel')
    vida = request.form.get('vida')

    nivel = int(nivel)
    vida = int (vida)

    if validar_personaje (nombre, clase, nivel, vida) == True:
        nuevo_heroe = Personaje(nombre, clase, nivel, vida)
        lista_personajes.append(nuevo_heroe)
        return redirect('/personajes')
    else:
      return render_template(
          'personajes.html',
          lista_personajes=lista_personajes,
          error='Datos del personaje inválidos',
        )
       

if __name__ == '__main__':
    app.run(debug=True)