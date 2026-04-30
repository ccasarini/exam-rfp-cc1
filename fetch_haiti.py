import requests
import json
import time

# --- SETUP ---
# We use the Overpass API, which is the standard way to get data out of OpenStreetMap.
# We include multiple servers in case one is busy.
OVERPASS_URLS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.osm.ch/api/interpreter",
    "https://overpass.nchc.org.tw/api/interpreter"
]

# We should identify ourselves to the servers.
HEADERS = {
    'User-Agent': 'HaitiBorderFetcher/1.0 (Contact: your-email@example.com)'
}

# This is the "Query". It's like a search command.
# We are looking for:
# - relation: A complex shape in OSM.
# - ISO3166-1=HT: The international code for Haiti.
# - admin_level=2: The country-level border.
QUERY = """
[out:json][timeout:90];
relation["ISO3166-1"="HT"]["admin_level"="2"];
out geom;
"""

def fetch_haiti_border():
    """
    Downloads Haiti's border from OpenStreetMap and saves it as a GeoJSON file.
    GeoJSON is a standard format for sharing map data that Leaflet understands easily.
    """
    for url in OVERPASS_URLS:
        print(f"Trying to fetch data from: {url}...")
        try:
            # Send the request to the server
            response = requests.post(url, data={'data': QUERY}, headers=HEADERS, timeout=100)
            response.raise_for_status() # Check if the request was successful
            
            data = response.json()
            
            # OpenStreetMap data comes in a custom format. 
            # We need to convert it into "GeoJSON" so our map can read it.
            geojson = {
                "type": "FeatureCollection",
                "features": []
            }
            
            for element in data.get('elements', []):
                if element['type'] == 'relation':
                    # A country border is often made of many segments (lines).
                    # We collect all these segments.
                    for member in element.get('members', []):
                        if 'geometry' in member:
                            coordinates = [[p['lon'], p['lat']] for p in member['geometry']]
                            geojson['features'].append({
                                "type": "Feature",
                                "geometry": {
                                    "type": "LineString",
                                    "coordinates": coordinates
                                },
                                "properties": {
                                    "name": "Haiti Border Segment"
                                }
                            })
            
            if geojson['features']:
                # Save the final data to a file
                output_file = "haiti_border.geojson"
                with open(output_file, "w") as f:
                    json.dump(geojson, f, indent=2)
                print(f"✅ Success! Data saved to '{output_file}'.")
                return True
            
        except Exception as e:
            print(f"❌ Attempt failed: {e}")
            time.sleep(2) # Wait a moment before trying the next server

    print("🛑 Failed to fetch data from all servers.")
    return False

if __name__ == "__main__":
    fetch_haiti_border()
