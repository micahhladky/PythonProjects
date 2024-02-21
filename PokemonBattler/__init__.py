import json

#Initialize Pokedex
with open(r"C:\Users\micah\OneDrive\Documents\GitHub\PythonProjects\PokemonBattler\Pokedex.json") as Pokedex_json:
    Pokedex = json.load(Pokedex_json)
#print(Pokedex)

#Initialize Type Chart
with open(r"C:\Users\micah\OneDrive\Documents\GitHub\PythonProjects\PokemonBattler\Type_Chart.json") as Type_Chart_json:
    Type_Chart = json.load(Type_Chart_json)
#print(Type_Chart)
