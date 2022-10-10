import random
n=int(input("Entrer a number between 0-9: "))
predict=int((random.randint(0,9)))

while n>5:
    print("YOU LOSE, THE NUMBER IS: ",predict)
    if (n==predict):
        print("YOU WIN!")
    else:
        print("YOU LOSE!")

