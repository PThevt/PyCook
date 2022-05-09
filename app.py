from flask import Flask, jsonify
import json
from all_recipe_retriever import retrieve
from my_encoder import MyEncoder

app = Flask(__name__)


@app.route('/recipes/', methods=['GET'])
def get():
    """
        returns a list of recipes
        """
    recipes = retrieve()
    data = [
           MyEncoder().encode(recipe)
           for recipe in recipes
        ]
    return jsonify({
        'status': 'ok',
        'data': data
    })


if __name__ == "__main__":
    app.run(debug=True)
