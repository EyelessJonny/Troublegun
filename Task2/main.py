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
        damaged = ("BROKEN", "CRACK", "SMASH")
        offnon = ("SLOW", "CRASH", "")
        charge = ("OFF", "", "")
        wet = ("", "", "")
        infected = ("INFECTED", "MALWARE", "AD")
        data = ("", "", "")
        bootloop = ("BOOT", "LOOP", "")
        kindex = 0
        userinput = (input("Please enter your issue:\n")).upper()

        if any(var in userinput for var in damaged):
            main.solution(0)
        elif any(var in userinput for var in offnon):
            main.solution(1)
        elif any(var in userinput for var in charge):
            main.solution(2)
        elif any(var in userinput for var in wet):
            main.solution(3)
        elif any(var in userinput for var in infected):

    def solution(x):
        """Solutions, parsing exit code"""
        index = int(x)
        sol = open("solutions.dat")
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
