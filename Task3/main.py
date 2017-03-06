# A Python program to help troubleshoot mobile device issues
# automatically with device specifics.

__author__ = "Jonny"
__version__ = "0.2"

class Main:
    """Main class for project; handles everything"""
    def __init__(self):
        print("Welcome to Troublegun Devices v{} made by {}.\n\n\n"
              "The following question will help shoot your troubles:\n "
              .format(__version__, __author__))
        self.error = "I'm sorry I didn't understand...\n\n"

    def mainF(self):
        """Questioning functions"""
        userinput = str.lower(str(input("Please enter your device's brand: e.g. 'Apple'\n")))
        try:
            exec("import lib.{}" .format(userinput))
            eval("module = lib.{}.{}.intro()" .format(userinput, userinput))
            if(module != None):
                main.failure(module)
            else:
                main.quit()
        except:
            main.failure()
            main.quit()

    def failure(self, x):
        from datetime import datetime as d
        exitcode = d.date.today() * 1000
        device = x
        print("Your device's manufacturer is not currently supported...\n")
        userinput = str.lower(str(input("Briefly describe your issue for our technicians:\n")))
        exec("error = open('unsolved/{} - {}.dat', 'a+')" .format(caseno, device))

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

if (__name__ == "__main__"):
    main = Main()
    main.mainF()
