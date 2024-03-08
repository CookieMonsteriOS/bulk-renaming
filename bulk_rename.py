import os

def bulk_rename_files(directory, prefix, extension):
    # Get a list of all files in the directory
    files = os.listdir(directory)
    
    # Iterate over each file in the directory
    for index, file in enumerate(files):
        # Construct the new filename
        new_filename = f"{prefix}_{index + 1}.{extension}"
        
        # Get the current file's full path
        old_filepath = os.path.join(directory, file)
        
        # Construct the new file's full path
        new_filepath = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_filepath, new_filepath)
        print(f"Renamed {file} to {new_filename}")

# Example usage
if __name__ == "__main__":
    directory = "/path/to/your/directory"
    prefix = "file"
    extension = "txt"
    bulk_rename_files(directory, prefix, extension)
