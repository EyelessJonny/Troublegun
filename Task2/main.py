# A Python program to help troubleshoot mobile device issues
# automatically with substrings.


class Main:
    """Main class for task; handles everything"""
    def __init__(self):
        print("\n--==[Troublegun Task 2 for Python 3.6]==--\n\n"
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
        userinput = (input("Please enter your issue:\n> ")).upper()

        if any(i in userinput for i in damaged):
            main.solution(0)
        elif any(i in userinput for i in offnon):
            main.solution(1)
        elif any(i in userinput for i in charge):
            main.solution(2)
        elif any(i in userinput for i in wet):
            main.solution(3)
        elif any(i in userinput for i in infected):
            main.solution(4)
        elif any(i in userinput for i in data):
            main.solution(5)
        elif any(i in userinput for i in bootloop):
            main.solution(6)
        else:
            print("I could not interpret your problem.\n")
            main.quit()

    def solution(self, x):
        """Solutions, parsing exit code"""
        index = int(x)
        with open("Task2/solutions.dat") as f:
            solutions = f.readlines()
            print (solutions[index])
        main.quit()

    def quit(self):
        """Quit"""
        userinput = (input("If you would like to quit Task 2, please type "
                            "'Q', or to restart type 'R'.\n> ")).upper()
        if (userinput == "Q"):
            print ("Troublegun Task 2 Shutting Down...\n")
            return
        elif (userinput == "R"):
            print ("Troublegun Task 2 Restarting...\n\n")
            main.mainF()
        else:
            print ("I'm sorry I didn't understand...\n\n")
            main.quit()

main = Main()
