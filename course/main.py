import random

def affichage_info(user_input, value):
    if(user_input > value):
        return(f"Le nombre est plus petit que {user_input}")
    elif(user_input < value):
        return(f"Le nombre est plus grand que {user_input}")
    else:
        return f"BRAVO le nombre était bien {value}"

want_continue = True;

while(want_continue):
    difficulty = 0
    choose = 0
    maxi = 0
    while(difficulty not in [1,2,3]):
        difficulty = int(input("Entrez une difficulté : \n 1.Facile(1-10) \n2.normal(1-100) \n3.Difficile(1-1000)\n"))
    choose = int(input("entrez un nombre : "))
    match difficulty:
        case 1:
            rand = random.randint(1,10)
            while(choose != rand):
                print(affichage_info(choose,rand))
                choose = int(input())
        case 2:
            rand = random.randint(0,100)
            while(choose != rand):
                print(affichage_info(choose,rand))
                choose = int(input())
        case 3:
            rand = random.randint(0,1000)
            while(choose != rand):
                print(affichage_info(choose,rand))
                choose = int(input())


    if(input('Voulez-vous continuer ?(O/n)') == "N"):
        want_continue = False


print("A la prochaine")

