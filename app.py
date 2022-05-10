from flask import Flask, jsonify
from all_recipe_retriever import retrieve
from my_encoder import MyEncoder
from database_init import init_tables_in_database, waiting_for_database_up

app = Flask(__name__)

waiting_for_database_up()
init_tables_in_database()


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
    print("HELLO !",flush=True)
    return jsonify({
        'status': 'ok',
        'data': data
    })


if __name__ == "__main__":
    app.run(debug=True)
