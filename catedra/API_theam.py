from flask import Flask, jsonify, request
import mysql.connector


"""
To do:
"""

"""
DONE:
# STATUS: LOOKS ALL DONE
# login del usuario (Consultar que exista y dar acceso) check
# Horario del usario check
# circulares check
# post para agendar materias update materiaalumno, materia
# get para oferta (ver que show ya que son muchos campos y no simpre estaran llenos)
Modify data base to have spaces for courses
"""

app = Flask(__name__)
db = mysql.connector.connect (
    user = "userName", password = "password", database = "theamUdg")

cursor = db.cursor()

def data_exists(table, column, data):
    retData = False
    preliminar = "error"
    query = f"SELECT {column} FROM {table} WHERE {column}=\"{data}\""
    cursor.execute(query)
    for aux in cursor.fetchall():
        preliminar = aux[0]
        if preliminar != "error":
            retData = True
    return retData

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
    query = "SELECT codigo, nombre, apellidoP, apellidoM, carrera, cicloInicio,"\
            "activo FROM usuario WHERE codigo = %s ORDER BY apellidoP"
    cursor.execute(query,(cod,))
    usuario = {}
    for row in cursor.fetchall():
        usuario = {
            'codigo' : row[0],
            'nombre' : row[1],
            'apellidoP' : row[2],
            'apellidoM' : row[3],
            'carrera' : row[4],
            'ciclo' : row[5],
            'activo' : row[6]
        }
    return usuario

def getCourses(dataBase, code):
    cursor =  dataBase.cursor()
    query = 'SELECT nrc FROM materiaAlumno WHERE codigo = %s'
    cursor.execute(query, (code,))
    nrc = []
    for row in cursor.fetchall():
        a = row[0]
        nrc.append(a)
    courses = []
    for course in nrc:
        queryCour = 'SELECT * FROM materia WHERE nrc = %s'
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
                'Profesor' : row[9],
                'Ciclo': row[10],
                'Centro' : row[11]
            }
            courses.append(a)
    return courses

@app.route("/")
@app.route("/login", methods = ['GET'])
def accessUser ():
    codigo = request.args.get('codigo')
    passw = request.args.get('contrasenia')
    if codigo == None:
        return jsonify({'code': 'Error: No code or password provided'})
    elif passw == None:
        return jsonify({'code': 'Error: No code or password provided'})
    elif data_exists("usuario", "codigo", codigo) == False:
        return jsonify({'code':'Error: code or password are incorrect'})
    elif data_exists("usuario", "contrasenia", passw) == False:
        return jsonify({'code':'Error: code or password are incorrect'})
    elif (login(db,codigo,passw)):
        return jsonify(getUserData(db,codigo))
    return (jsonify({'code':'User doesn\'t exist'}))

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
@app.route('/horario/<int:codigo>')
def userCourses(codigo=None):
    if codigo == None:
        return jsonify({'Code':'User code missing'})
    elif codigo:
        return jsonify(getCourses(db,codigo))
    return jsonify({'Code':'Error'})

'''
Formats for request:
    GET -> /agenda?codigo=userCode&nrc=nrcRegis
'''
@app.route('/agenda', methods = ['POST'])
def registrarMateriaAlumno():
    if request.method == 'POST' and request.is_json:
        data = request.get_json()
        nrc = data["nrc"]
        codigo = data["codigo"]
        cuposDis = get_cupos_dis(nrc)
        if not codigo and not nrc:
            return jsonify({'code' : 'Missing CODE and NRC'})
        if not codigo or not nrc:
            return jsonify({'code' : 'Missing argument', 'cod' : codigo, 'nrc' : nrc})
        if cuposDis == "error":
            return jsonify({'code': 'Invalid NRC'})
        if data_exists("usuario", "codigo", codigo) == False:
            return jsonify({'code': 'Invalid code'})
        # Mensaje de error en caso de que el alumno quiera ingresar la misma materia más de una vez
        if data_exists("materiaAlumno", "codigo", codigo) == True and data_exists("materiaAlumno", "nrc", nrc):
            return jsonify({'code': 'User has already registered this course'})
        if (cuposDis >= 0):
            cuposDis = cuposDis - 1
            query = "UPDATE materia SET cuposDis=%s WHERE nrc=%s"
            cursor.execute(query, (cuposDis, nrc))
            db.commit()
            # se modifica tabla materiaAlumno
            query = "INSERT INTO materiaAlumno (codigo, nrc) VALUES (%s, %s)"
            cursor.execute(query, (codigo, nrc))
            db.commit()
            return jsonify({"code": "ok"})
        # Si la materia ya cuenta con cupo negativo entonces se hay un error
        return jsonify({"code": "error no space"})
    else:
        return jsonify({"code": "Error"})

@app.route('/oferta', methods=['GET'])
def oferta():
    data = []
    ciclo = request.args.get('ciclo')
    centro = request.args.get('centro')
    clave = request.args.get('clave')
    materia = request.args.get('materia')
    maestro = request.args.get('maestro')
    multiple = False
    query = "SELECT * FROM materia WHERE"
    if (ciclo):
        if (multiple):
            query += " AND"
        else:
            multiple = True
        query += f" ciclo=\"{ciclo}\""
    if (clave):
        if (multiple):
            query += " AND"
        else:
            multiple = True
        query += f" clave=\"{clave}\""
    if (materia):
        if (multiple):
            query += " AND"
        else:
            multiple = True
        query += f" nrc=\"{materia}\""
    if (maestro):
        if (multiple):
            query += " AND"
        else:
            multiple = True
        query += f" profesor=\"{maestro}\""
    if (centro):
        if (multiple):
            query += " AND"
        else:
            multiple = True
        query += f" centro=\"{centro}\""
    if query == "SELECT * FROM materia WHERE":
        return jsonify({'code': 'Error, no data avaliable'})
    else:
        query += ' ORDER BY nrc'
    cursor.execute(query)
    auxLista = cursor.fetchall()
    if len(auxLista) != 0:
        for row in auxLista:
            auxData = {
                    'NRC' : row[0],
                    'Clave' : row[1],
                    'Materia' : row[2],
                    'Seccion' : row[3],
                    # Hace falta poner créditos
                    'Créditos': 0,
                    'Cupos': row[9],
                    'CuposDis': row[10],
                    'Horario' : row[4],
                    'Dias': row[5],
                    'Edificio' : row[6],
                    'Aula' : row[7],
                    'Ciclo': row[11],
                    'Maestro' : row[8]
                }
            data.append(auxData)
            return jsonify(data)
    data = { "code": "Error" }
    return jsonify(data)

def get_cupos_dis(nrc):
    # Dato preliminar, si el dato no cambia después de realizar la
    # query entonces la consulta falló    
    cuposDis = "error"
    if not nrc:
        return jsonify({'code': 'NRC Missing'})
    query = "SELECT cuposDis from materia WHERE nrc=%s"
    cursor.execute(query, (nrc,))
    for aux in cursor.fetchall():
        cuposDis = aux[0]
    return cuposDis

if __name__ == '__main__':
    app.run (debug = True)
