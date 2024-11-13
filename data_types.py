# Code By Samir chaudhary


# For Creating variables of each primitive data types
int_value = 7
float_value = 16.4
str_value = "nepal"
my_bool = True

# For Performing Arithmetic Operations
sum_value = int_value + float_value         # Adding int and float
difference_value = float_value - int_value  # Subtracting int from float
product_value = int_value * float_value     # Multiplying int and float 
division_value = float_value / int_value    # Dividing float by int


# For String concatenation
concatenated_str = str_value + " travel "



# For logical operation
bool_a = True
bool_b = False

# Logical AND
and_result = bool_a and bool_b   # Returns False because one of the operands is False

# Logical OR
or_result = bool_a or bool_b    # Returns True because one of the operands is True

# Logical NOT
not_result = not bool_a         # Returns False because bool_a is True

# Combining logical operations
combined_result = (bool_a and not bool_b)  # True because both conditions are True




# For Creating a dictionary to store and display these variables by their types as keys
datatypes_dict = {
    "int": [int_value],
    "float": [float_value],
    "str": [concatenated_str],
}


# For Displaying the results
print(datatypes_dict)
for data_type, values in datatypes_dict.items():
    print(f"{data_type}: {values}")