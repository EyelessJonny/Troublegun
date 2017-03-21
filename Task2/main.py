# A Python program to help troubleshoot mobile device issues
# automatically with substrings.
import time

class Main:
    """Main class for project; handles everything"""
    def __init__(self):
        print("--==[Troublegun Susbstring for Python 3.6]==--\n\n\n"
              "The following question will help shoot your troubles:\n")
        self.error = "I'm sorry I didn't understand...\n\n"

    def mainF(self):
        """Questioning functions"""
        damaged = ("Broken", "Crack", "Smash", "Slow", "Crash", "",
                    "", "", "", "", "")
        kindex = 0
        userinput = (input("Please enter your issue:\n")).upper()
        if (userinput in any(damaged)):
            print("Yes")
        else:
            print(self.error)
            main.MainF()
#        try:
#            damaged = ("Broken", "Crack", "Smash", "Slow", "Crash", "",
#                        "", "", "", "", "")
#            kindex = 0
#            userinput = (input("Please enter your issue:\n")).upper()
#            if (any(damaged) in userinput):
#                print("Yes")
#            else:
#                print(self.error)
#                main.MainF()
#        except:
#            print("Someting went wrong...\n\n")
#            main.quit()

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
        userinput = (input("If you would like to quit, please type "
                            "'Q', or to restart type 'R'.\n")).upper()
        if (userinput == "Q"):
            print ("Troublegun Shutting Down...\n")
            time.sleep(1)
            exit()
        elif (userinput == "R"):
            print ("Troublegun Restarting...\n\n")
            main.mainF()
        else:
            print (self.error)
            main.quit()

if (__name__ == "__main__"):
    main = Main()
    main.mainF()
else:
    print ("Please run Main.py")
