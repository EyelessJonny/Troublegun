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
        """Questioning functions"""
        userinput = (input("Please enter your device's brand: e.g. 'Apple'\n> ")
        ).lower()

        if (userinput == "apple"):
            from lib import apple as a
            module = a.apple.intro()
            global module
        elif (userinput == "samsung")
            from lib import samsung as s
            module = s.samsung.intro()
            global module
        else:
            module = userinput

    def support(self):
        if (module != None):
            print("Your device is not currently supported...\n")
            main.failure(module)
        else:

        main.quit()

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
