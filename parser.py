import pathlib

# Define the directory path
directory_path = '.' # Use '.' for the current directory, or a specific path like 'C:/Users/YourUser/Docs'

# Iterate through all items in the directory that match the '*.txt' pattern
for file_path in pathlib.Path(directory_path).glob('*.txt'):
    # Ensure the item is a file (not a directory with a .txt extension in its name)
    if file_path.is_file():
        # Open and read the file's content
        with open(file_path, 'r') as f:
            content = f.read()
            # *** Your parsing logic goes here ***
            # Example: print the file name and content
            print(f"--- Processing {file_path.name} ---")