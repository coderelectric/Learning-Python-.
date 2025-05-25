import os 

def list_directory_contents(path='/chapter 1 problems'):
    """
    List and print all files and directories in the specified path.
    Defaults to the current directory if no path is provided.
    """
    try:
        # Get list of entries in the directory
        entries = os.listdir(path)
        
        print(f"Contents of directory: {os.path.abspath(path)}")
        for entry in entries:
            print(entry)
    
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask user for the directory path
if __name__ == "__main__":
    user_input = input("Enter directory path (leave empty for current directory): ").strip()
    if not user_input:
        user_input = '.'
    list_directory_contents(user_input)


       