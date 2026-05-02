import requests
import zipfile
import os
import geopandas as gpd

# 1. Configuration - Where to get the data and where to save it
HDX_URL = "https://data.humdata.org/dataset/hotosm_hti_education_facilities/resource/47be53fa-5572-453a-9304-5345b3d1505e/download/hotosm_hti_education_facilities_points_geojson.zip"
ZIP_PATH = "data/schools/schools_points.zip"
EXTRACT_PATH = "data/schools/temp_schools"
PAUP_BOUNDARY_PATH = "data/borders/port_au_prince.geojson"
OUTPUT_PATH = "data/schools/paup_schools.geojson"

def fetch_and_filter_schools():
    # Step A: Create directories if they don't exist
    if not os.path.exists(EXTRACT_PATH):
        os.makedirs(EXTRACT_PATH)

    # Step B: Download the file from HDX
    print(f"Downloading data from HDX...")
    response = requests.get(HDX_URL)
    with open(ZIP_PATH, 'wb') as f:
        f.write(response.content)

    # Step C: Unzip the file
    print("Unzipping files...")
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_PATH)

    # Step D: Load the data into GeoPandas
    # We look for the .geojson file inside the extracted folder
    geojson_file = [f for f in os.listdir(EXTRACT_PATH) if f.endswith('.geojson')][0]
    all_schools = gpd.read_file(os.path.join(EXTRACT_PATH, geojson_file))
    
    # Step E: Load Port-au-Prince boundary
    paup_boundary = gpd.read_file(PAUP_BOUNDARY_PATH)

    # Step F: Filter (Clip) the schools to only those inside the Port-au-Prince boundary
    print("Filtering schools for Port-au-Prince...")
    paup_schools = gpd.clip(all_schools, paup_boundary)

    # Step G: Save the result
    paup_schools.to_file(OUTPUT_PATH, driver='GeoJSON')
    print(f"Success! {len(paup_schools)} schools saved to {OUTPUT_PATH}")

    # Cleanup: remove temporary files
    os.remove(ZIP_PATH)
    # Note: we keep the temp folder for now, or you can delete it if you want

if __name__ == "__main__":
    fetch_and_filter_schools()
