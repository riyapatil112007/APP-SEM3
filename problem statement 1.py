# Read the input file
with open("input.txt", "r") as file:
    data = file.read()

# Convert text into uppercase
data = data.upper()

# Write into another file
with open("output.txt", "w") as file:
    file.write(data)

print("File converted into uppercase successfully!")