#Samsung Module

class Samsung:
    def __init__(self):
        print ("\nTroublegun Samsung Initialized...\n")
        self.error = "I'm sorry I didn't understand...\n\n"
        self.nosupp = "Your device is currently not supported...\n"

    def intro(self):
        userinput = str.upper(str(input("What model of Samsung device do you have? "
                                                                     "e.g Galaxy S7 Edge")))
        if("GALAXY" in userinput) and ("S" in userinput):
            galaxyS(userinput)
        elif("GALAXY" in userinput):
            print ("Your device is currently not supported...")
            return
        else:
            print (self.error)
            Samsung(self)

    def galaxyS(self, x):
        if("7" in x) and ("EDGE" in x):
            """S7 Edge"""
            version = "S7 Edge"
            
            return
        elif("7" in x) and ("EDGE" not in x):
            """Galaxy S7"""
            return
        else:
            print(self.nosupp)
            return

if __name__ != "__main__":
    main = Samsung()
    main.intro()
