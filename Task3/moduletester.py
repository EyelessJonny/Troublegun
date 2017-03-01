# A Python script used to test modules which can only be run on import,
# but which auto run on import.

userinput = str.lower(str(input("Please enter a module to test:\n")))
# solution = __import__(userinput)
exec("import lib.{}" .format(userinput))
exec("lib.{}" .format(userinput))
