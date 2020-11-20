import mysql.connector

# Nos conectamos a la base de datos
# NOTA: user y password pueden cambiar dependiendo de la base de datos
# que vayan a usar.
db = mysql.connector.connect (user='userName',
                              password='password',
                              database='typing_game',
                              auth_plugin='mysql_native_password')
cursor = db.cursor()

# Función que retorna un diccionario con todos los datos de todas las lecciones
def get_lessons():
    # Se ejecuta la query especificada
    cursor.execute("SELECT * FROM lesson;")
    # fetchall regresa una lista que contiene a todos los registros retornados
    # por la base de datos anterior, por lo que iteramos por esta obteniendo
    # sus filas
    for row in cursor.fetchall():
        datos = {
            "numLess": row[0],
            "name": row[1],
            "explanation": row[2],
            "category": row[3],
            "data": []
        }
    return datos

# Función que retorna un diccionario con textos aleatorios, se le puede
# proporcionar una id para filtrarlos
def get_text(numLess=None):
    # Si se proporciona una id
    content = []
    idRands = []
    if id is not None:
        query =  "SELECT idRand FROM lessrand WHERE idLess=%s;"

        # Se guardan todos los id de randomtext que coincidan
        # con el id proporcionado en una lista
        cursor.execute(query, (numLess,))
        
        for row in cursor.fetchall():
            idRands.append(row[0])

        # Se recorre la lista y se obtiene el contenido de cada registro del
        # id proporcionado
        for idRand in idRands: 
            query = """SELECT contents FROM randomtext
                    WHERE id=%s"""
            cursor.execute(query, (idRand,))
            for row in cursor.fetchall():
                content.append(row[0])
        return content
    # Si no se proporciona id
    cursor.execute("SELECT contents FROM randomtext;")
    for row in cursor.fetchall():
        content.append(row[0])
    return content
