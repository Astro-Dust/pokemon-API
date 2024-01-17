from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/search", methods=["POST"])
def search():
    name = request.form["name"].capitalize()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
    data = response.json()
    
    photo = data["sprites"]["front_default"]
    pokemon_number = data["id"]
    pokemon_type = data["types"][0]["type"]["name"].capitalize()
    
    type_color = get_type_color(pokemon_type)
    
    return render_template("chosen_pokemon.html", name=name, photo=photo, pokemon_type=pokemon_type, pokemon_number=pokemon_number, type_color=type_color)

def get_type_color(pokemon_type):
    type_colors = {
        "Normal":"#A8A77A",
        "Fire": "#EE8130",
        "Water": "#6390F0"
    }
    return type_colors.get(pokemon_type, "#fff")

app.run(debug=True, port=8000)
