#VACCUM_CLEANER
room_A=str(input("Is room A dirty or clean?:"))
room_B=str(input("Is room B dirty or clean?:"))
current="ra"
while room_A=="dirty" or room_B=="dirty":
    print("Current room:A")
    if room_A=="dirty":
        print("Cleaning room A")
        room_A="clean"
    else:
        print("room A is clean")
    print("moving right")
    print("Current room:B")
    current="rb"
    if room_B=="dirty":
        print("Cleaning room B")
        room_B="clean"
    else:
        print("room B is clean")
print("Cleaning Completed")
