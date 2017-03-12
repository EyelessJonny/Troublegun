# A Python program to help troubleshoot mobile device issues
# automatically with device specifics.

import datetime, random, time

class Main:
    """Main class for project; handles everything"""
    def __init__(self):
        print("Welcome to Troublegun Devices made by Jonny.\n\n\n"
              "The following question will help shoot your troubles:\n")
        self.error = "I'm sorry I didn't understand...\n\n"

    def mainF(self):
        """Questioning functions
        userinput = (input("Please enter your device's brand: e.g. 'Apple'\n> ")
        ).lower()
        try:
            module = None
            exec("from lib import {}" .format(userinput))
            exec("module = {}.{}.intro()" .format(userinput, userinput))
            if (module != None):
                print("1")
                #print("Your device is not currently supported...\n")
                #main.failure(module)
            else:
                print("2")
                #main.quit()
        except Exception as e:
            print("Something went wrong, error [{}]\n\n" .format(e))
            if (module != None):
                print("3")
                print("Your device is not currently supported...\n")
                main.failure(module)
            else:
                print("4")
                print("Your device's manufacturer is not currently "
                      "supported...\n")
                main.failure(userinput)
        main.quit"""

        userinput = (input("Please enter a module to test:\n> ")).lower()
        try:
            module = None
            exec("from lib import {}" .format(userinput))
            exec("module = {}.{}.intro()" .format(userinput, userinput))
            if(module != None):
                print("1")
            else:
                print("2")
        except Exception as e:
            print("Something went wrong, error [{}]\n\n" .format(e))
            if (module != None):
                print("3" )
            else:
                print("4")

    def failure(self, x):
        caseno = str(random.random())[2:]
        device = x.upper()
        userinput = str(input("Briefly describe your issue for our technicians:"
                              "\n> "))
        casefile = str("unsolved/" + caseno + " - " + device + ".dat")
        with open(casefile, "w+") as f:
            f.write(userinput)

    def quit(self):
        """Quit"""
        userinput = (input("If you would like to quit, please type 'Q', or to "
                           "restart type 'R'.\n> ")).lower()
        if (userinput == "q"):
            print ("Troublegun Shutting Down...\n")
            exit()
        elif (userinput == "r"):
            print ("Troublegun Restarting...\n\n")
            main.mainF()
        else:
            print (self.error)
            main.quit()

if (__name__ == "__main__"):
    main = Main()
    main.mainF()
