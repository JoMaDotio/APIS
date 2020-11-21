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
    user = "userName", password = "password", database = "theamUdg")

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
    query = 'SELECT claseNrc FROM materiaAlumno WHERE codigoAl = %s'
    cursor.execute(query, (code,))
    nrc = []
    for row in cursor.fetchall():
        a = row[0]
        nrc.append(a)
    courses = []
    for course in nrc:
        queryCour = 'SELECT * FROM materia WHERE claseNrc = %s'
        cursor.execute(queryCour, (course,))
        row = cursor.fetchone()
        if row:
            a = {
                'NRC' : row[0],
                'Clave' : row[1],
                'Nombre' : row[2],
                'Dias' : row[3],
                'Seccion' : row[4],
                'Cupos': row[5],
                'CuposDis': row[6],
                'Edificio' : row[7],
                'Aula' : row[8],
                'Profesor' : row[9]
            }
            courses.append(a)
    return courses

@app.route("/")
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

@app.route('/agenda')
def registrarMateriaAlumno(codigo=215476966, nrc=42268):
    if request.method == "GET":
        cupDis = get_cupos_dis(nrc)
        if (cupDis >= 0):
            cupDis = cupDis - 1
            query = "UPDATE materia SET cupDis=%s WHERE claseNRC=%s"
            print(query, (cupDis, nrc))
            cursor.execute(query, (cupDis, nrc))
            
            # se modifica tabla materiaAlumno
            query = "INSERT INTO materiaAlumno (codigoAl, claseNrc) VALUES (%s, %s)"
            cursor.execute(query, (codigo, nrc))
            
            return jsonify({"code": "ok"})
        # Si la materia ya cuenta con cupo negativo entonces se hay un error
        return jsonify({"code": "error"})

def get_cupos_dis(nrc):
    if not nrc:
        raise Exception("No NRC provided")
    query = "SELECT cupDis from materia WHERE claseNrc=%s"
    cursor.execute(query, (nrc,))
    for aux in cursor.fetchall():
        cupDis = aux[0]
    return cupDis

if __name__ == '__main__':
    app.run (debug = True)