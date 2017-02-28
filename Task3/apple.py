#Apple Module

class Apple:
    def __init__(self):
        print ("\nTroublegun Apple Initialized...\n")
        self.error = "I'm sorry I didn't understand...\n\n"

    def intro(self):
        userinput = str.upper(str(input("What model of Apple device do you have?\n")))
        if("IPHONE" in userinput):
            iphone(userinput)
        elif("IPOD" in userinput) or ("IPAD" in userinput):
            print ("Your device is currently not supported...\n")
            return
        else:
            print (self.error)
            apple(self)

    def iphone(x):
        print("iPhone Selected")
        return

if __name__ != "__main__":
    main = Apple()
    main.intro()
else:
    print("This module is designed only to be imported, run main.py")
