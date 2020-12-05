import mysql.connector

# Nos conectamos a la base de datos
# NOTA: user y password pueden cambiar dependiendo de la base de datos
# que vayan a usar.
db = mysql.connector.connect(user='userName',
                             password='password',
                             database='typing_game')
cursor = db.cursor()

# Función que retorna una lista que contiene los diccionarios que corresponden
# a cada lección almacenada en la base de datos


def getLessons(numLess=None):
    dataList = []
    if numLess:
        query = "SELECT * FROM lesson WHERE numLess=%s"
        try:
            cursor.execute(query, (numLess,))
        except:
            return dataList
        auxTuple = cursor.fetchall()
        innerAT = auxTuple[0]
        data = {
            "numLess": innerAT[0],
            "name": innerAT[1],
            "explanation": innerAT[2],
            "category": innerAT[3],
            "content": []
        }
        return data
    # Se ejecuta la query especificada
    try:
        cursor.execute("SELECT * FROM lesson;")
    except:
        return dataList
    # fetchall regresa una lista que contiene a todos los registros retornados
    # por la base de datos anterior, por lo que iteramos por esta obteniendo
    # sus filas
    for row in cursor.fetchall():
        data = {
            "numLess": row[0],
            "name": row[1],
            "explanation": row[2],
            "category": row[3],
            "content": []
        }
        dataList.append(data)
    return dataList

# Función que retorna una lista de contenidos ("textos aleatorios"), se le puede
# proporcionar el id de la lección a la que están ligados para filtrarlos


def getContent(numLess=None):
    # Si se proporciona una id
    contents = []
    idRands = []
    if numLess:
        query = "SELECT idRand FROM lessRand WHERE idLess=%s;"
        # Se guardan todos los id de randomtext que coincidan
        # con el id proporcionado en una lista
        try:
            cursor.execute(query, (numLess,))
        except:
            return contents
        for idRandAux in cursor.fetchall():
            idRands.append(idRandAux[0])

        # Se recorre la lista y se obtiene el contenido de cada registro del
        # id proporcionado
        for idRand in idRands:
            query = """SELECT contents FROM randomText
                    WHERE id=%s;"""
            try:
                cursor.execute(query, (idRand,))
            except:
                return contents
            auxList = (cursor.fetchall())[0]
            contents.append(auxList[0])

        return contents
    # Si no se proporciona id
    cursor.execute("SELECT contents FROM randomText;")
    contents = cursor.fetchall()
    return contents

# Regresa una lista de objetos que tiene todas las posiciones del ranking


def getActualRanking():
    ranking = []
    try:
        cursor.execute("SELECT * FROM ranking ORDER BY wpm DESC LIMIT 10;")
    except:
        return ranking
    for aux in cursor.fetchall():
        data = {
            "username": aux[0],
            "wpm": aux[1]
        }
        ranking.append(data)
    return ranking


def updateRanking(user, wpm):
    try:
        query = 'INSERT INTO ranking(userName, wpm) VALUES (%s, %s);'
        cursor.execute(query, (user, wpm))
        db.commit()
        return True
    except:
        return False


def getRandomText():
    query = 'SELECT contents FROM randomText ORDER BY RAND() LIMIT 1;'
    try:
        cursor.execute(query)
    except:
        input("No funka")
    text = []
    for row in cursor.fetchall():
        a = {
            'content': row[0]
        }
        text.append(a)
    return text
