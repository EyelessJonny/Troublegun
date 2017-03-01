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
            iphone(userinput)
        elif("IPOD" in userinput) or ("IPAD" in userinput):
            print (self.nosupp)
            return
        else:
            print (self.error)
            main.intro()

    def iphone(x):
        print("iPhone Selected")
        if("7" in userinput) and ("plus" in userinput)
            sevenplus()
        elif("7" in userinput) and ("plus" not in userinput)
            seven()
        elif("6" in userinput) and ("s" in userinput) and ("plus" in userinput)
            sixsplus()
        else:
            print(self.nosupp)

if __name__ != "__main__":
    main = Apple()
    main.intro()
else:
    print("This module is designed only to be imported, run main.py")
