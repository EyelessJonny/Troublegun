# A Python program to help troubleshoot mobile device issues
# automatically with device specifics.

import random, time, lib

class Main:
    """Main class for project; handles everything"""
    def __init__(self):
        print("Welcome to Troublegun Devices for Python 3.6\n\n\n"
              "The following question will help shoot your troubles:\n")
        self.error = "I'm sorry I didn't understand...\n\n"

    def mainF(self):
        """Questioning functions"""
        userinput = (input("Please enter your device's brand: e.g. 'Apple'\n> ")
        ).lower()
        try:
            obj = main.apple()
            if (obj != None):
                print("1")
                print("Your device is not currently supported...\n")
                main.failure(obj)
            else:
                print("2")
        except Exception as e:
            print("Something went wrong, error [{}]\n\n" .format(e))
            if (obj != None):
                print("3")
                print("Your device is not currently supported...\n")
                main.failure(obj)
            else:
                print("4")
                print("Your device's manufacturer is not currently "
                      "supported...\n")
                main.failure(userinput)
        main.quit()

    def apple(self):
        """Selection function"""
        print ("Troublegun Apple Initialized...")
        userinput = (input("What model of Apple device do you have? e.g. "
                           "'iPhone 7 Plus\n> ")).upper()
        x = userinput
        if("IPHONE" in x) and ("7" in x) and ("PLUS" in x):
            version = "sevenplus"
        elif("IPHONE" in x) and ("7" in x) and ("PLUS" not in x):
            version = "seven"
        elif("IPHONE" in x) and ("6" in x) and ("S" in x) and ("PLUS" in x):
            version = "sixsplus"
        elif("IPHONE" in x) and ("6" in x) and ("S" in x) and ("PLUS" not in x):
            version = "sixs"
        elif("IPHONE" in x) and ("SE" in x):
            version = "se"
        else:
            return userinput
        exec("import lib.models.iphone.{}" .format(version))

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
