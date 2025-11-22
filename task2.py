import os

file_name = "output.txt"

def write_append_and_read():

    if not os.path.exists(file_name):
        user_input = input("Enter text to write to the file: ")
        with open(file_name, "w") as file:
            file.write(user_input + "\n")
            print(f"Data successfully written to {file_name}.\n")
    else:
        additional_text = input("Enter additional text to append: ")
        with open(file_name, "a") as file:
            file.write(additional_text + "\n")
        print(f"Data successfully appended to {file_name}.\n")

    user_input = input("Enter 25 to read the file content: ")
    if user_input == "25":
        with open(file_name, "r") as file:
            content = file.read()
            print(f"Final content of {file_name}:\n{content}")
               
    else:
        print("You did not enter 25. Exiting without reading the file.")

write_append_and_read()



