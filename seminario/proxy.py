from db_connector import get_lessons, get_text
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/lesson_menu')
def get_lessons_menu():
    dicc = get_lessons()
    dicc["data"] = get_text(dicc["numLess"])
    return jsonify(dicc)

@app.route('/lessons')
def get_all_lessons(numLess=1):
    return jsonify(get_text())

@app.route('/lesson<int:id>')
def get_text_db(numLess=1):
    return jsonify(get_text(id))

if __name__ == '__main__':
    app.run(debug=True)
