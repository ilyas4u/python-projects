mumber=18
nog = 1
print("number off guesses is only limited to 9 times")
while(nog<=9):
    print("guess the number")
    gno = int(input())
    if gno >18:
        print("no entered is greater")
        nog = nog + 1
    elif gno<18:
        print("no entered is lesser")
        nog = nog + 1
    else:
        print("you won")
        print("no of guess you take : ", nog)
        print("no of guess left : ", nog-9)
        break

if nog>9:
    print("game over : you have reached your guess limit")