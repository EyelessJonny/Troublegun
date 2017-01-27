#A Python program to help troubleshoot mobile device issues automatically.
__author__ = "Jonny"
__version__ = "0.10"

from sys import exit
from time import sleep

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

    class Submain(self):
        def __init__(self):
            submain.qos()
        """Questioning class"""
        try:
            def qos(self):
                """What OS?"""
                userinput = str.lower(str(input(self.que[0])))
                if (userinput == "ANDROID"):
                    print ("ANDROID selected!\n")
                    self.os = "Android"
                elif (userinput == "IOS"):
                    print ("IOS selected!\n")
                    self.os = "iOS"
                else:
                    print ("I'm sorry I didn't understand, restarting...\n\n")
                    submain.qos()
                    return
            def qwar(self):
                """Warranty?"""
                userinput = str.lower(str(input(self.que[1])))
                if (userinput == "YES"):
                    print ("YES selected!\n")
                    self.warranty = "In warranty"
                    main.solution(0)
                    return
                elif (userinput == "NO"):
                    print ("NO selected!\n")
                    self.warranty = "Out of warranty"
                    submain.qpow()
                else:
                    print ("I'm sorry I didn't understand, restarting...\n\n")
                    submain.qwar()
                    return
            def qpow():
                """Powered on?"""
                userinput = str.lower(str(input(self.que[2])))
                if (userinput == "YES"):
                    print ("YES selected!\n")
                    self.power = "On"
                    """Turn it off and on?"""
                    userinput = str.lower(str(input(self.que[3])))
                    if (userinput == "YES"):
                        print ("YES selected!\n")
                        submain.qext()
                        return
                    elif (userinput == "NO"):
                        print ("NO selected!\n")
                        main.solution(1)
                        return
                    else:
                        print ("I'm sorry I didn't understand, restarting...\n\n")
                        submain.qpow()
                        return
                elif (userinput == "NO"):
                    print ("NO selected!\n")
                    self.power = "Off"
                    """Charge?"""
                    userinput = str.lower(str(input(self.que[4])))
                    if (userinput == "YES"):
                        print ("YES selected!\n")
                        self.charge = "Charged"
                        submain.qext()
                    elif (userinput == "NO"):
                        print ("NO selected!\n")
                        main.solution(2)
                        return
                    else:
                        print ("I'm sorry I didn't understand, restarting...\n\n")
                        submain.qpow()
                        return
                else:
                    print ("I'm sorry I didn't understand, restarting...\n\n")
                    submain.qpow()
                    return
            def qext():
                """Exterior?"""
                userinput = str.lower(str(input(self.que[5])))
                if (userinput == "YES"):
                    print ("YES selected!\n")
                    self.exterior = "Damaged"
                    """Wet"""
                    userinput = str.lower(str(input(self.que[6])))
                    if (userinput == "YES"):
                        print ("YES selected!\n")
                        main.solution(4) ################
                    elif (userinput == "NO"):
                        print ("NO selected!\n")
                        main.solution(3) ################
                elif (userinput == "NO"):
                    print ("NO selected!\n")
                    self.exterior = "Not damaged"
                    submain.qwre()
                else:
                    print ("I'm sorry I didn't understand, restarting...\n\n")
                    submain.qext()
                    return
            def qwre():
                """Malware?"""
                userinput = str.lower(str(input(self.que[7])))
                if (userinput == "YES"):
                    print ("YES selected!\n")
                    main.solution(5) ################
                elif (userinput == "NO"):
                    print ("NO selected!\n")
                    self.malware = "Not infected"
                    submain.neg()
                else:
                    print ("I'm sorry I didn't understand, restarting...\n\n")
                    submain.qwre()
                    return
            def neg():
                """No problems"""
                print ("Troublegun can't find any troubles to shoot, here is your dump:\n"
                            "Operating System: {}\nWarranty: {}\nPower: {}\nExterior: {}\nMalware: {}\n"
                            .format(self.os, self.warranty, self.power, self.exterior, self.malware))
                return
        except:
            print("Something went wrong, restarting...\n\n")
            submain()

    def solution(self, x):
        index = int(x)
        if(str.lower(self.os) == "IOS"):
            index += 10
        sol = open("solutions.txt")
        solutions = sol.readlines()
        print (solutions[index])
        sol.close()
        quitq = "If you would like to quit, please type 'q', or to restart type 'r'."
        if (str.lower(input(quitQ)) == "q"):
            main.quit()
        elif (str.lower(input(quitQ)) == "r"):
            print ("Troublegun restarting...\n\n")
            submain()
        else:
            print ("I'm sorry I didn't understand, restarting...\n\n")
            submain()

    def start(self):
        """Intialization"""
        submain = Submain()
        subsubmain()

    def quit(self):
        """Quit"""
        print ("Troublegun Shutting Down...\n")
        time.sleep(3)
        sys.exit()

if __name__ == "__main__":
    main = Main()
    main.start()
else:
    print ("Please run Main.py")
