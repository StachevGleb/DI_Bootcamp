import flask
import os
import markdownify

app = flask.Flask(__name__)

with open("'\in-this-chapter.md','a',encoding="utf8",errors="ignore") as file1:
	with open('chapter-example.txt') as file:
		file1.write('\n'.join(file.readlines()))

with open("'\exercises.md','a',encoding="utf8",errors="ignore") as file1:
	with open('exercise-example.txt') as file:
		file1.write('\n'.join(file.readlines()))

@app.route('\exercises')
def ex_page():
	return flask.render_template('exercises.md')

@app.route('\lesson')
def les_page():
	return flask.render_template('in-this-chapter.md')

app.run(port=5000,debug=True)