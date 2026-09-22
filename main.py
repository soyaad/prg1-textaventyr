name = input("choose your name")
print(f" Hi {name}, you seem lost in a strange new world.")
choise = input(" what do you choose (stay/go forward)")
if choise.lower() == "go forward" :
    print(f"{name} starts walkning forward.")
    print(f"you walk for a while and you end up at a strange door")
else:
    print(f"for some reason {name} stayed.")
    print(f"{name} stood there for a while and died from starvation")
    print(f"game over")
    exit()
choise2 = input(f"{name} arrives at the door. What is your choise? (open/keep it closed) ")

if choise2.lower() == "open" : 
    print(f"{name} opends the door. You walk inside and the door closes behind you")
    choise3 = input(f"everything is dark except a tiny green light in a corner far away but theres also a red ligt in the other corner. Which light do you choose? (green/red)")
    if choise3.lower() == "red": 
        print(f"of course you choose the red light to be smart, and it seems that you are right ")
        print(f"you end ut at the red light and you find a exit door. You opend the door and wake up in your own bed, it was just a silly dream")
        exit()
    else : 
        print(f"you went whit the smart answer and choose the green ligt cuz green=good.")
        print(f"you walk up to the light and relize it not a light, its a gigant anglerfish. u get eaten")
        print(f"game over")
        exit()
        

else: 
    print(f"{name} thinks the door is too suspicious")
    print(f"you decide to look around the door and you end up finding another door.")

    print(f"you decide to go opend the door")
    choise4=input(f"you enter the door but you end up falling down a deep hole. At the end of the hole you see a dark pit and a door. what do you choose (dark pit/door)")
    if choise4.lower() == "dark pit" :
        print(f"you jump down the pit because you want to but you end up landing on a pile of spikes and die")
        print(f"game over, {name} what did you think would happend??")
        exit()

    else:
        print(f"you open the door and ypu end up waking up in your bed")
        exit()

 