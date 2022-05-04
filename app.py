from flask import Flask, jsonify
import json
from all_recipe_retriever import retrieve
from my_encoder import MyEncoder

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello World!'


@app.route('/recipes/')
def get():
    """
        returns a list of recipes
        """
    recipes = retrieve()
    print("recipes retrieved")
    print(recipes)
    data = []
    for recipe in recipes:
        data.append(MyEncoder().encode(recipe))
    print("The response")
    print(data)
    return jsonify({
        'status': 'ok',
        'data': data
    })


if __name__ == "__main__":
    app.run(debug=True)
