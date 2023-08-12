import os
import json

def chunk_data(data, size):
    """Yield successive size-sized chunks from data."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def process_jsonl_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = [json.loads(line) for line in f]

    if len(data) <= 10:
        return  # No need to split and write new files
    
    # Split data into chunks and write to new files
    for idx, chunk in enumerate(chunk_data(data, 10)):
        new_file_name = os.path.splitext(file_path)[0] + f"_part_{idx+1}.jsonl"
        with open(new_file_name, 'w', encoding='utf-8') as nf:
            for item in chunk:
                nf.write(json.dumps(item) + '\n')
        print(f"Written to {new_file_name}")

def process_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Check if the data is a dictionary and contains the 'examples' key
        if isinstance(data, dict) and "examples" in data:
            data_list = data["examples"]
            if len(data_list) <= 10:
                return  # No need to split and write new files

            # Split the examples into chunks and write to new files
            for idx, chunk in enumerate(chunk_data(data_list, 10)):
                new_data = data.copy()
                new_data["examples"] = chunk
                new_file_name = os.path.splitext(file_path)[0] + f"_part_{idx+1}.json"
                with open(new_file_name, 'w', encoding='utf-8') as nf:
                    json.dump(new_data, nf, indent=2)
                print(f"Written to {new_file_name}")

    except json.JSONDecodeError:
        # This block attempts to read the file as a .jsonl if there's a decode error
        # and then writes the chunks if the data length exceeds 10.
        with open(file_path, 'r', encoding='utf-8') as f:
            data_list = [json.loads(line) for line in f]
            
            if len(data_list) <= 10:
                return
            
            for idx, chunk in enumerate(chunk_data(data_list, 10)):
                new_file_name = os.path.splitext(file_path)[0] + f"_part_{idx+1}.json"
                with open(new_file_name, 'w', encoding='utf-8') as nf:
                    for item in chunk:
                        nf.write(json.dumps(item) + '\n')
                print(f"Written to {new_file_name}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


# Start processing from the current directory
current_dir = '.'

for dirpath, dirnames, filenames in os.walk(current_dir):
    for file in filenames:
        if file.endswith('.jsonl'):
            process_jsonl_file(os.path.join(dirpath, file))
        elif file.endswith('.json'):
            process_json_file(os.path.join(dirpath, file))
