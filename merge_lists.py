import os
import json

def merge_lists():
    # List of input files (adjust names/paths as needed)
    files_to_merge = [
        'ipv4MTN',
        'ipv4MCI',
        'ipv4TZ',
        'CFDNS',
        'frag',
        'ipv6',
        'wp.txt'
    ]
        # Dictionary to store data
    data = {}
    # Set for unique merged entries (excluding wp)
    merged_set = set()
    
    # Process each file
    for file_name in files_to_merge:
        if os.path.exists(file_name):
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Read and clean entries
                    entries = [entry.strip().strip('"').strip(',') for entry in file.read().replace('\n', ',').split(',') if entry.strip()]
                    # Use file name (without extension) as key
                    key = os.path.splitext(file_name)[0]
                    data[key] = entries
                    # Add to merged set only if not wp
                    if key != 'wp':
                        merged_set.update(entries)
                    print(f"Processed {file_name} with {len(entries)} entries")
            except Exception as e:
                print(f"Error reading {file_name}: {e}")
        else:
            print(f"Warning: {file_name} not found, skipping.")
    
    # Add deduplicated, sorted merged list
    data["merged"] = sorted(merged_set)
    
    # Write to JSON file with proper formatting
    with open('merged_lists.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    
    # Print summary
    print("\nSummary:")
    for key, value in data.items():
        print(f"{key}: {len(value)} entries")

if __name__ == "__main__":
    merge_lists()
