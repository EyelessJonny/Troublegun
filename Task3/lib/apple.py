#Apple Module

class Apple:
    """Main class for module"""
    def __init__(self):
        print ("\nTroublegun Apple Initialized...\n")
        self.error = "I'm sorry I didn't understand...\n\n"

    def intro(self):
        """Selection function"""
        x = (input("What model of Apple device do you have? e.g. "
                   "'iPhone 7 Plus\n> ")).upper()
        if ("IPHONE" in x) and ("7" in x) and ("PLUS" in x):
            version = "sevenplus"
        elif ("IPHONE" in x) and ("7" in x) and ("PLUS" not in x):
            version = "seven"
        elif ("IPHONE" in x) and ("6" in x) and ("S" in x) and ("PLUS" in x):
            version = "sixsplus"
        elif ("IPHONE" in x) and ("6" in x) and ("S" in x) and ("PLUS" not in x):
            version = "sixs"
        elif ("IPHONE" in x) and ("SE" in x):
            version = "se"
        else:
            return x
        exec("import Task3.lib.models.iphone.{}" .format(version))

apple = Apple()
