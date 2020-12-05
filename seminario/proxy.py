from db_connector import getLessons, getContent, getActualRanking, updateRanking, getRandomText
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/content/<int:num>')
def getLessonContent(num):
    return jsonify(getContent(num))

@app.route('/menu')
def getMenu():
    lessons = getLessons()
    #for lesson in lessons:
        #lesson["content"] = getContent(lesson["numLess"])
    return jsonify(lessons)


@app.route('/lesson')
@app.route('/lesson/<int:num>')
def getLessonData(num=1):
    lesson = getLessons(num)
    lesson["content"] = getContent(lesson["numLess"])
    print(lesson)
    return jsonify(lesson)

@app.route('/rankedList', methods = ['GET','POST'])
def getRanking():
    if request.method == 'GET':
        return jsonify(getActualRanking())
    # actualizar lista rankeada
    elif request.method == 'POST' and request.is_json:
        data =  request.get_json()
        userName = data['userName']
        wpm = data['wpm']
        if (updateRanking(userName, wpm)):
            return jsonify({'code' : 'ranking updated'})
        else: 
            return jsonify({'code' : 'Not added'})
    else:
        return jsonify({'code' : 'Error raised in getRanking proxy.py'})

@app.route('/randomText')
def freeMode():
    return jsonify(getRandomText())

if __name__ == '__main__':
    app.run(debug=True)
