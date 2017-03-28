# A Python program to help troubleshoot mobile device issues
# automatically with substrings.
import time

class Main:
    """Main class for project; handles everything"""
    def __init__(self):
        print("--==[Troublegun Susbstring for Python 3.6]==--\n\n\n"
              "The following question will help shoot your troubles:\n")

    def mainF(self):
        """Questioning functions"""
        damaged = ("BROKEN", "CRACK", "SMASH")
        offnon = ("SLOW", "CRASH")
        charge = ("OFF", "POWER", "TURN")
        wet = ("WET", "WATER")
        infected = ("INFECTED", "MALWARE", "AD")
        data = ("CORRUPT", "GONE", "WIPE")
        bootloop = ("BOOT", "LOOP")
        kindex = 0
        userinput = (input("Please enter your issue:\n> ")).upper()

        if any(var in userinput for var in damaged):
            main.solution(0)
        elif any(var in userinput for var in offnon):
            main.solution(1)
        elif any(var in userinput for var in charge):
            main.solution(2)
        elif any(var in userinput for var in wet):
            main.solution(3)
        elif any(var in userinput for var in infected):
            main.solution(4)
        elif any(var in userinput for var in data):
            main.solution(5)
        elif any(var in userinput for var in bootloop):
            main.solution(6)
        else:
            print("I could not interpret your problem.\n")
            main.quit()

    def solution(self, x):
        """Solutions, parsing exit code"""
        index = int(x)
        with open("solutions.dat") as f:
            solutions = f.readlines()
            print (solutions[index])
        main.quit()

    def quit(self):
        """Quit"""
        userinput = (input("If you would like to quit, please type "
                            "'Q', or to restart type 'R'.\n> ")).upper()
        if (userinput == "Q"):
            print ("Troublegun Shutting Down...\n")
            time.sleep(1)
            exit()
        elif (userinput == "R"):
            print ("Troublegun Restarting...\n\n")
            main.mainF()
        else:
            print ("I'm sorry I didn't understand...\n\n")
            main.quit()

if (__name__ == "__main__"):
    main = Main()
    main.mainF()
else:
    print ("Please run Main.py")
