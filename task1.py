import os

file_name = "sample.txt"
if not os.path.exists(file_name):
    print(f"The file {file_name} was not found.")
else:
    with open(file_name, "rt") as file:
        content = file.read()
    for i, line in enumerate(content.strip().splitlines() , start=1):
          print(f" Line {i}: {line}")     
    

#     with open("sample.txt", "rt") as file:
#         line1 = file.readline()
#         line2 = file.readline()
        
# print(f" Line 1: {line1}")
# print(f" Line 2: {line2}")