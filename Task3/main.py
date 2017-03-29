# A Python program to help troubleshoot mobile device issues
# automatically with device specifics.

import random

class Main:
    """Main class for project; handles everything"""
    def __init__(self):
        print("\n--==[Troublegun Devices for Python 3.6]==--\n\n"
              "The following question will help shoot your troubles:\n")

    def mainF(self):
        """Questioning functions"""
        userinput = (input("Please enter your device's "
                           "brand: e.g. 'Apple'\n> ")).lower()
        r = main.imports(userinput)
        c = main.checkModule(r)
        if (c == True):
            pass
        elif(c == False):
            main.failure(r)
        main.quit()

    def imports(self, userinput):
        global module
        if ("apple" in userinput):
            from Task3.lib import apple as a
            module = a.apple.intro()
            return module
        elif ("samsung" in userinput):
            from Task3.lib import samsung as s
            module = s.samsung.intro()
            return module
        else:
            return userinput

    def checkModule(self, module):
        if (module != None):
            print("Your device is not currently supported...\n")
            return False
        else:
            return True

    def failure(self, x):
        caseno = str(random.random())[2:]
        device = x.upper()
        userinput = str(input("Briefly describe your issue for "
                              "our technicians:\n> "))
        casefile = str("Task3/unsolved/" + caseno + " - " + device + ".dat")
        with open(casefile, "w+") as f:
            f.write(userinput)

    def quit(self):
        """Quit"""
        userinput = (input("If you would like to quit Task 3, please type 'Q', or to "
                           "restart type 'R'.\n> ")).lower()
        if (userinput == "q"):
            print ("Troublegun Task 3 Shutting Down...\n")
            return
        elif (userinput == "r"):
            print ("Troublegun Task 3 Restarting...\n\n")
            main.mainF()
        else:
            print ("I'm sorry I didn't understand...\n\n")
            main.quit()

main = Main()
