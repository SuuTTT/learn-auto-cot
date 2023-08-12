import os

def rename_part_1_files(directory='.'):
    # Iterate through all files in the given directory
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            # Check if the file ends with '_part_1.json'
            if filename.endswith('_part_1.json'):
                original_name = filename.rsplit('_part_1', 1)[0] + '.json'
                original_path = os.path.join(dirpath, original_name)
                part_1_path = os.path.join(dirpath, filename)
                
                # Remove the original file
                if os.path.exists(original_path):
                    os.remove(original_path)
                
                # Rename the _part_1.json file to the original name
                os.rename(part_1_path, original_path)
                print(f"Renamed {part_1_path} to {original_path}")

# Run the function
rename_part_1_files()
