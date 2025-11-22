import os

file_name = "output.txt"

def write_and_append_file():

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

write_and_append_file()

input_number = input("Enter 25 to read the file content: ")
if input_number == "25":
    def read_file(n):
            with open(file_name, "r") as file:
                content = file.read()
                print(f"Final content of {file_name}:\n{content}")
               
    read_file(input_number)
else:
    print("You did not enter 25. Exiting without reading the file.")


# if not os.path.exists(file_name):
#     data = input(f"Enter text to write to file: ")
#     def write_file(data):
#         with open(file_name, "wt") as file:
#             file.write(data + "\n")
#             print(f"Data successfully written to {file_name}.")
#     write_file(data)

# else:   
#     data = input(f"Enter additional text to append: ")
#     def append_file(data):
#         with open(file_name, "at") as file:
#             file.write(data + "\n")
#             print(f"Data successfully appended to {file_name}.")
#     append_file(data)
    
# def read_file(data):
#     with open(file_name , "rt") as file:
#         content = file.read()
#         print(f"Current content of {file_name}: ")
#         print(content)

# read_file(data)


