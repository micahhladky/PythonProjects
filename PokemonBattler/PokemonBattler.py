import random
import json

#Initialize Pokedex
with open(r"C:\Users\micah\OneDrive\Documents\GitHub\PythonProjects\PokemonBattler\Pokedex.json") as Pokedex_json:
    Pokedex = json.load(Pokedex_json)
#print(Pokedex)

#Initialize Type Chart
with open(r"C:\Users\micah\OneDrive\Documents\GitHub\PythonProjects\PokemonBattler\Type_Chart.json") as Type_Chart_json:
    Type_Chart = json.load(Type_Chart_json)
#print(Type_Chart)

def main():
    #Ask the player who their pokemon is
    Player_Pokemon_Name = input('Who is your Pokemon?\n')
    #Ensure Player_Pokemon_Name is valid
    while Player_Pokemon_Name not in Pokedex:
        print('Error! Invalid pokemon. Choose from ', list(Pokedex.keys()), ". ")
        Player_Pokemon_Name = input('Who is your Pokemon?\n')

    print(Player_Pokemon_Name, ', I choose you!')

    #Random Pokemon for Computer opponent
    Computer_Pokemon_Name = random.choice(list(Pokedex.keys()))
    print("Battle: ", Player_Pokemon_Name, "vs. ", Computer_Pokemon_Name, "!")
    
    Player_Pokemon_Stats = Pokedex[Player_Pokemon_Name]
    Computer_Pokemon_Stats = Pokedex[Computer_Pokemon_Name]
    
    #Player_Pokemon_HP = Pokedex[Player_Pokemon_Name]["hp"]
    #Computer_Pokemon_HP = Pokedex[Computer_Pokemon_Name]["hp"]
    
    while Player_Pokemon_Stats["hp"] > 0 and Computer_Pokemon_Stats["hp"] > 0:
        Computer_Pokemon_Stats["hp"] = Attack_turn(Player_Pokemon_Stats, Computer_Pokemon_Stats)        
        if Computer_Pokemon_Stats["hp"] > 0:
            Player_Pokemon_Stats["hp"] = Attack_turn(Computer_Pokemon_Stats, Player_Pokemon_Stats)
        else:
            pass
        
    if Player_Pokemon_Stats["hp"] <= 0:
        print("You lose!") 
    elif Computer_Pokemon_Stats["hp"] <= 0:
        print("You win!")
    else:
        print("IDK who won, I'm just glad we all had fun.")

#Individual Attack Turn Mapping
def Attack_turn(Attacking_Pokemon, Defending_Pokemon):
    Attack_Type = Attacking_Pokemon["type"]
    Defense_Type = Defending_Pokemon["type"]
    Attack_Value = Attacking_Pokemon["attack"]
    Defense_HP = Defending_Pokemon["hp"]
    Damage_Multiplier = Type_Chart[Attack_Type][Defense_Type]
    Damage_Dealt = int(Attack_Value * Damage_Multiplier)
    
    print(Attacking_Pokemon["name"], " hits ", Defending_Pokemon["name"], " for ", Damage_Dealt, " damage!")
    
    if Damage_Multiplier == 1.0:
        print("It's effective!")
    elif Damage_Multiplier == 2.0:
        print("It's super-effective!")
    elif Damage_Multiplier == 0.5:
        print("It's not very effective...")
    elif Damage_Multiplier == 0.0:
        print("It doesn't affect enemy ", Defending_Pokemon["name"], "...")
    
    Before_HP = Defense_HP
    After_HP = Before_HP - Damage_Dealt
    Show_HP_Change = str(Before_HP) + " --> " + str(After_HP)
    print(Show_HP_Change)
    return After_HP

main()