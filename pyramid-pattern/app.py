# Number of rows in the pyramid
rows = 5

# Loop through each row
for i in range(rows):
    # Calculate the number of spaces for the current row
    spaces = " " * (rows - i - 1)
    
    # Calculate the number of stars for the current row
    stars = "*" * (2 * i + 1)
    
    # Print the row with spaces and stars
    print(spaces + stars)