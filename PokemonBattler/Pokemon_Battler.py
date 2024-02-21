import random
import __init__ as i
import Battle

def main():
    #Ask the player who their pokemon is
    Player_Pokemon_Name = input('Who is your Pokemon?\n')
    #Ensure Player_Pokemon_Name is valid
    while Player_Pokemon_Name not in i.Pokedex:
        print('Error! Invalid pokemon. Choose from ', list(i.Pokedex.keys()), ". ")
        Player_Pokemon_Name = input('Who is your Pokemon?\n')

    print(Player_Pokemon_Name, ', I choose you!')

    #Random Pokemon for Computer opponent
    Computer_Pokemon_Name = random.choice(list(i.Pokedex.keys()))
    print("Battle: ", Player_Pokemon_Name, "vs. ", Computer_Pokemon_Name, "!")
    
    Player_Pokemon_Stats = i.Pokedex[Player_Pokemon_Name]
    Computer_Pokemon_Stats = i.Pokedex[Computer_Pokemon_Name]
    
    #Player_Pokemon_HP = i.Pokedex[Player_Pokemon_Name]["hp"]
    #Computer_Pokemon_HP = i.Pokedex[Computer_Pokemon_Name]["hp"]
    
    while Player_Pokemon_Stats["hp"] > 0 and Computer_Pokemon_Stats["hp"] > 0:
        #Player Turn
        #Initialize Attack Names
        Player_Type_Attack = Player_Pokemon_Stats["type_attack"]
        Player_Normal_Attack = Player_Pokemon_Stats["normal_attack"]
        
        #Give Player Attack Options
        print(Player_Type_Attack, "\n", Player_Normal_Attack)
        Player_Attack_Choice = input("Choose an attack: ")
        #print("PAC = ", Player_Attack_Choice, "PNA = ", Player_Normal_Attack, "PTA = ", Player_Type_Attack)
        
        #Ensure Input is valid
        while Player_Attack_Choice != Player_Normal_Attack and Player_Attack_Choice != Player_Type_Attack:
            print(Player_Attack_Choice)
            print("Error! Invalid attack choice. Please use either ", Player_Type_Attack, "or ", Player_Normal_Attack, ".")
            print(Player_Type_Attack, "\n", Player_Normal_Attack)            
            Player_Attack_Choice = input("Choose an attack: ")
        
        #Convert PAC to Player Attack Type
        if Player_Attack_Choice == Player_Type_Attack:
            Player_Attack_Type = Player_Pokemon_Stats["type"]
        elif Player_Attack_Choice == Player_Normal_Attack:
            Player_Attack_Type = "Normal"
        else:
            print("Error! Invalid attack selection.")
        
        #Run Battle.Attack_Turn
        Computer_Pokemon_Stats["hp"] = Battle.Attack_Turn(Player_Pokemon_Stats, Computer_Pokemon_Stats, Player_Attack_Type, Player_Attack_Choice)
        
        #Computer Turn
        Computer_Attack_Type_List = (Computer_Pokemon_Stats["type"], "Normal")
        Computer_Attack_Choice_Type = random.choice(Computer_Attack_Type_List)
        if Computer_Attack_Choice_Type == Computer_Pokemon_Stats["type"]:
            Computer_Attack_Name = Computer_Pokemon_Stats["type_attack"]
        elif Computer_Attack_Choice_Type == "Normal":
            Computer_Attack_Name = Computer_Pokemon_Stats["normal_attack"]
        else:
            print("Computer Attack Name Error!")
            
        if Computer_Pokemon_Stats["hp"] > 0:
            Player_Pokemon_Stats["hp"] = Battle.Attack_Turn(Computer_Pokemon_Stats, Player_Pokemon_Stats, Computer_Attack_Choice_Type, Computer_Attack_Name)
        else:
            pass
        
    if Player_Pokemon_Stats["hp"] <= 0:
        print("You lose!") 
    elif Computer_Pokemon_Stats["hp"] <= 0:
        print("You win!")
    else:
        print("IDK who won, I'm just glad we all had fun.")

main()