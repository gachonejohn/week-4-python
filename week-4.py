def read_and_modify_file():
#    accepting user input (file name)
    input_filename = input("Enter the file name: ")
    
    try:
        # Opening file in read mode 
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modifying the content (converting to uppercase)
        modified_content = content.upper()

        # user to enter the file name for the modified content 
        output_filename = input("Enter file name for the modified content: ")

        # Writing the modified content to the new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read the file '{input_filename}' or write to the output file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# calling the function
read_and_modify_file()
