# Dictionary generator
In this project, we are using specified keywords to generate a dictionary of keywords. This guide explains how to generate all possible passwords using a given list of keywords in Python. It features a recursive approach to create combinations of keywords, storing the results in a text file.

<h2>General Information</h2>
Python is a high-level, interpreted programming language known for its readability and versatility. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python's extensive standard library and large ecosystem of third-party packages make it suitable for a wide range of applications, from web development to data analysis and artificial intelligence.

The official home of Python is https://www.python.org.

<h2>Project Description</h2>
This project aims to generate all possible passwords from a given list of keywords using Python. The approach involves a recursive helper function that builds combinations of keywords up to a specified length. The generated passwords are written to a text file named `passwords.txt`. This project demonstrates how to use recursion in Python to solve combinatorial problems and manage output file operations efficiently. By iterating through different lengths and combining keywords, the project showcases how to create a comprehensive list of potential passwords for security testing or other purposes.

<h2>Features</h2>

- <b>Recursive function for generating combinations</b>
- <b>Dynamic length adjustment for combinations</b>
- <b>File operations to store generated passwords</b>
- <b>Scalable approach to handle various keyword lists</b>
- <b>Simple and readable Python code</b>

<h2>Code Explanation</h2>
The overall solution involves defining a recursive helper function and a main function to initiate the password generation process. The recursive function, `generate`, constructs combinations of the given keywords up to the desired length and writes them to a file. The main function, `crack`, iterates through different lengths to ensure all possible combinations are covered.

```python
# Python3 program to generate all passwords for given keywords

# Recursive helper function
# Adds/removes characters until the desired length is reached

def generate(arr, i, s, length):
    # Base case
    if i == 0:  # When length has been reached
        # Print it out/write to a file
        with open('passwords.txt', 'a') as out_file:
            out_file.write(s + '\n')
        return
    
    # Iterate through the array
    for j in range(0, length):
        # Create new string with the next character
        appended = s + arr[j]
        # Call generate again until the string has reached its length
        generate(arr, i - 1, appended, length)
    return

# Function to generate all possible passwords
def crack(arr, length):
    # Call for all required lengths
    for i in range(1, length + 1):
        generate(arr, i, "", length)
    return

# List of keywords to generate the password list
arr = ['readiness', 'carpar', 'mat', '1996', 'Curve', 'john']
length = len(arr)
possible_passwords = crack(arr, length)
```

<h2>Interactions in the Code</h2>

1. **Keyword List**: The list `arr` contains the keywords used for generating passwords. This list can be modified to include any set of keywords.
2. **Recursive Generation**: The `generate` function constructs combinations of keywords recursively. For each keyword, it appends it to the current string and calls itself with a reduced length.
3. **File Output**: Generated passwords are written to `passwords.txt` to ensure they are stored persistently. This allows for easy review and analysis of the generated passwords.
4. **Length Variation**: The `crack` function ensures that combinations of all lengths, from 1 to the length of the keyword list, are generated. This provides a comprehensive set of possible passwords.

<h2>Steps to Execute the Project</h2>

1. **Prepare the Environment**: Ensure Python is installed on your system. Create a new directory for the project and navigate to it.
2. **Create the Script**: Copy the provided code into a Python script file (e.g., `password_generator.py`).
3. **Run the Script**: Execute the script using the command `python password_gen.py`. This will generate the passwords and store them in `passwords.txt`.
4. **Review the Output**: Open `passwords.txt` to review the generated passwords. The file will contain all possible combinations of the given keywords.

