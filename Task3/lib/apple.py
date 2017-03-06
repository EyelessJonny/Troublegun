#Apple Module

class Apple:
    """Main class for module"""
    def __init__(self):
        print ("\nTroublegun Apple Initialized...\n")
        self.error = "I'm sorry I didn't understand...\n\n"

    def intro(self):
        """Selection function"""
        userinput = (input("What model of Apple device do you have? e.g. "
                           "'iPhone 7 Plus\n> ")).upper()
        """X for line length"""
        x = userinput
        if("IPHONE" in x) and ("7" in x) and ("PLUS" in x):
            version = "sevenplus"
        elif("IPHONE" in x) and ("7" in x) and ("PLUS" not in x):
            version = "seven"
        elif("IPHONE" in x) and ("6" in x) and ("S" in x) and ("PLUS" in x):
            version = "sixsplus"
        elif("IPHONE" in x) and ("6" in x) and ("S" in x) and ("PLUS" not in x):
            version = "sixs"
        elif("IPHONE" in x) and ("SE" in x):
            version = "se"
        elif("IPOD" in x) or ("IPAD" in x):
            return userinput
        else:
            print (self.error)
            apple.intro()
        exec("import lib.models.iphone.{}" .format(version))

if (__name__ != "__main__"):
    apple = Apple()
else:
    print("This module is designed only to be imported, run main.py")
