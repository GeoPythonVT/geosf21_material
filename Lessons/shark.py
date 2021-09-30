class Shark:

    # Class variables
    animal_type = "fish"
    location = "Indian Ocean"

    # Constructor method with instance variables name and age
    def __init__(self, nameStr, ageNmbr):
        self.name = nameStr
        self.age = ageNmbr

    # Method with instance variable length in [meter]
    def set_length(self, length):
        print("This shark has a length of " + str(length) + " meter.")
        
        
# Create a Shark instance, pass instance variables to constructor method

# Print out instance variable name

# Print out class variable location (in a sentence)

# Create a second Shark instance

# Print out instance variable name

# Use set_length method and pass length instance variable

# Print out class variable animal_type
