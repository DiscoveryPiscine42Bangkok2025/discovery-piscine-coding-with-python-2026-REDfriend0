
import sys 

if len(sys.argv) < 2: 
    print("none")
else: 
    word = str(input("what was the parameter? "))
    if word == sys.argv[1]: 
        print("Good job!")
    else: 
        print("Nope, sorry...")
