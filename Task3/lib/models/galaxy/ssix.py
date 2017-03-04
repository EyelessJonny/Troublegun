# Galaxy S6 module

__author__ = "Jonny"
__version__ = "1.0"

class Main:
    """Main class for project; handles everything"""
    def __init__(self):
        print("Galaxy S6 Selected\n\n")
        self.error = "I'm sorry I didn't understand...\n\n"
        self.que = ("",
                              "Is your Galaxy S6 under warranty? 'YES' or 'NO'\n",
                              "Can your Galaxy S6 be powered on? 'YES' or 'NO'.\n",
                              "Have you turned your Galaxy S6 off and on again? 'YES' or 'NO' \n",
                              "Has your Galaxy S6's battery been charged? 'YES' or 'NO'\n",
                              "Is your Galaxy S6's exterior damaged? 'YES' or'NO'\n",
                              "Is your Galaxy S6 wet? 'YES' or 'NO'\n",
                              "Is your Galaxy S6 infected with malware? 'YES' or 'NO'\n",
                              "Is your Galaxy S6 boot-looping? 'YES' or 'NO'\n")
        self.os = str
        self.warranty = str
        self.power = str
        self.exterior = str
        self.malware = str

    def mainF(self):
        """Questioning functions"""
        try:
            def qos(self):
                """What OS?"""
                self.os = "Android"
                qwar(self)


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
        sol = open("lib/android.txt")
        solutions = sol.readlines()
        print (solutions[index])
        sol.close()

if (__name__ != "__main__"):
    main = Main()
    main.mainF()
