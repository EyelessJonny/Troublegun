#Samsung Module

class Samsung:
    """Main class for module"""
    def __init__(self):
        print ("\nTroublegun Samsung Initialized...\n")
        self.error = "I'm sorry I didn't understand...\n\n"

    def intro(self):
        """Selection function"""
        x = (input("What model of Samsung device do you "
                   "have? e.g 'Galaxy S6 Edge+'\n> ")).upper()
        if ("GALAXY" in x) and ("7" in x) and ("EDGE" in x):
            version = "ssevenedge"
        elif ("GALAXY" in x) and ("7" in x) and ("EDGE" not in x):
            version = "sseven"
        elif ("GALAXY" in x) and ("6" in x) and ("+" in x) and ("EDGE" in x):
            version = "ssixedge+"
        elif ("GALAXY" in x) and ("6" in x) and ("+" not in x) and ("EDGE" in x):
            version = "ssixedge"
        elif ("GALAXY" in x) and ("6" in x) and ("+" not in x) and ("EDGE" not in x):
            version = "ssix"
        else:
            return x
        exec("import Task3.lib.models.galaxy.{}" .format(version))

samsung = Samsung()
