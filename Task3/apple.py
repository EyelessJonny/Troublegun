#Apple Module

def apple(self):
    userinput = str.upper(str(input"What model of Apple device do you have?"))
    if("IPHONE" in userinput)
        iphone(userinput)
    elif("IPOD" in userinput) or ("IPAD" in userinput)
        print ("Your device is currently not supported...")
        pass
    else:
        print (self.error)
        apple(self)

def iphone(x):
    print("iPhone Selected")
