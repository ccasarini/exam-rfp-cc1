import requests
import csv

# 1. Setup
OVERPASS_URL = "https://overpass-api.de/api/interpreter"
# Many APIs require a 'User-Agent' to know who is requesting the data.
HEADERS = {
    'User-Agent': 'HaitiBorderFetcher/1.0 (https://example.com/)'
}

# 2. The Query
# We use ISO3166-1="HT" because it's a unique code for Haiti.
QUERY = """
[out:json];
relation["ISO3166-1"="HT"]["admin_level"="2"];
(._;>;);
out body;
"""

def fetch_haiti_border():
    print("Connecting to OpenStreetMap...")
    
    try:
        # Send the request with headers
        response = requests.post(OVERPASS_URL, data={'data': QUERY}, headers=HEADERS, timeout=60)
        
        # If we still get a 406, try GET instead of POST
        if response.status_code == 406:
            print("POST failed with 406, trying GET...")
            response = requests.get(OVERPASS_URL, params={'data': QUERY}, headers=HEADERS, timeout=60)
            
        response.raise_for_status()
        
        data = response.json()
        elements = data.get('elements', [])
        nodes = [e for e in elements if e['type'] == 'node']
        
        if not nodes:
            print("No points found. The server might be busy or the query needs adjustment.")
            return

        filename = "haiti_borders.csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['latitude', 'longitude'])
            for node in nodes:
                writer.writerow([node['lat'], node['lon']])
        
        print(f"Success! '{filename}' created with {len(nodes)} points.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_haiti_border()
