X = input("Enter anything: ")
 
if  X.isdigit():
    Y = int(X)
    if Y % 2 != 0:
        print (X, "is an odd integer")
    else:
        print(X,"is an even integer")
else:
    print(X,"is Not an integer") 