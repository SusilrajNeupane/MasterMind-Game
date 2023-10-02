
# importing Mastermind from gameContent on gameContent
from gameContent import Mastermind



def intro():
    print("")
    print("")
    print(f"~~~ Welcome to Mastermind Game ~~~")
    print("")
    print(f"Hi gamer , welcome to the Mastermind game")
    name = input("What is your name: ")
    print("")
    print(f'Hello,{name}, Please follow the given instructions to play the game.')

intro()
def playGame():

    

    obj = Mastermind()
    # obj.intro()
    obj.instructions()
    obj.guessCode()
    obj.guessFlagColorAndDisplayRes()



playGame()