import requests
import json
import os

def update_wp_file():
    # URL for the ip.json file from ircfspace/endpoint
    ip_json_url = "https://raw.githubusercontent.com/ircfspace/endpoint/main/ip.json"
    
    try:
        # Fetch the JSON file
        response = requests.get(ip_json_url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse JSON
        data = response.json()
        
        # Extract IP:port pairs
        wp_entries = [entry["ip"] for entry in data if "ip" in entry and isinstance(entry["ip"], str)]
        
        if not wp_entries:
            print("Warning: No valid IP:port entries found in ip.json")
            return
        
        # Write to wp.txt
        with open('wp.txt', 'w', encoding='utf-8') as file:
            for entry in wp_entries:
                file.write(f"{entry}\n")
        
        print(f"Successfully updated wp.txt with {len(wp_entries)} entries")
        
    except requests.RequestException as e:
        print(f"Error fetching ip.json: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing ip.json: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    update_wp_file()
