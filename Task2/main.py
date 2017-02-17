# A Python program to help troubleshoot mobile device issues
# automatically with substrings.
__author__ = "Jonny"
__version__ = "0.1"

class Main:
    """Main class for project; handles everything"""
    def __init__(self):
        print("Welcome to Troublegun Substring v{} made by {}.\n\n\n"
                   "The following question will help shoot your troubles:\n "
                    .format(__version__, __author__))
        self.error = "I'm sorry I didn't understand...\n\n"

    def mainF(self):
        """Questioning functions"""
        keywords = ("Broken", "Crack", "Smash", "Slow", "Crash", "", "", "", "", "", "")
        kindex = 0
        userinput = str.upper(str(input("Please enter your issue:\n")))
        while (str.upper(keywords[kindex]) not in userinput):
            kindex += 1
        if (kindex < 2):
            """Damaged"""
            Main.solution(0)
        elif(kindex < 9):
            """Off and on"""
        else:
            print (self.error)
            main.MainF()

    def solution(x):
        """Solutions, parsing exit code"""
        index = int(x)
        sol = open("solutions.txt")
        solutions = sol.readlines()
        print (solutions[index])
        sol.close()
        main.quit()

    def quit(self):
        """Quit"""
        from sys import exit as ex
        from time import sleep as sl
        userinput = str.upper(str(input("If you would like to quit, please type "
                                                                     "'Q', or to restart type 'R'.\n")))
        if (userinput == "Q"):
            print ("Troublegun Shutting Down...\n")
            sl(2)
            ex()
        elif (userinput == "R"):
            print ("Troublegun Restarting...\n\n")
            main.mainF()
        else:
            print (self.error)
            main.quit()

if __name__ == "__main__":
    main = Main()
    main.mainF()
