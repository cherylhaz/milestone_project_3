import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

from os import path
if path.exists("env.py"):
    import env 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_box'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')


@app.route('/')
def main_page():
    return render_template('index.html',
    categories = mongo.db.categories.find())


@app.route('/search_results')
def search_results():
    return render_template("search_results.html", recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
