from db_connector import getLessons, getContent, getActualRanking
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/menu')
def getMenu():
    lessons = getLessons()
    for lesson in lessons:
        lesson["content"] = getContent(lesson["numLess"])
    return jsonify(lessons)

@app.route('/lesson<int:num>')
def getLessonData(num=1):
    lesson = getLessons(num)
    lesson["content"] = getContent(lesson["numLess"])
    print(lesson)
    return jsonify(lesson)

@app.route('/ranked', methods = ['GET','POST'])
def getRanking():
    if request.method == 'GET':
        return jsonify(getActualRanking())
    # actualizar lista rankeada
    elif request.method == 'POST':
        pass

if __name__ == '__main__':
    app.run(debug=True)