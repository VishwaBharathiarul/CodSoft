import random
print("\t\t****Rock Paper Scissors Game****")
print("Rock beats scissors, scissors beat paper, and paper beats rock.\nPoints will be displayed when the user presses 6, which determines the end of a round.")
point = 0
pointcmp = 0    
while True:
    ch = int(input('''Choose your move
    1.Rock
    2.Paper
    3.Scissors
    press 6 to stop playing: '''))
    sys = random.randint(1,3)
    if ch == 6:
        if(point > pointcmp):
            print()
            print("   ***Points Table*** ")
            print(f"   Player1: {point}\n   System: {pointcmp}")
            print("You WON!!")
        else:
            print()
            print("   ***Points Table***  ")
            print(f"   Player1: {point}\n   System: {pointcmp}")
            print("You LOST :(")
        break
    elif sys == ch:
        print("Draw")
    elif sys == 1:
        if ch == 3:
            print("System gets a point")
            pointcmp+=1
        else :
            print("Player gets a point")
            point+=1
    elif sys == 2:
        if ch == 1:
            print("System gets a point")
            pointcmp+=1
        else:
            print("Player gets a point")
            point+=1
    else:
        if ch == 1:
            print("Player gets a point")
            point+=1
        else:
            print("System gets a point")
            pointcmp+=1

    
