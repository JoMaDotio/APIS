from db_connector import getLessons, getContent, getActualRanking, updateRanking
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/menu')
def getMenu():
    lessons = getLessons()
    for lesson in lessons:
        lesson["content"] = getContent(lesson["numLess"])
    return jsonify(lessons)


@app.route('/lesson/')
@app.route('/lesson/<int:num>')
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
    elif request.method == 'POST' and request.is_json:
        data =  request.get_json()
        userName = data['userName']
        wpm = data['wpm']
        print (data)
        if (updateRanking(userName, wpm)):
            return jsonify({'code' : 'all good'})
        else: 
            return jsonify({'code' : 'Not added'})

if __name__ == '__main__':
    app.run(debug=True)
