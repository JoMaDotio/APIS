from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect (
    user="userName", password="password", database="theamUdg", buffered=True)

cursor = db.cursor()

def data_exists(table, column, data):
    retData = False
    preliminar = "error"
    query = f"SELECT {column} FROM {table} WHERE {column}=\"{data}\""
    try:
        cursor.execute(query)
    except:
        return False
    for aux in cursor.fetchall():
        preliminar = aux[0]
        if preliminar != "error":
            retData = True
    return retData

def login(data_base, cod, password):
    cursor = data_base.cursor()
    query = "SELECT COUNT(*) FROM usuario WHERE codigo = %s AND contrasenia = %s"
    try:
        cursor.execute(query, (cod,password))
    except:
        return False
    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False

def getUserData(dataBase, cod):
    cursor = dataBase.cursor()
    query = "SELECT codigo, nombre, apellidoP, apellidoM, carrera, cicloInicio,"\
            "activo FROM usuario WHERE codigo = %s ORDER BY apellidoP"
    try:
        cursor.execute(query,(cod,))
    except:
        return 
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

@app.route('/horario', methods=['GET'])
def getSchedule():
    if request.method == 'GET':
        codigo = request.args.get('codigo')
        return jsonify(getCourses(db, codigo))
    else:
        return jsonify({"code": "error"})

def getCourses(dataBase, code):
    cursor =  dataBase.cursor()
    query = 'SELECT nrc FROM materiaAlumno WHERE codigo = %s'
    try:
        cursor.execute(query, (code,))
    except:
        return {"code": "error"}
    nrc = []
    for row in cursor.fetchall():
        a = row[0]
        nrc.append(a)
    courses = []
    for course in nrc:
        queryCour = 'SELECT nrc, clave, materia, seccion, horario, dias,'\
                    'edificio, aula, profesor, cupos, cuposDis, ciclo,'\
                    ' centro FROM materia WHERE nrc = %s'
        try:
            cursor.execute(queryCour, (course,))
        except:
            return {"code": "error"}
        row = cursor.fetchone()
        if row:
            a = {
                'NRC' : row[0],
                'Clave' : row[1],
                'Nombre' : row[2],
                'Seccion' : row[3],
                'Horario' : row[4],
                'Dias' : row[5],
                'Edificio' : row[6],
                'Aula' : row[7],
                'Profesor' : row[8],
                'Cupos': row[9],
                'CuposDis': row[10],
                'Ciclo': row[11],
                'Centro' : row[12]
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
    try:
        cursor.execute(query, (cant,))
    except:
        return jsonify({"code": "error"})
    circulares = []
    for row in cursor.fetchall():
        a = {
            'contenido' : row[0],
            'numero' : row[1],
            'fecha' : row[2]
        }
        circulares.append(a)
    return jsonify(circulares)

'''
Formats for request:
    GET -> /agenda?codigo=userCode&nrc=nrcRegis
'''

@app.route('/agenda', methods = ['POST'])
def agendar():
    if request.method == 'POST' and request.is_json:
        data = []
        courses = request.get_json()
        for nrc in courses["nrcs"]:
            auxData = registrarMateriaAlumno(nrc, courses["codigo"])
            auxData["nrc"] = nrc
            data.append(auxData)
        return jsonify(data)
    else:
        return jsonify({"nrc": "Error", "code": "Error"})

def registrarMateriaAlumno(nrc, codigo):
    cuposDis = get_cupos_dis(nrc)
    if not codigo and not nrc:
        return {'code' : 'Missing CODE and NRC'}
    if not codigo or not nrc:
        return {'code' : 'Missing argument', 'cod' : codigo, 'nrc' : nrc}
    if data_exists("usuario", "codigo", codigo) == False:
        return {'code': 'Invalid code'}
    if data_exists("materia", "nrc", nrc) == False:
        return {'code': 'Invalid nrc'}
    if cuposDis == "error":
        return {'code': 'Error'}
    # Mensaje de error en caso de que el alumno quiera ingresar la misma materia más de una vez
    if data_exists("materiaAlumno", "codigo", codigo) == True and data_exists("materiaAlumno", "nrc", nrc):
        return {'code': 'User has already registered this course'}
    if (cuposDis >= 0):
        cuposDis = cuposDis - 1
        query = "UPDATE materia SET cuposDis=%s WHERE nrc=%s"
        try:
            cursor.execute(query, (cuposDis, nrc))
        except:
            return {'code': 'Error'}
        db.commit()
        # se modifica tabla materiaAlumno
        query = "INSERT INTO materiaAlumno (codigo, nrc) VALUES (%s, %s)"
        try:
            cursor.execute(query, (codigo, nrc))
        except:
            return {'code': 'Error'}
        db.commit()
        return {"code": "ok"}
    # Si la materia ya cuenta con cupo negativo entonces se hay un error
    return {"code": "error no space"}
    

@app.route('/oferta', methods=['GET'])
def oferta():
    data = []
    ciclo = request.args.get('ciclo')
    centro = request.args.get('centro')
    clave = request.args.get('clave')
    materia = request.args.get('materia')
    maestro = request.args.get('maestro')
    nrc = request.args.get('nrc')
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
    if (nrc):
        if (multiple):
            query += " AND"
        else:
            multiple = True
        query += f" nrc=\"{nrc}\""
    if (materia):
        if (multiple):
            query += " AND"
        else:
            multiple = True
        query += f" materia=\"{materia}\""
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
        query += ' ORDER BY materia'
    try:
        cursor.execute(query)
    except:
        data = {"code": "Error"}
        return jsonify(data)
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
    try:
        cursor.execute(query, (nrc,))
    except:
        return "error"
    for aux in cursor.fetchall():
        cuposDis = aux[0]
    return cuposDis

if __name__ == '__main__':
    app.run (debug = True)
