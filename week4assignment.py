def file_modifier_with_error_handling():
    """
    A combined program that reads from a user-specified file, modifies its
    content, and writes to a new file, with robust error handling.
    """
    print("Welcome to the File Modifier!")
    print("This program will read a file, convert its text to uppercase, and save it to a new file.")
    
    # Loop for user input and error handling
    while True:
        source_filename = input("\nEnter the name of the file to read from: ")
        destination_filename = input("Enter the name of the file to write to: ")

        # Check for empty filenames
        if not source_filename or not destination_filename:
            print("Error: Filenames cannot be empty. Please try again.")
            continue

        try:
            # Step 1: Read the content from the source file
            with open(source_filename, 'r') as infile:
                content = infile.read()
                print(f"\nSuccessfully read from '{source_filename}'.")
            
            # Step 2: Modify the content (e.g., convert to uppercase)
            modified_content = content.upper()
            
            # Step 3: Write the modified content to the destination file
            with open(destination_filename, 'w') as outfile:
                outfile.write(modified_content)
            
            print(f"Successfully wrote the modified content to '{destination_filename}'.")
            print("Task completed successfully!")
            
            # Exit the loop on success
            break

        except FileNotFoundError:
            print(f"Error: The file '{source_filename}' was not found.")
            print("Please ensure the file exists and the name is spelled correctly.")
        
        except PermissionError:
            print(f"Error: You do not have permission to access one of the files.")
            print("Check your file permissions and try again.")
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again with different filenames.")

# Run the combined program
file_modifier_with_error_handling()