# Exercise 1
# import flask
# print(dir(flask))

# Exercise 2
import flask

app = flask.Flask(__name__)

hobbies = [
	{
		"name": "article1",
		"title": "RC models"
	},
	{
		"name": "article2",
		"title": "Programming"
	},
	{
		"name": "article3",
		"title": "Street sport"
	},
]

skills = [
	{
		"name": "article1",
		"title": "css"
	},
	{
		"name": "article2",
		"title": "html"
	},
	{
		"name": "article3",
		"title": "python"
	},
]

strengths = ['focus', 'hard will power', 'humor']
weaknesses = ['low level english', 'love to complicated people']
@app.route('/user-name')
def main_page():
	return f'''
		<html>
			<head>
				<title>Articles Titles</title>
			</head>
			<body>
				<h1>Hello, Gleb !</h1>
				<a href="http://127.0.0.1:8080/picture">My picture</a>
				<a href="http://127.0.0.1:8080/your-hobbies">Hobbies</a>
				<a href="http://127.0.0.1:8080/skills">Your skills</a>
				<a href="http://127.0.0.1:8080/strengths">Strengths</a>
				<a href="http://127.0.0.1:8080/weaknesses">Weaknesses</a>
			</body>
		</html>'''


@app.route('/picture')
def display_articles_titles():
	return f'''
	<html>
	    <head>
	        <title>Articles Titles</title>
	    </head>
	    <body>
            <img src="/man-icon.webp" alt="Prof-img" width="500" height="600">    
	    </body>
	</html>'''

@app.route('/your-hobbies')
def display_hobbies_titles():
	hobbies_titles = list(map(lambda article: article["title"], hobbies))
	template = '''
	<html>
	    <head>
	        <title>My hobbies</title>
	    </head>
	    <body>
	        <h1>{{hobbies}}</h1>
	    </body>
	</html>'''
	return flask.render_template_string(template, hobbies=hobbies_titles)

@app.route('/skills')
def display_skills_titles():
	skills_titles = list(map(lambda article: article["title"], skills))
	template = '''
	<html>
	    <head>
	        <title>Articles Titles</title>
	    </head>
	    <body>
	        <h1>{{skills}}</h1>
	    </body>
	</html>'''
	return flask.render_template_string(template, skills=skills_titles)

@app.route('/strengths')
def display_strengths_titles():
	strengths_titles = list(map(lambda article: article, strengths))
	template = '''
	<html>
	    <head>
	        <title>Articles Titles</title>
	    </head>
	    <body>
	        <h1>{{strengths}}</h1>
	    </body>
	</html>'''
	return flask.render_template_string(template, strengths=strengths_titles)
@app.route('/weaknesses')
def display_weaknesses_titles():
	weaknesses_titles = list(map(lambda article: article, weaknesses))
	template = '''
	<html>
	    <head>
	        <title>Articles Titles</title>
	    </head>
	    <body>
	        <h1>{{weaknesses}}</h1>
	    </body>
	</html>'''
	return flask.render_template_string(template, weaknesses=weaknesses_titles)

app.run(port=8080, debug=True)
