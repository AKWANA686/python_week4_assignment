# QUESTION 1
# File Read & Write Challenge 🖋️
# Create a program that reads a file and writes a modified version to a new file.

# Reads the input file
with open('input.txt', 'r') as f:
    content = f.read()

# Here we are modifying the content by changing it to lowercase
modified = content.lower()

# Writes the modified content to a new file(output.txt)
with open('output.txt', 'w') as f:
    f.write(modified)
print("File has been modified and saved as output.txt")

# QUESTION 2
# Error Handling Lab 🧪
# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
filename = input("Enter the filename: ")
try:
    with open(filename) as f:
        content = f.read()
    
    new_content = content.upper()
    
    with open("new_" + filename, 'w') as f:
        f.write(new_content)
        print("Created new_" + filename)
        
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
except:
    print("Error:Could not read or write the file.")