import csv
import json

def csv_to_geojson(csv_file, geojson_file):
    features = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                # Handle comma as decimal separator
                lat_str = row['CENTROID_LATITUDE'].replace(',', '.')
                lon_str = row['CENTROID_LONGITUDE'].replace(',', '.')
                
                lat = float(lat_str)
                lon = float(lon_str)
                
                feature = {
                    "type": "Feature",
                    "properties": {
                        "event_type": row['EVENT_TYPE'],
                        "sub_event_type": row['SUB_EVENT_TYPE'],
                        "fatalities": int(row['FATALITIES']),
                        "events_count": int(row['EVENTS']),
                        "disorder_type": row['DISORDER_TYPE'],
                        "population_exposure": row['POPULATION_EXPOSURE'],
                        "week": row['WEEK']
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [lon, lat]
                    }
                }
                features.append(feature)
            except (ValueError, KeyError) as e:
                print(f"Skipping row due to error: {e}")
                continue

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    with open(geojson_file, 'w', encoding='utf-8') as f:
        json.dump(geojson, f, indent=2)

if __name__ == "__main__":
    csv_to_geojson('ouest_armedconflict_cleaned.csv', 'data/ouest_conflict.geojson')
    print("Converted ouest_armedconflict_cleaned.csv to data/ouest_conflict.geojson")
