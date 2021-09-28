""" Put description, function, version, time, author information 
 @version  2021-09-26
 @author Werth @ VT """

# attributes: Variables and functions
title = 'The meaning of Life'   # global variable

def world():
    print('Hello, world!')


# main program
    
def main():
    print(title)

    
# This line causes main() to be executed if this file (module)
# is executed without an import (i.e., from the command line).
# If the module is imported, the condition will fail.
if __name__ == "__main__": main()
    # you could also add more code here
    # code to run when this is the main program
