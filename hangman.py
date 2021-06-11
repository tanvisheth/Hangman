import random

def hangman():
    words = open('animal.txt').read().splitlines()
    word =random.choice(words)
    word=word.lower()
    validLetter='abcdefghijklmnopqrstuvwxyz'
    turns=10
    guessmade=''

    while len(word)>0:
        main=""
        missed=0

        for letter in word:
            if letter in guessmade:
                main=main+letter
            else:
                main=main +"_"+ " "
        if main == word:
            print(main)
            print(" Congrats you had guess the correct word ")
            break

        print(" Guess the word : ",main)
        guess=input()

        if guess in validLetter:
            guessmade=guessmade+guess
        else:
            print(" Enter valid Character ")

        if guess not in word:
            turns=turns-1

            if turns==9:
                print(" OOPS!!! Try to guess again 9 chance left ")
                print(" ------------------ ")
            if turns==8:
                print(" OOPS!!! Try to guess again 8 chance left ")
                print(" ------------------ ")
                print("         O          ")
            if turns==7:
                print(" OOPS!!! Try to guess again 7 chance left ")
                print(" ------------------ ")
                print("         O          ")
                print("         |          ")
            if turns==6:
                print(" OOPS!!! Try to guess again 6 chance left ")
                print(" ------------------ ")
                print("         O          ")
                print("         |          ")
                print("        /           ")
            if turns==5:
                print(" OOPS!!! Try to guess again 5 chance left ")
                print(" ------------------ ")
                print("         O          ")
                print("         |          ")
                print("        / \         ")
            if turns == 4:
                print(" OOPS!!! Try to guess again 4 chance left ")
                print(" ------------------ ")
                print("       \ O          ")
                print("         |          ")
                print("        / \         ")
            if turns == 3:
                print(" OOPS!!! Try to guess again 3 chance left ")
                print(" ------------------ ")
                print("      \  O  /       ")
                print("         |          ")
                print("        / \         ")
            if turns == 2:
                print(" OOPS!!! Try to guess again 2 chance left ")
                print(" ------------------ ")
                print("      \  O  / |     ")
                print("         |          ")
                print("        / \         ")
            if turns == 1:
                print(" OOPS!!! Try to guess again 1 chance left ")
                print(" Last breaths counting, Take care! ")
                print(" ------------------ ")
                print("      \  O_| /      ")
                print("         |          ")
                print("        / \         ")
            if turns == 0:
                print(" OOPS!!! You can't guess the word ")
                print(" You let a kind man die ")
                print(" ------------------ ")
                print("         O_|       ")
                print("        /|\         ")
                print("        / \         ")
                break

while True:
    name=input(" Enter your name ")
    print(" Welcome ",name)
    print(" ------------------- ")
    print(" Try to guess animal name in less than 10 trys ")
    hangman()
    print()
    answer=input(" Do you want to try your luck once again?? (y/n) ")
    if answer !="y":
        break
