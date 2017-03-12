# A Python script used to test modules which can only be run on import,
# but which auto run on import.

userinput = (input("Please enter a module to test:\n> ")).lower()
try:
    module = None
    exec("from lib import {}" .format(userinput))
    exec("module = {}.{}.intro()" .format(userinput, userinput))
    if(module != None):
        print("1")
    else:
        print("2")
except Exception as e:
    print("Something went wrong, error [{}]\n\n" .format(e))
    if (module != None):
        print("3" )
    else:
        print("4")
