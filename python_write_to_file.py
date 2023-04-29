
## write data to a non-existent file
file_name = "dummy_file.txt"
## r+ means read and write
with open(file_name, 'r+') as file_object:
    file_object.write("Python is cAsE-sEnsitive.")

## Append Mode
## run this multiple times to test
file_name = "invitation.txt" # file to store the messages
msg = "Please enter your name below. \n " \
      "Type 'q' if you want to stop adding names: "
guest_name : str = ""

while guest_name != 'q':
    guest_name  = input(msg)
    with open(file_name, 'a') as file_object:
        if guest_name != 'q':
            file_object.write(f"{guest_name}\n")
print(f"\n names saved to {file_name}")