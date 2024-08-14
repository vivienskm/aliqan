question = "Enter a number: "
response = input(question)

# Try to convert the input to an integer
try:
    number = int(response)
    print(f"You entered the number {number}.")
except ValueError:
    print("That's not a valid number!")
