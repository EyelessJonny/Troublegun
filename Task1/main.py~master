#A Python program to help troubleshoot mobile device issues automatically.
__author__ = "Jonny"
__version__ = "1.0"

class Main:
    """Main class for project; handles everything"""
    def __init__(self):
        print("Welcome to Troublegun Flowchart v{} made by {}.\n\n\n"
                   "The following questions  will help shoot your troubles:\n "
                    .format(__version__, __author__))
        self.error = "I'm sorry I didn't understand...\n\n"
        self.que = ("What operating system does your mobile device use: 'ANDROID', "
                              "OR 'IOS'.\n",
                              "Is your device under warranty? 'YES' or 'NO'\n",
                              "Can your mobile device be powered on? 'YES' or 'NO'.\n",
                              "Have you turned your mobile device off and on again? 'YES' or 'NO' \n",
                              "Has your device's battery been charged? 'YES' or 'NO'\n",
                              "Is your device's exterior damaged? 'YES' or'NO'\n",
                              "Is your device wet? 'YES' or 'NO'\n",
                              "Is your device infected with malware? 'YES' or 'NO'\n",
                              "Is your device boot-looping? 'YES' or 'NO'\n")
        self.os = str
        self.warranty = str
        self.power = str
        self.exterior = str
        self.malware = str

        userinput = input("Is your phone screen cracked?")
        print (userinput)

    def mainF(self):
        """Questioning functions"""
        try:
            def qos(self):
                """What OS?"""
                userinput = str.upper(str(input(self.que[0])))
                if (userinput == "ANDROID") or (userinput == "A"):
                    print ("ANDROID selected!\n")
                    self.os = "Android"
                    qwar(self)
                elif (userinput == "IOS") or (userinput == "I"):
                    print ("IOS selected!\n")
                    self.os = "iOS"
                    qwar(self)
                else:
                    print (self.error)
                    qos(self)

            def qwar(self):
                """Warranty?"""
                userinput = str.upper(str(input(self.que[1])))
                if (userinput == "YES") or (userinput == "Y"):
                    print ("YES selected!\n")
                    self.warranty = "In warranty"
                    main.solution(0)
                elif (userinput == "NO") or (userinput == "N"):
                    print ("NO selected!\n")
                    self.warranty = "Out of warranty"
                    qpow(self)
                else:
                    print (self.error)
                    qwar(self)

            def qpow(self):
                """Powered on?"""
                userinput = str.upper(str(input(self.que[2])))
                if (userinput == "YES") or (userinput == "Y"):
                    print ("YES selected!\n")
                    self.power = "On"
                    """Turn it off and on?"""
                    userinput = str.upper(str(input(self.que[3])))
                    if (userinput == "YES") or (userinput == "Y"):
                        print ("YES selected!\n")
                        qext(self)
                    elif (userinput == "NO") or (userinput == "N"):
                        print ("NO selected!\n")
                        main.solution(1)
                    else:
                        print (self.error)
                        qpow(self)
                elif (userinput == "NO") or (userinput == "N"):
                    print ("NO selected!\n")
                    self.power = "Off"
                    """Charge?"""
                    userinput = str.upper(str(input(self.que[4])))
                    if (userinput == "YES") or (userinput == "Y"):
                        print ("YES selected!\n")
                        """Boot-loop?"""
                        userinput = str.upper(str(input(self.que[8])))
                        if (userinput == "YES") or (userinput == "Y"):
                            print ("YES selected!\n")
                            main.solution(8)
                        elif (userinput == "NO") or (userinput == "N"):
                            print ("NO selected!\n")
                            main.solution(7)
                        else:
                            print (self.error)
                            qpow(self)
                    elif (userinput == "NO") or (userinput == "N"):
                        print ("NO selected!\n")
                        main.solution(2)
                    else:
                        print (self.error)
                        qpow(self)
                else:
                    print (self.error)
                    qpow(self)

            def qext(self):
                """Exterior?"""
                userinput = str.upper(str(input(self.que[5])))
                if (userinput == "YES") or (userinput == "Y"):
                    print ("YES selected!\n")
                    self.exterior = "Damaged"
                    """Wet"""
                    userinput = str.upper(str(input(self.que[6])))
                    if (userinput == "YES") or (userinput == "Y"):
                        print ("YES selected!\n")
                        main.solution(4)
                    elif (userinput == "NO") or (userinput == "N"):
                        print ("NO selected!\n")
                        main.solution(3)
                    else:
                        print (self.error)
                        qext(self)
                elif (userinput == "NO") or (userinput == "N"):
                    print ("NO selected!\n")
                    self.exterior = "Not damaged"
                    qwre(self)
                else:
                    print (self.error)
                    qext(self)

            def qwre(self):
                """Malware?"""
                userinput = str.upper(str(input(self.que[7])))
                if (userinput == "YES") or (userinput == "Y"):
                    print ("YES selected!\n")
                    main.solution(5)
                elif (userinput == "NO") or (userinput == "N"):
                    print ("NO selected!\n")
                    self.malware = "Not infected"
                    neg(self)
                else:
                    print (self.error)
                    qwre(self)

            def neg(self):
                """No problems"""
                print ("Troublegun can't find any troubles to shoot, here is your dump:\n"
                       "Operating System: {}\nWarranty: {}\nPower: {}\nExterior: {}\nMalware: {}\n"
                       .format(self.os, self.warranty, self.power, self.exterior, self.malware))
                main.quit()
        except:
            print("Something went wrong\n\n")
            main.quit()
        qos(self)

    def solution(self, x):
        """Solutions, parsing exit code"""
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
        from sys import exit as brexit
        from time import sleep as PMQs
        userinput = str.upper(input("If you would like to quit, please type "
                                                                "'Q', or to restart type 'R'.\n"))
        if (userinput == "Q"):
            print ("Troublegun Shutting Down...\n")
            PMQs(2)
            brexit()
        elif (userinput == "R"):
            print ("Troublegun restarting...\n\n")
            main.mainF()
        else:
            print (self.error)
            main.quit()

if __name__ == "__main__":
    main = Main()
    main.mainF()
