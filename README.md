# Module 5: Files, Exceptions, and Errors in Python

This repository contains Python programs for **Module 5**, focusing on file handling, user input, and error checking using the `os` module.

Both tasks demonstrate practical usage of **reading, writing, appending, and validating files** in Python.

---

##  Task 1: Read a File and Handle Errors

###  File Used
`sample.txt`

###  What the program does

1. Checks if `sample.txt` file exists using `os.path.exists()`
2. If NOT found → Displays an error message
3. If found:
   - Reads the file content
   - Prints each line with a line number 
   - Removes blanks lines and trailing spaces from the end of file

### 🔹 Sample Output

**If file exists:**
It prints the contents of the file and also removes any blank lines or spaces in the end of the file.

Line 1: This is a sample file
Line 2: File handling in progress

---

##  Task 2: Write and Append Data to a File

###  File Used
`output.txt`

###  What the program does

1. Checks if `output.txt` exists
2. If NOT exists:
   - Asks user to enter text 
   - Creates file and writes the text to `output.txt`
3. If exists:
   - Asks user for additional text
   - Appends it to the file
4. Prompts user to enter **25**
   - If user enters **25** → Reads and displays the final content of `output.txt`
   - If not → print message "You did not enter 25. Exiting without reading the file"

### 🔹 Example Output

Enter additional text to append: Learning file handling in Python.
Data successfully appended to output.txt.

Enter 25 to read the file content: 25
Final content of output.txt:
Hello, Python!
Learning file handling in Python.