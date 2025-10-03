def process_file(filename):
    try:
        # Try to open and read the file
        with open(filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except IOError:
        print(f"Error: The file '{filename}' cannot be read.")
        return

    # Convert content to uppercase
    modified_content = content.upper()

    # Create output filename
    output_filename = f"modified_{filename}"

    try:
        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
    except IOError:
        print(f"Error: Could not write to file '{output_filename}'.")
        return

    print(f"Success! Modified content written to '{output_filename}'.")

# Ask user for filename
user_filename = input("Enter the filename to process: ")
process_file(user_filename)