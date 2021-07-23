
n = int(input("The year ::"))

def is_leap(n):
    if (n%4 == 0 ):
        print("True")
        if( n%100 == 0 ):
            print("False")
            if ( n%400 == 0):
                print("True")