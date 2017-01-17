#A Python program to help troubleshoot mobile device issues automatically.
__author__ = "Jonny"
__version__ = "0.01"

from sys import exit
from time import sleep

class Main:
    """Main class for project; handles everything."""
    def __init__(self):
        self.que = ("What operating system does your mobile device use: 'ANDROID', "
                              "OR 'IOS'.\n",
                              "Is your device under warranty? 'YES' or 'NO'\n",
                              "Can your mobile device be powered on? 'YES' or 'NO'.\n",
                              "Have you turned your mobile device off and on again? 'YES' or 'NO' \n",
                              "Has your device's battery been charged? 'YES' or 'NO'\n",
                              "Is your device's exterior damaged? 'YES' or'NO'\n",
                              "Is your device infected with malware?\n",
                              "\n")
        self.os = str
        self.warranty = str
        self.turned_on = bool
        self.exterior = str

    def welcome(self):
        print("Welcome to Troublegun v{} made by {}.\n\n\nThe following questions"
                   " will help shoot your troubles:\n " .format(__version__, __author__))

    def mainF(self):
        try:
            """What OS?"""
            userinput = str.upper(str(input(self.que[0])))
            if (userinput == "ANDROID"):
                print ("ANDROID selected!\n")
                self.os = "Android"
            elif (userinput == "IOS"):
                print ("IOS selected!\n")
                self.os = "iOS"
            else:
                print ("I'm sorry I didn't understand, restarting...\n\n")
                main.mainF()
                return
            """Warranty?"""
            userinput = str.upper(str(input(self.que[1])))
            if (userinput == "YES"):
                print ("YES selected!\n")
                self.warranty = "In warranty"
                main.solution(0)
                return
            elif (userinput == "NO"):
                print ("NO selected!\n")
                self.warranty = "Out of warranty"
            else:
                print ("I'm sorry I didn't understand, restarting...\n\n")
                main.mainF()
                return
            """Powered on?"""
            userinput = str.upper(str(input(self.que[2])))
            if (userinput == "YES"):
                print ("YES selected!\n")
                self.turned_on = True
                """Turn it off and on?"""
                userinput = str.upper(str(input(self.que[3])))
                if (userinput == "YES"):
                    print ("YES selected!\n")
                elif (userinput == "NO"):
                    print ("NO selected!\n")
                    main.solution(1)
                    return
                else:
                    print ("I'm sorry I didn't understand, restarting...\n\n")
                    main.mainF()
                    return
            elif (userinput == "NO"):
                print ("NO selected!\n")
                self.turned_on = False
                """Charge?"""
                userinput = str.upper(str(input(self.que[4])))
                if (userinput == "YES"):
                    print ("YES selected!\n")
                elif (userinput == "NO"):
                    print ("NO selected!\n")
                    main.solution(2)
                    return
                else:
                    print ("I'm sorry I didn't understand, restarting...\n\n")
                    main.mainF()
                    return
            else:
                print ("I'm sorry I didn't understand, restarting...\n\n")
                main.mainF()
                return
            """Exterior?"""
            userinput = str.upper(str(input(self.que[5])))
            if (userinput == "YES"):
                print ("YES selected!\n")
                self.exterior = "Damaged"
                main.solution(3)
                return
            elif (userinput == "NO"):
                print ("NO selected!\n")
                self.exterior = "Not damaged"
            else:
                print ("I'm sorry I didn't understand, restarting...\n\n")
                main.mainF()
                return
            """No problems"""
            print ("Troublegun can't find any troubles to shoot, here is your dump:\n"
                        "Operating System: {}\nWarranty: ")
        except:
            print("Something went wrong, restarting...\n\n")
            main.MainF()

    def solution(self, x):
        index = int(x)
        if(self.os == "ios"):
            index += 10
        sol = open("solutions.txt")
        solutions = sol.readlines()
        print (solutions[index])
        sol.close()

    def start(self):
        main.welcome()
        main.mainF()

    def quit(self):
        print ("Troublegun Shutting Down...\n")
        time.sleep(3)
        sys.exit()

if __name__ == "__main__":
    main = Main()
    main.start()
else:
    print ("Please run Main.py")
