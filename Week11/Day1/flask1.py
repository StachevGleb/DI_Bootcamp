# import flask

# app = flask.Flask(__name__)
#
# articles = [
# 	{
# 		"name": "article1",
# 		"title": "article1 title"
# 	},
# 	{
# 		"name": "article2",
# 		"title": "article2 title"
# 	},
# 	{
# 		"name": "article3",
# 		"title": "article3 title"
# 	},
# ]
#
#
# @app.route('/blog')
# def main_page():
# 	return "Hello to all the users"
#
#
# @app.route('/blog/articles')
# def display_articles_titles():
# 	articles_titles = list(map(lambda article: article["title"], articles))
# 	template = '''
# 	<html>
# 	    <head>
# 	        <title>Articles Titles</title>
# 	    </head>
# 	    <body>
# 	        <h1>{{titles}}</h1>
# 	    </body>
# 	</html>'''
# 	return flask.render_template_string(template, titles=articles_titles)
#
#
# app.run(port=8080, debug=True)

import flask
app = flask.Flask(__name__)

template = '''
	<html>
	    <head>
	        <title>homepage.html</title>
	    </head>
	    <body>
	        <h1>Hello there</h1>
	    </body>
	</html>'''

articles = [
	{
		"name": "article1",
		"title": "article1 title"
	},
	{
		"name": "article2",
		"title": "article2 title"
	},
	{
		"name": "article3",
		"title": "article3 title"
	},
]

@app.route('/blog/articles')
def display_articles_titles():
	articles_titles = list(map(lambda article: article["title"], articles))
	template = '''
	<html>
	    <head>
	        <title>Articles Titles</title>
	    </head>
	    <body>
	        <h1>{{titles}}</h1>
	    </body>
	</html>'''
	return flask.render_template_string(template, titles=articles_titles)
@app.route('/blog')
def main_page():
	return flask.render_template_string(template)

app.run(port=5000,debug=True)