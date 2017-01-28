#A Python program to help troubleshoot mobile device issues automatically.
__author__ = "Jonny"
__version__ = "0.11"

import sys
import time

class Main:
    """Main class for project; handles everything."""
    def __init__(self):
        print("Welcome to Troublegun v{} made by {}.\n\n\nThe following questions"
                   " will help shoot your troubles:\n " .format(__version__, __author__))
        self.que = ("What operating system does your mobile device use: 'ANDROID', "
                              "OR 'IOS'.\n",
                              "Is your device under warranty? 'YES' or 'NO'\n",
                              "Can your mobile device be powered on? 'YES' or 'NO'.\n",
                              "Have you turned your mobile device off and on again? 'YES' or 'NO' \n",
                              "Has your device's battery been charged? 'YES' or 'NO'\n",
                              "Is your device's exterior damaged? 'YES' or'NO'\n",
                              "Is your device wet? 'YES' or 'NO'\n",
                              "Is your device infected with malware? 'YES' or 'NO'\n")
        self.os = str
        self.warranty = str
        self.power = str
        self.charge = str
        self.exterior = str
        self.malware = str

    def mainF(self):
        """Questioning functions"""
        try:
            def qos(self):
                """What OS?"""
                userinput = str.upper(str(input(self.que[0])))
                if (userinput == "ANDROID"):
                    print ("ANDROID selected!\n")
                    self.os = "Android"
                    qwar(self)
                elif (userinput == "IOS"):
                    print ("IOS selected!\n")
                    self.os = "iOS"
                    qwar(self)
                else:
                    print ("I'm sorry I didn't understand, restarting question...\n\n")
                    qos(self)
                    return

            def qwar(self):
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
                    qpow(self)
                else:
                    print ("I'm sorry I didn't understand, restarting question...\n\n")
                    qwar(self)
                    return

            def qpow(self):
                """Powered on?"""
                userinput = str.upper(str(input(self.que[2])))
                if (userinput == "YES"):
                    print ("YES selected!\n")
                    self.power = "On"
                    """Turn it off and on?"""
                    userinput = str.upper(str(input(self.que[3])))
                    if (userinput == "YES"):
                        print ("YES selected!\n")
                        qext(self)
                        return
                    elif (userinput == "NO"):
                        print ("NO selected!\n")
                        main.solution(1)
                        return
                    else:
                        print ("I'm sorry I didn't understand, restarting question...\n\n")
                        qpow(self)
                        return
                elif (userinput == "NO"):
                    print ("NO selected!\n")
                    self.power = "Off"
                    """Charge?"""
                    userinput = str.upper(str(input(self.que[4])))
                    if (userinput == "YES"):
                        print ("YES selected!\n")
                        self.charge = "Charged"
                        qext(self)
                    elif (userinput == "NO"):
                        print ("NO selected!\n")
                        main.solution(2)
                        return
                    else:
                        print ("I'm sorry I didn't understand, restarting question...\n\n")
                        qpow(self)
                        return
                else:
                    print ("I'm sorry I didn't understand, restarting question...\n\n")
                    qpow(self)
                    return

            def qext(self):
                """Exterior?"""
                userinput = str.upper(str(input(self.que[5])))
                if (userinput == "YES"):
                    print ("YES selected!\n")
                    self.exterior = "Damaged"
                    """Wet"""
                    userinput = str.upper(str(input(self.que[6])))
                    if (userinput == "YES"):
                        print ("YES selected!\n")
                        main.solution(4)
                    elif (userinput == "NO"):
                        print ("NO selected!\n")
                        main.solution(3)
                elif (userinput == "NO"):
                    print ("NO selected!\n")
                    self.exterior = "Not damaged"
                    qwre(self)
                else:
                    print ("I'm sorry I didn't understand, restarting question...\n\n")
                    qext(self)
                    return

            def qwre(self):
                """Malware?"""
                userinput = str.upper(str(input(self.que[7])))
                if (userinput == "YES"):
                    print ("YES selected!\n")
                    main.solution(5)
                elif (userinput == "NO"):
                    print ("NO selected!\n")
                    self.malware = "Not infected"
                    neg(self)
                else:
                    print ("I'm sorry I didn't understand, restarting question...\n\n")
                    qwre(self)
                    return

            def neg(self):
                """No problems"""
                print ("Troublegun can't find any troubles to shoot, here is your dump:\n"
                       "Operating System: {}\nWarranty: {}\nPower: {}\nExterior: {}\nMalware: {}\n"
                       .format(self.os, self.warranty, self.power, self.exterior, self.malware))
                main.quit()
        except:
            print("Something went wrong, restarting...\n\n")
            main()
        qos(self)

    def solution(self, x):
        index = int(x)
        if(str.upper(self.os) == "IOS"):
            index += 10
        sol = open("solutions.txt")
        solutions = sol.readlines()
        print (solutions[index])
        sol.close()
        main.quit()

    def quit(self):
        """Quit"""
        userinput = str.upper(input("If you would like to quit, please type "
                                                                "'q', or to restart type 'r'.\n"))
        if (userinput == "Q"):
            print ("Troublegun Shutting Down...\n")
            time.sleep(2)
            sys.exit()
        elif (userinput == "R"):
            print ("Troublegun restarting...\n\n")
            main.mainF()
        else:
            print ("I'm sorry I didn't understand...\n\n")
            main.quit()

if __name__ == "__main__":
    main = Main()
    main.mainF()
else:
    print ("Please run Main.py")
