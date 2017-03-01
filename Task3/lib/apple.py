#Apple Module

class Apple:
    def __init__(self):
        print ("\nTroublegun Apple Initialized...\n")
        self.error = "I'm sorry I didn't understand...\n\n"
        self.nosupp = "Your device is currently not supported...\n"

    def intro(self):
        userinput = str.upper(str(input("What model of Apple device do you have? "
                                                                     "e.g. iPhone 7 Plus\n")))
        if("IPHONE" in userinput):
            main.iphone(userinput)
        elif("IPOD" in userinput) or ("IPAD" in userinput):
            print (self.nosupp)
            return
        else:
            print (self.error)
            main.intro()

    def iphone(Self, x):
        if("7" in x) and ("PLUS" in x):
            version = "7 Plus"
        elif("7" in x) and ("PLUS" not in x):
            version = "7"
        elif("6" in x) and ("S" in x) and ("PLUS" in x):
            version = "6S Plus"
        elif("6" in x) and ("S" in x) and ("PLUS" not in x):
            version = "6S"
        elif("SE" in x):
            version = "SE"
        else:
            print(self.nosupp)
        print("iPhone {} Selected" .format(version))

if __name__ != "__main__":
    main = Apple()
    main.intro()
else:
    print("This module is designed only to be imported, run main.py")
