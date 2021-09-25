#
#Python: 3.7.8
#
#Author: Ryan Spears
#

def start(nice = 0,mean = 0,name = ""):
    #Get user's name.
    name = describeGame(name)
    nice,mean,name = niceMean(nice, mean, name)

def describeGame(name):
    if name != "":
        print("\nThank you for playing agian, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean, ")
                    print("but at the end of the game your fate \nwill be sealed by your actions...")
                    stop = False

    return name

def niceMean(nice, mean, name):
    stop = True
    while stop:
        showScore(nice, mean, name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice or mean? (N/M) \n>>>:").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you and storms off...")
            mean = (mean + 1)
            stop = False
        #This is my customization. If the player types anything other than N or M, they get this message.    
        else:
            print("\nCan you not read, {}? It clearly says type ( N ) for 'NICE', \nand ( M ) for 'MEAN'.".format(name))
    score(nice, mean, name)

def showScore(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))

def score(nice, mean, name):
    if nice > 2:
        win(nice, mean, name)
    if mean > 2:
        lose(nice, mean, name)
    else:
        niceMean(nice, mean, name)

def win(nice, mean, name):
    print("\nNice job, {}! You win! \nEveryone loves you, and you made \nlots of friends along the way!".format(name))
    again(nice, mean, name)

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (Y/N):\n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("\nOh well...sorry to see you go.")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', and ( N ) for 'NO':\n>>>")

def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)

def lose(nice, mean, name):
    print("\nBruh...How did you lose? Too bad! XD \n{}, you probably aren't very good at games if you lost this.".format(name))
    again(nice, mean, name)

if __name__ == "__main__":
    start()

    

