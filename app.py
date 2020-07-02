import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_box'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', categories=mongo.db.categories.find(), sub_categories=mongo.db.sub_categories.find(), required_tools=mongo.db.required_tools.find())


@app.route('/search_results')
def search_results():
    return render_template("search_results.html", recipes=mongo.db.recipes.find())


# Add New Recipe to Database
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('submitted')) 


# Delete Recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('search_results'))


# Edit Recipe
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    all_sub_categories = mongo.db.sub_categories.find()
    all_required_tools = mongo.db.required_tools.find()
    return render_template('edit_recipe.html', recipe=the_recipe,
                           categories=all_categories,
                           sub_categories = all_sub_categories,
                           required_tools = all_required_tools)


@app.route('/submitted')
def submitted():
    return render_template("submission.html")


@app.route('/more_info')
def more_info():
    return render_template("more_information.html")


@app.route('/')
def main_page():
    return render_template('index.html', categories=mongo.db.categories.find(),sub_categories=mongo.db.sub_categories.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
