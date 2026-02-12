

def add_one(value):
    """Adds 1 to the parameter passed to the method."""
    return value + 1

# Initialize a variable in the body of the program
my_variable = 5
print(f"Initial value: {my_variable}")

# Call the method that adds 1 to the variable
my_variable = add_one(my_variable)

# Display the variable again in the body of the program
print(f"Value after add_one: {my_variable}")