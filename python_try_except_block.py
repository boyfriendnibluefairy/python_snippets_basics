
## try-except blocks are used to handle errors
## Put the code that might cause an error inside the try block.
## If there's no error, the code inside the else block will continue to run.
## Use the "pass" keyword if you want except block to do nothing.

## For ErrorCodes or ErrorTypes, see python_error_types.txt

## Example: How to handle values with wrong data type
msg : str = "Please enter two numbers and I'll give you the sum.\n"
msg += "Enter 'q' to quit.\n"
print(msg)
while True:
    try:
        x = input("Please enter first number: ")
        if x == 'q':
            break
        y = input("Please enter second number: ")
        if y == 'q':
            break
        sum : int = int(x) + int(y)
    except ValueError:
        print("You did not enter a number. Please try again.")
    else:
        print(f"{x} + {y} = {sum}\n\n")


## Example: How to handle files that do not exist
## In this example, lorem.txt do not exist.
## "with" keyword properly opens and closes the file.
file_name1 = "lorem.txt"
file_name2 = "lorem_ipsum.txt"
try:
    with open(file_name1) as f1: # comment out to test
        contents1 = f1.read() # comment out to test
    with open(file_name2) as f2:
        contents2 = f2.read()
except FileNotFoundError:
    # uncomment to fail silently
    # pass

    # do not fail silently
    print("File not found")
else:
    print(f"{file_name1} contents:\n") # comment out to test
    print(contents1) # comment out to test
    print(f"{file_name2} contents:\n")
    print(contents2)

