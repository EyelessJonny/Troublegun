# A Python script used to test modules which can only be run on import,
# but which auto run on import.

userinput = str.lower(str(input("Please enter a module to test:\n")))
exec("import lib.{}" .format(userinput))
exec("module = lib.{}.{}.intro()" .format(userinput, userinput))
if(module == 1):
    print("Fail")
else:
    print("Success")
