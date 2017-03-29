# A Python program to help troubleshoot mobile device issues automatically.


class Main:
    """Main class for project; handles everything"""
    def __init__(self):
        print("\n--==[Troublegun Task 1 for Python 3.6]==--\n\n"
              "The following questions will help shoot your troubles:\n")
        self.error = "I'm sorry I didn't understand...\n\n"
        self.que = ("What operating system does your mobile device use: 'ANDROID', "
                    "OR 'IOS'.\n> ",
                    "Is your device under warranty? 'YES' or 'NO'\n> ",
                    "Can your mobile device be powered on? 'YES' or 'NO'\n> ",
                    "Have you turned your mobile device off and on again? 'YES' or 'NO'\n> ",
                    "Has your device's battery been charged? 'YES' or 'NO'\n> ",
                    "Is your device's exterior damaged? 'YES' or'NO'\n> ",
                    "Is your device wet? 'YES' or 'NO'\n> ",
                    "Is your device infected with malware? 'YES' or 'NO'\n> ",
                    "Is your device boot-looping? 'YES' or 'NO'\n> ")
        self.os       = str
        self.warranty = str
        self.power    = str
        self.exterior = str
        self.malware  = str

    def mainF(self):
        """Questioning functions"""
        try:
            def qos(self):
                """What OS?"""
                userinput = (input(self.que[0])).upper()
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
                userinput = (input(self.que[1])).upper()
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
                userinput = (input(self.que[2])).upper()
                if (userinput == "YES") or (userinput == "Y"):
                    print ("YES selected!\n")
                    self.power = "On"
                    """Turn it off and on?"""
                    userinput = (input(self.que[3])).upper()
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
                    userinput = (input(self.que[4])).upper()
                    if (userinput == "YES") or (userinput == "Y"):
                        print ("YES selected!\n")
                        """Boot-loop?"""
                        userinput = (input(self.que[8])).upper()
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
                userinput = (input(self.que[5])).upper()
                if (userinput == "YES") or (userinput == "Y"):
                    print ("YES selected!\n")
                    self.exterior = "Damaged"
                    """Wet"""
                    userinput = (input(self.que[6])).upper()
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
                userinput = (input(self.que[7])).upper()
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
                print ("Troublegun can't find any troubles to shoot, here is "
                       "your dump:\n Operating System: {}\nWarranty: {}\nPower:"
                       " {}\nExterior: {}\nOperating System: {}\n{}\nMalware: {}\n"
                       .format(self.os, self.warranty, self.power, self.exterior,
                       self.malware))
                main.quit()
        except Exception as e:
            print("Something went wrong, error [{}]\n\n" .format(e))
            main.quit()
        qos(self)

    def solution(self, x):
        """Solutions, parsing exit code"""
        index = int(x)
        if (self.os == "iOS"):
            index += 10
        with open("Task1/solutions.dat") as f:
            solutions = f.readlines()
            print (solutions[index])
        main.quit()

    def quit(self):
        """Quit"""
        userinput = (input("If you would like to quit Task 1, please type "
                           "'Q', or to restart type 'R'.\n> ")).upper()
        if (userinput == "Q"):
            print ("Troublegun Task 1 Shutting Down...\n")
            return
        elif (userinput == "R"):
            print ("Troublegun Task 1 Restarting...\n\n")
            main.mainF()
        else:
            print (self.error)
            main.quit()
            
main = Main()
