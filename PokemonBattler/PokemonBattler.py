import random
import json

#Create Pokedex
with open(r"C:\Users\micah\OneDrive\Documents\GitHub\PythonProjects\PokemonBattler\Pokemon.json") as f:
    Pokedex = json.load(f)

#Pokemon Types    
Types = ['Water', 'Fire', 'Grass', 'Electric', 'Flying', 'Ground']    

#Available Pokemon
Pokemon = ['Bulbasaur', 'Squirtle', 'Charmander', 'Pikachu', 'Pidgey', 'Cubone']

#Pokemon Attacks and their effectiveness against other types
Water_Attacks = {'Water': 0.5, 'Fire': 2.0, 'Grass': 0.5, 'Electric': 1.0, 'Flying': 1.0, 'Ground': 2.0}
Fire_Attacks = {'Water': 0.5, 'Fire': 0.5, 'Grass': 2.0, 'Electric': 1.0, 'Flying': 1.0, 'Ground': 1.0}
Grass_Attacks = {'Water': 2.0, 'Fire': 0.5, 'Grass': 0.5, 'Electric': 1.0, 'Flying': 0.5, 'Ground': 2.0}
Electric_Attacks = {'Water': 2.0, 'Fire': 1.0, 'Grass': 0.5, 'Electric': 0.5, 'Flying': 2.0, 'Ground': 0.0}
Flying_Attacks = {'Water': 1.0, 'Fire': 1.0, 'Grass': 2.0, 'Electric': 0.5, 'Flying': 1.0, 'Ground': 1.0}
Ground_Attacks = {'Water': 1.0, 'Fire': 2.0, 'Grass': 0.5, 'Electric': 2.0, 'Flying': 0.0, 'Ground': 1.0} 

#Pokemon and their Types
PokemonByType = {'Bulbasaur': 'Grass', 'Squirtle': 'Water', 'Charmander': 'Fire', 'Pikachu': 'Electric', 'Pidgey': 'Flying', 'Cubone': 'Ground'}

#Ask the player who their pokemon is
PlayerPokemon = input('Who is your Pokemon?\n')

#Ensure PlayerPokemon is valid
while PlayerPokemon not in Pokemon:
    print('Error! Invalid pokemon. Choose from ', Pokemon, ". ")
    PlayerPokemon = input('Who is your Pokemon?\n')

print(PlayerPokemon, ', I choose you!')

#Random Pokemon for Computer opponent
ComputerPokemon = random.choice(Pokemon)

print("Battle: ", PlayerPokemon, "vs. ", ComputerPokemon, "!")

def Battle(Pokemon_A, Pokemon_B):
    if Pokemon_A[2] == "Water":
        Pokemon_A_Attack = Water_Attacks
    elif Pokemon_A[1] == "Fire":
        Pokemon_A_Attack = Fire_Attacks
    elif Pokemon_A[1] == "Grass":
        Pokemon_A_Attack = Grass_Attacks
        Pokemon_A_Attack = Electric_Attacks
    elif Pokemon_A[1] == "Flying":
        Pokemon_A_Attack = Flying_Attacks
    elif Pokemon_A[1] == "Ground":
        Pokemon_A_Attack = Ground_Attacks
    else:
        print("Type Error")
        
    if Pokemon_B[1] == "Water":
        Pokemon_B_Attack = Water_Attacks
    elif Pokemon_B[1] == "Fire":
        Pokemon_B_Attack = Fire_Attacks
    elif Pokemon_B[1] == "Grass":
        Pokemon_B_Attack = Grass_Attacks
    elif Pokemon_B[1] == "Electric":
        Pokemon_B_Attack = Electric_Attacks
    elif Pokemon_B[1] == "Flying":
        Pokemon_B_Attack = Flying_Attacks
    elif Pokemon_B[1] == "Ground":
        Pokemon_B_Attack = Ground_Attacks
    else:
        print("Type Error")
    
    print(Pokemon_A_Attack, Pokemon_B_Attack)
    
print(Battle(PlayerPokemon, ComputerPokemon))
#main()