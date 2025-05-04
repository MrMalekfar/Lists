# merge_lists.py
import os

def merge_lists():
    # List of files to merge
    files_to_merge = [
        'ipv4MTN',
        'ipv4MCI',
        'ipv4TZ',
        'CFDNS',
        'frag',
        'ipv6'
    ]
    
    # Set to store unique lines
    merged_set = set()
    
    # Read each file and add lines to the set
    for file_name in files_to_merge:
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                # Remove whitespace and add non-empty lines to set
                for line in lines:
                    line = line.strip()
                    if line:  # Ignore empty lines
                        merged_set.add(line)
        except FileNotFoundError:
            print(f"Warning: {file_name} not found, skipping.")
        except Exception as e:
            print(f"Error reading {file_name}: {e}")
    
    # Sort the merged list for consistency
    merged_list = sorted(merged_set)
    
    # Write the merged list to a new file
    output_file = 'merged_list.txt'
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in merged_list:
            file.write(line + '\n')
    
    print(f"Merged list written to {output_file} with {len(merged_list)} unique lines.")

if __name__ == "__main__":
    merge_lists()
