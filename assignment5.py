def read_modify_write_file():
    filename = input("📝 Enter the filename to read: ")

    try:
        # Try to open and read the original file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (example: add line numbers)
        lines = content.splitlines()
        modified_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]
        modified_content = "\n".join(modified_lines)

        # Create and write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"✅ Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file was not found. Please check the filename and try again.")
    except IOError:
        print("❌ Error: There was a problem reading or writing the file.")

# Run the function
read_modify_write_file()
