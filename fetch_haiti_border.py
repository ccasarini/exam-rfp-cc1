import requests
import json
import time

# 1. Setup - Using a different server that might be less busy
OVERPASS_URLS = [
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass-api.de/api/interpreter"
]
HEADERS = {
    'User-Agent': 'HaitiBorderFetcher/1.0 (https://example.com/)'
}

# 2. The Query: Fetching the relation geometry directly
QUERY = """
[out:json][timeout:90];
relation["ISO3166-1"="HT"]["admin_level"="2"];
out geom;
"""

def fetch_haiti_border():
    for url in OVERPASS_URLS:
        print(f"Fetching geometry from {url}...")
        try:
            response = requests.post(url, data={'data': QUERY}, headers=HEADERS, timeout=100)
            response.raise_for_status()
            
            data = response.json()
            geojson = {"type": "FeatureCollection", "features": []}
            
            for element in data.get('elements', []):
                if element['type'] == 'relation':
                    for member in element.get('members', []):
                        if 'geometry' in member:
                            coordinates = [[p['lon'], p['lat']] for p in member['geometry']]
                            geojson['features'].append({
                                "type": "Feature",
                                "geometry": {"type": "LineString", "coordinates": coordinates},
                                "properties": {}
                            })
            
            if geojson['features']:
                with open("haiti_borders.json", "w") as f:
                    json.dump(geojson, f)
                print("Success! Data saved to 'haiti_borders.json'.")
                return
            
        except Exception as e:
            print(f"Attempt failed: {e}")
            time.sleep(2)

    print("Failed to fetch data from all servers.")

if __name__ == "__main__":
    fetch_haiti_border()
