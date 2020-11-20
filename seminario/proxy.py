from db_connector import getLessons, getContent
from flask import Flask, jsonify

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

if __name__ == '__main__':
    app.run(debug=True)