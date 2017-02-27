#Samsung Module

class Samsung:
    def __init__(self):
        print ("\nTroublegun Samsung Initialized...\n")
        self.error = "I'm sorry I didn't understand...\n\n"

    def intro(self):
        userinput = str.upper(str(input("What model of Samsung device do you have?")))
        if("GALAXY" in userinput) and ("S" in userinput):
            galaxyS(userinput)
        elif("GALAXY" in userinput):
            print ("Your device is currently not supported...")
            return
        else:
            print (self.error)
            Samsung(self)

    def galaxyS(x):
        print ("Galaxy S Selected")
        if("7" in x) and ("EDGE" in x):
            """Galaxy S7 Edge"""
            pass
        elif("7" in x) and ("EDGE" not in x):
            """Galaxy S7"""

if __name__ != "__main__":
    main = Samsung()
    main.intro()
