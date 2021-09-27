from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

from config.db import mysql

import models.paises
paises = models.paises

app= Flask(__name__)
CORS(app)
query = MySQL(mysql(app)) 


@app.route('/')
def index():
    try:
        data = paises.listado(query)
        listado = []
        for i in data:
            fila = {'id': i[0], 'nombre': i[1], 'continente': i[2]}
            listado.append(fila)
        return jsonify({'data': listado})
    except Exception as e:
        return jsonify(e)

@app.route('/<int:id>', methods=['GET'])
def search(id):
    try:
        data = paises.listadoID(query, id)
        if data != None:
            fila = {'id': data[0], 'nombre': data[1], 'continente': data[2]}
            return jsonify({'data': fila})
        else:
            return jsonify({'message': 'No existe dato con ese ID'})
    except Exception as e:
        return jsonify(e)

@app.route('/', methods=['POST'])
def post():
    try:
        json = request.json
        if request.method == 'POST':
            nombre = json['nombre']
            continente = json['continente']
        if paises.unicoNombreG(query,nombre):
            return jsonify({'nombre': 'Nombre ya esta registrado en la base de datos'})
        else:
            data = paises.guardarDatos(query,nombre,continente)
            if data[0]=='nombre':
                return jsonify({'nombre': data[1]})
            else:
                return jsonify({'data': data})
    except Exception as e:
        return jsonify(e)

@app.route('/<int:id>', methods=['PUT'])
def put(id):
    try:
        json = request.json
        if request.method == 'PUT':
            nombre = json['nombre']
            continente = json['continente']
        fila = paises.unicoNombreU(query,nombre,id)
        if fila >= 2:
            return jsonify({'nombre': 'Nombre ya esta registrado en la base de datos'})
        else:
            data = paises.actualizarDatos(query,nombre,continente,id)
            if data[0]=='nombre':
                return jsonify({'nombre': data[1]})
            else:
                return jsonify({'data': data})
    except Exception as e:
        return jsonify(e)

@app.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        fila = paises.listadoID(query, id)
        if fila != None:
            data = paises.eliminarDatos(query,id)
            return jsonify({'data': data})
        else:
            return jsonify({'message': 'No existe dato con ese ID'})
    except Exception as e:
        return jsonify(e)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
