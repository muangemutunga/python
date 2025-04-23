def read_and_modify_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: File not found.")
    except IOError:
        print("❌ Error: File could not be read or written.")

# Run the function
read_and_modify_file()
