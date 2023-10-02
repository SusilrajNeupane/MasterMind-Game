
import random


class Mastermind:
       # static variable or class variable
    maximum_number_guesses =0
    gamecount = 1                       
    number_of_digits = 3

    def __init__(self):
        pass


    def instructions(self):          # provie instructions
        print("")
        print(f"~~~ GAME INSTRUCTION ~~~")
        print(f"I am thinking of a 3-digit number. Try to guess what it is.")
        print("Here are some clues:")
        print("When I say :\tThat means:")
        print("YELLOW \t\tOne digit is correct but in the wrong position")
        print("GREEN \t\tOne digit is correct and in the right position")
        print("RED \t\tNo digit is correct.")

        print("For example, if the secret number was 346 and your guess was 843, the clues would be Green and Yellow. ")

    def guessCode(self):       # a random number will be generated in range [100,1000) but not three reperation of same number 
        self.num = random.randint(100, 999)
        # self.num = 123                                 # USE OF FIXED NUMBER DURING DEVELOPMENT 
        # print(f"The number is {self.num}")                 ...............................................
        self.digits = []

        while self.num > 0:
            self.digit = self.num % 10
            self.digits.append(self.digit)
            self.num //= 10

        if(self.digits[0] == self.digits[1] and self.digits[1] == self.digits[2]):
            return self.guessCode()
        self.digits1 = self.digits[::-1]
        return self.digits1


    def guessFlagColorAndDisplayRes(self):          # getting number from the user
        isRed = 0
        
        self.condition = False
        for i in range(10):
            print("")
            print("_________")
            print(f"Guess {i+1}:")
            self.userNum = int(input())
            isRed = 0
            if self.userNum in range(100,1000):             # provided number must be in the range of 100 and 999
                pass
            else:
                print("your input must be in between 100 and 999")
                print("Please enter valid value !!!")
                break

            self.userNumDigits = []

            # conversion of given user number into list of single digit number
            while self.userNum>0:
                self.userNumDigit = self.userNum % 10
                self.userNumDigits.append(self.userNumDigit)
                self.userNum //= 10
            self.userNumDigits[::-1]
            self.userNumDigits1 = self.userNumDigits[::-1]


            #  checking the given number is the expected number or not
            for k in range(Mastermind.number_of_digits):
                if self.userNumDigits1[k] in self.digits1:
                    isRed = 0
                    if (self.userNumDigits1[k]==self.digits1[k]):
                        print("Green ",end="")
                    elif(self.userNumDigits1[k]!=self.digits1[k]):
                        print("Yellow ",end="")
                if self.userNumDigits1[k] not in self.digits1:
                    isRed = isRed + 1
                    if (isRed  ==3):
                        print("RED",end="")
                        isRed = 0
                    else:
                        pass
                    
                        



 
                

            if(self.userNumDigits1 == self.digits1):
                print("")
                print(f"You cracked the number on attempt {i+1}.")
                Mastermind.maximum_number_guesses = Mastermind.maximum_number_guesses + i + 1
                print("Do you want to play more?")
                print("1. YES ")
                print("2. NO")
                getOption = input().upper()
                if (getOption=="YES"):
                    Mastermind.gamecount = Mastermind.gamecount +1
                    obj = Mastermind()
                    obj.instructions()
                    obj.guessCode()
                    obj.guessFlagColorAndDisplayRes()
                    break
                    # pass
                elif(getOption=="NO"):
                    print("Thank you for playng...")
                    print("OVERALL RESULTS:")
                    print(f"Total games: {Mastermind.gamecount}")
                    print(f"Total guesses = {Mastermind.maximum_number_guesses}")
                    print(f"Average guesses/game = {float(Mastermind.maximum_number_guesses/Mastermind.gamecount)}")
                    self.condition=True

            if(i==9):
                print("Better luck next time !!")
            if(self.condition):
                break

