import random
ttt=[0,0,0,0,0,0,0,0,0]
while true:
    while turn=="human":
        n=int(input("Choose ur position:"))
        if ttt[n]==0:
            ttt[n]=1
            turn="bot"
        else:
            print("tile occupied")
    while turn=="bot":
        if ttt[4]==0:
            ttt[4]=2
        
