
import sys

def shrink(input_string):
    """Displays the first eight characters of the input string."""
    print(input_string[:8])

def enlarge(input_string):
    """Appends 'Z' characters to make the string a total of eight characters."""
    print(input_string + 'Z' * (8 - len(input_string)))

def main():
    # Get the command line arguments (skip the first one as it's the script name)
    args = sys.argv[1:]

    # Check if no arguments are provided
    if len(args) < 1:
        print('none')
        return

    # Iterate over each argument and apply the appropriate method
    for arg in args:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:  # len(arg) == 8
            print(arg)

if __name__ == '__main__':
    main()