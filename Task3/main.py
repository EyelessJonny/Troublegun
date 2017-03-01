# A Python program to help troubleshoot mobile device issues
# automatically with device specifics.

__author__ = "Jonny"
__version__ = "0.1"

class Main:
    """Main class for project; handles everything"""
    def __init__(self):
        print("Welcome to Troublegun Devices v{} made by {}.\n\n\n"
                   "The following question will help shoot your troubles:\n "
                    .format(__version__, __author__))
        self.error = "I'm sorry I didn't understand...\n\n"

    def mainF(self):
        """Questioning functions"""
        userinput = str.lower(str(input("Please enter your decive's brand: e.g. 'Apple'\n")))
        try:
            solution = __import__(userinput)
            main.quit()
        except:
            print("Your device's manufacturer is not currently supported...\n")
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
