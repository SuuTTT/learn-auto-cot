import json
import os

# Define the directories and filenames based on the provided structure
directories = {
    "/workspaces/learn-auto-cot/dataset/MultiArith": "MultiArith.json",
    "/workspaces/learn-auto-cot/dataset/SingleEq": "questions.json"
}

def truncate_file_content(dirpath, filename):
    # Construct full path
    filepath = os.path.join(dirpath, filename)

    # Open, read, and modify JSON file
    with open(filepath, 'r') as f:
        truncated_data = data[:10]  # Retain only the first 10 items

    # Overwrite the original file with truncated data
    with open(filepath, 'w') as f:
        json.dump(truncated_data, f, indent=4)

for dirpath, filename in directories.items():
    truncate_file_content(dirpath, filename)
