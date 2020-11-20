from os import execlp
from flask import Flask, jsonify, request
import mysql.connector


"""
To do:
Modify data base to have spaces for courses
# get para oferta (ver que show ya que son muchos campos y no simpre estaran llenos)
# post para agendar materias update materiaalumno, materia
"""

"""
DONE:
# login del usuario (Consultar que exista y dar acceso) check
# Horario del usario check
# circulares check
"""

app = Flask(__name__)
db = mysql.connector.connect (
    user = "manuel", password = "taquero", database = "theamUdg")


cursor = db.cursor()


def login(data_base, cod, password):
    cursor = data_base.cursor()
    query = "SELECT COUNT(*) FROM usuario WHERE codigo = %s AND contrasenia = %s"
    cursor.execute(query, (cod,password))
    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False

def getUserData(dataBase, cod):
    cursor = dataBase.cursor()
    query = "SELECT codigo, nombre, sNombres, apellidoP, apellidoM, carrera, cicloInicio, activo FROM usuario WHERE codigo = %s"
    cursor.execute(query,(cod,))
    usuario = {}
    for row in cursor.fetchall():
        usuario = {
            'codigo' : row[0],
            'nombre' : row[1],
            'sNombre' : row[2],
            'apellidoP' : row[3],
            'apellidoM' : row[4],
            'carrera' : row[5],
            'cicloInicio' : row[6],
            'activo' : row[7]
        }
    return usuario

def getCourses(dataBase, code):
    cursor =  dataBase.cursor()
    query = 'SELECT claseNrc FROM materiaalumno WHERE codigoAl = %s'
    cursor.execute(query, (code,))
    nrc = []
    for row in cursor.fetchall():
        a = row[0]
        nrc.append(a)
    courses = []
    for course in nrc:
        queryCour = 'SELECT claseNrc, clave, nombre, dias, seccion, edificio, aula, profesor FROM materia WHERE claseNrc = %s'
        cursor.execute(queryCour, (course,))
        row = cursor.fetchone()
        if row:
            a = {
                'NRC' : row[0],
                'Clave' : row[1],
                'Nombre' : row[2],
                'Dias' : row[3],
                'Seccion' : row[4],
                'Edificio' : row[5],
                'Aula' : row[6],
                'Profesor' : row[7]
            }
            courses.append(a)
    return courses


@app.route("/login", methods = ['GET', 'POST'])
def accessUser ():
    if request.method == 'GET':
        codigo = request.args.get('codigo')
        passw = request.args.get('contrasenia')
        if (login(db,codigo,passw)):
            return (jsonify(getUserData(db,codigo)))
        else:
           (jsonify({'code':'Dont exist user'}))
    elif request.method == 'POST':
        pass
    return (jsonify({'code':'Error'}))

@app.route('/circulares')
@app.route('/circulares/<int:cant>')
def circulares(cant = 4):
    query = 'SELECT contenido, numero, fecha FROM circulares ORDER BY numero DESC LIMIT %s'
    cursor.execute(query, (cant,))
    circulares = []
    for row in cursor.fetchall():
        a = {
            'contenido' : row[0],
            'numero' : row[1],
            'fecha' : row[2]
        }
        circulares.append(a)
    return jsonify(circulares)

@app.route('/horario')
@app.route('/horario/<int:cod>')
def userCourses(cod = None):
    if not cod:
        return jsonify({'Code':'Missing user code'})
    elif cod:
        return jsonify(getCourses(db,cod))
    else:
        return jsonify({'Code':'Error'})

def get_cupos_dis(nrc):
    if not nrc:
        raise Exception("invalid nrc")
    query = "SELECT "
    cursor


if __name__ == '__main__':
    app.run (debug = True)
    