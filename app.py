from flask import Flask, render_template, request, jsonify, redirect, url_for
import database as dbase
from materiales import Material

app = Flask(__name__)
db = dbase.dbConnection()

# Rutas de la aplicación
@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/materiales')
def materiales():
    materiales = db['materiales']
    materialesRecibidos = materiales.find()

    return render_template('materiales.html', materials=materialesRecibidos)

# Método POST
@app.route('/materiales', methods=['POST'])
def addMaterial():
    materiales = db['materiales']
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    resistencia = request.form['resistencia']
    corrosion = request.form['corrosion']
    precio_kg = request.form['precio_kg']

    if nombre and descripcion and resistencia and corrosion and precio_kg:
        material = Material(nombre, descripcion, resistencia, corrosion, precio_kg)
        materiales.insert_one(material.toDBCollection())
        return redirect(url_for('materiales'))
    else:
        return notFound()

# Método DELETE
@app.route('/delete/<string:material_name>')
def deleteMaterial(material_name):
    materiales = db['materiales']
    materiales.delete_one({'nombre': material_name})
    return redirect(url_for('materiales'))

# Método PUT
@app.route('/edit/<string:material_name>', methods=['POST'])
def editMaterial(material_name):
    materiales = db['materiales']
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    resistencia = request.form['resistencia']
    corrosion = request.form['corrosion']
    precio_kg = request.form['precio_kg']

    if nombre and descripcion and resistencia and corrosion and precio_kg:
        materiales.update_one({'nombre': material_name}, {'$set': {'nombre': nombre, 'descripcion': descripcion, 'resistencia': resistencia, 'corrosion': corrosion, 'precio_kg': precio_kg}})
        return redirect(url_for('materiales'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 not found'
    }

    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=4000)
