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
        'ipv6'
    ]
    
    # Dictionary to store data
    data = {}
    # Set for unique merged entries
    merged_set = set()
    
    # Process each file
    for file_name in files_to_merge:
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                # Split by commas or newlines, and clean each entry
                entries = [entry.strip().strip('"').strip(',') for entry in content.replace('\n', ',').split(',') if entry.strip()]
                # Use file name (without extension) as key
                key = os.path.splitext(file_name)[0]
                data[key] = entries
                # Add to merged set for deduplication
                merged_set.update(entries)
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
