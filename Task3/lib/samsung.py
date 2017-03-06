#Samsung Module

class Samsung:
    """Main class for module"""
    def __init__(self):
        print ("\nTroublegun Samsung Initialized...\n")
        self.error = "I'm sorry I didn't understand...\n\n"
        self.nosupp = "Your device is currently not supported...\n"

    def intro(self):
        """Selection"""
        userinput = str.upper(str(input("What model of Samsung device do you
                                        "have? e.g 'Galaxy S6 Edge+''\n> ")))
        if("GALAXY" in userinput) and ("S" in userinput):
            main.galaxys(userinput)
        elif("GALAXY" in userinput):
            print (self.nosupp)
            return
        else:
            print (self.error)
            Samsung(self)

    def galaxys(self, x):
        """Detailed selection"""
        if("7" in x) and ("EDGE" in x):
            version = "ssevenedge"
        elif("7" in x) and ("EDGE" not in x):
            version = "sseven"
        elif("6" in x) and ("+" in x) and ("EDGE" in x):
            version = "ssixedge+"
        elif("6" in x) and ("+" not in x) and ("EDGE" in x):
            version = "ssixedge"
        elif("6" in x) and ("+" not in x) and ("EDGE" not in x):
            version = "ssix"
        else:
            print(self.nosupp)
            return
        exec("import lib.models.galaxy.{}" .format(version))

if (__name__ != "__main__"):
    main = Samsung()
    main.intro()
