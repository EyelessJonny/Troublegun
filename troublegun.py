# Intro Script

class Troublegun:
    """Main class for project; handles everything"""
    def __init__(self):
        """Constructor"""
        print("Welcome to Troublegun\n")

    def mainF(self):
        """Main function"""
        userinput = input("Please select a task number: '1', '2' or '3'\n> ")
        if (userinput == "1"):
            from Task1 import main
            main.main.mainF()
        elif (userinput == "2"):
            from Task2 import main
            main.main.mainF()
        elif (userinput == "3"):
            from Task3 import main
            main.main.mainF()
        else:
            print("Task {} not found...\n" .format(userinput))

    def quit(self):
        """Quit"""
        userinput = (input("If you would like to quit, please type 'Q', or to "
                           "restart type 'R'.\n> ")).lower()
        if (userinput == "q"):
            print ("Troublegun Shutting Down...\n")
            exit()
        elif (userinput == "r"):
            print ("Troublegun Restarting...\n\n")
            tr.mainF()
        else:
            print ("I'm sorry I didn't understand...\n\n")
            tr.quit()


if (__name__ == "__main__"):
    tg = Troublegun()
    tg.mainF()
    tg.quit()
