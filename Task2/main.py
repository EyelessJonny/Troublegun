#A Python program to help troubleshoot mobile device issues automatically with substrings.
__author__ = "Jonny"
__version__ = "0.1"

import sys
import time

class Main:
    """Main class for project; handles everything"""
    def __init__(self):
        print("Welcome to Troublegun Substring v{} made by {}.\n\n\n"
                   "The following question will help shoot your troubles:\n "
                    .format(__version__, __author__))
        self.error = "I'm sorry I didn't understand...\n\n"

    def mainF(self):
        """Questioning functions"""
        keywords = ("Broken", "Crack", "Smash", "", "", "", "", "", "", "", "")
        kindex = 0
        userinput = str.upper(str(input("Please enter your issue:\n")))
        while (str.upper(keywords[kindex]) not in userinput):
            kindex += 1
        if (kindex < 4):
            """Damaged screen"""
            Main.solution(0)
        elif(kindex < 9)
            """"""
        else:


    def solution(self, x):
        """Solutions, parsing exit code"""
        index = int(x)
        sol = open("solutions.txt")
        solutions = sol.readlines()
        print (solutions[index])
        sol.close()
        main.quit()

    def Quit(self):
        """Quit"""
        userinput = str.upper(str(input("If you would like to quit, please type "
                                                                "'Q', or to restart type 'R'.\n")))
        if (userinput == "Q"):
            print ("Troublegun Shutting Down...\n")
            time.sleep(2)
            sys.exit()
        elif (userinput == "R"):
            print ("Troublegun restarting...\n\n")
            main.mainF()
        else:
            print (self.error)
            main.quit()

if __name__ == "__main__":
    main = Main()
    main.mainF()
else:
    print ("Please run Main.py")
