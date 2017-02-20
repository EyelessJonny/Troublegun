#A Python program to help troubleshoot mobile device issues automatically with substrings.
__author__ = "Jonny"
__version__ = "0.1"

import sys
import time

class Main:
    """Main class for project; handles everything"""
    def __init__(self):
        print("Welcome to Troublegun Substring v{} made by {}.\n\n\nThe following question"
                   " will help shoot your troubles:\n " .format(__version__, __author__))
        self.error = "I'm sorry I didn't understand...\n\n"

    def mainF(self):
        """Questioning functions"""
        keywords =("", "", "", "")
        userinput = str.upper(str(input("Please enter your issue:")))
        if (keywords in userinput):
            print("Yes")

    def solution(self, x):
        index = int(x)wdasd
        """Quit"""
        userinput = str.upper(str(input("If you would like to quit, please type "
                                                                "'q', or to restart type 'r'.\n")))
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
