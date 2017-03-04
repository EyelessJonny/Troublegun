#Apple Module

class Apple:
    """Main class for module"""
    def __init__(self):
        print ("\nTroublegun Apple Initialized...\n")
        self.error = "I'm sorry I didn't understand...\n\n"
        self.nosupp = "Your device is currently not supported...\n"

    def intro(self):
        """Selection"""
        userinput = str.upper(str(input("What model of Apple device do you have? "
                                                                     "e.g. 'iPhone 7 Plus'\n")))
        if("IPHONE" in userinput):
            main.iphone(userinput)
        elif("IPOD" in userinput) or ("IPAD" in userinput):
            print (self.nosupp)
            return
        else:
            print (self.error)
            main.intro()

    def iphone(Self, x):
        """Detailed selection"""
        if("7" in x) and ("PLUS" in x):
            version = "sevenplus"
        elif("7" in x) and ("PLUS" not in x):
            version = "seven"
        elif("6" in x) and ("S" in x) and ("PLUS" in x):
            version = "sixsplus"
        elif("6" in x) and ("S" in x) and ("PLUS" not in x):
            version = "sixs"
        elif("SE" in x):
            version = "se"
        else:
            print(self.nosupp)
            return
        exec("import lib.models.iphone.{}" .format(version))

if (__name__ != "__main__"):
    main = Apple()
    main.intro()
else:
    print("This module is designed only to be imported, run main.py")
