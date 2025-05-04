import os
import json

def merge_lists():
    # List of files to process (update paths if needed)
    files_to_merge = [
        'ipv4MTN',
        'ipv4MCI',
        'ipv4TZ',
        'CFDNS',
        'frag',
        'ipv6'
    ]
    
    # Dictionary to hold all lists
    data = {}
    
    # Set to collect unique entries for the merged list
    merged_set = set()
    
    # Process each file
    for file_name in files_to_merge:
        if os.path.exists(file_name):
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Read non-empty lines into a list
                    lines = [line.strip() for line in file if line.strip()]
                    # Use the file name without extension as the key
                    base_name = os.path.splitext(file_name)[0]
                    data[base_name] = lines
                    # Add to merged set
                    merged_set.update(lines)
                    print(f"Processed {file_name} with {len(lines)} entries")
            except Exception as e:
                print(f"Error reading {file_name}: {e}")
        else:
            print(f"Warning: {file_name} not found, skipping.")
    
    # Add the merged list (deduplicated and sorted)
    data["merged"] = sorted(merged_set)
    
    # Write to JSON file
    with open('merged_lists.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    
    # Summary
    print("\nSummary:")
    for key, value in data.items():
        print(f"{key}: {len(value)} entries")

if __name__ == "__main__":
    merge_lists()
