# Get the input from the user
input_str = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list of numbers
numbers = input_str.split()

# Initialize a variable to store the sum
sum_of_numbers = 0

# Use a for loop to iterate through the numbers and calculate the sum
for num in numbers:
    try:
        # Convert the input to a float (assuming decimal numbers)
        num = float(num)
        sum_of_numbers += num
    except ValueError:
        print(f"Skipping invalid input: {num}")

# Print the sum of the numbers
print(f"The sum of the numbers is: {sum_of_numbers}")
