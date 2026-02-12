
import sys

def downcase_it(string):
    """Convert the given string to lowercase and return it."""
    return string.lower()

# Check if there are parameters passed
if len(sys.argv) < 2:
    print("none")
else:
    # Iterate through the parameters and apply the downcase_it method
    for param in sys.argv[1:]:
        print(downcase_it(param))