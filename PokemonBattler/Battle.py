import __init__

def Attack_Turn(Attacking_Pokemon, Defending_Pokemon, Chosen_Attack_Type, Attack_Name):
    Attack_Type = Chosen_Attack_Type
    Attack_Name = Attack_Name
    Defense_Type = Defending_Pokemon["type"]
    Attack_Value = Attacking_Pokemon["attack_value"]
    Defense_HP = Defending_Pokemon["hp"]
    
    #Normal Damage Multiplier vs Type Damage Multiplier
    if Attack_Type == Attacking_Pokemon["type"]:
        Damage_Multiplier = __init__.Type_Chart[Attack_Type][Defense_Type]
    elif Attack_Type == "Normal":
        Damage_Multiplier = 1.0
    else:
        print("Damange Multiplier Error!")
    
    #Calculate Damage Done
    Damage_Dealt = int(Attack_Value * Damage_Multiplier)
    
    #Tell Player what happened
    print(Attacking_Pokemon["name"], "uses ", Attack_Name, "!")
    print(Attacking_Pokemon["name"], " hits ", Defending_Pokemon["name"], " for ", Damage_Dealt, " damage!")
    if Damage_Multiplier == 1.0:
        print("It's effective!")
    elif Damage_Multiplier == 2.0:
        print("It's super-effective!")
    elif Damage_Multiplier == 0.5:
        print("It's not very effective...")
    elif Damage_Multiplier == 0.0:
        print("It doesn't affect enemy ", Defending_Pokemon["name"], "...")
    
    #Show Player HP Change
    Before_HP = Defense_HP
    After_HP = Before_HP - Damage_Dealt
    Show_HP_Change = str(Before_HP) + " --> " + str(After_HP)
    print(Show_HP_Change)
    return After_HP
