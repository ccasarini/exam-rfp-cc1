import os
import requests
import gzip
import shutil
import geopandas as gpd

def fetch_and_clip_population():
    # 1. SET UP PATHS
    # The direct S3 URL for Haiti's population data from Kontur (H3 hexagons, 400m resolution)
    population_url_gz = "https://geodata-eu-central-1-kontur-public.s3.eu-central-1.amazonaws.com/kontur_datasets/kontur_population_HT_20231101.gpkg.gz"
    
    # Paths for saving the data
    compressed_path = "data/kontur_population_haiti.gpkg.gz"
    raw_gpkg_path = "data/kontur_population_haiti.gpkg"
    boundary_path = "data/borders/hti_admin1.geojson"
    output_path = "data/ouest_population_400m.geojson"

    # 2. DOWNLOAD THE DATA
    if not os.path.exists(raw_gpkg_path):
        if not os.path.exists(compressed_path):
            print(f"Downloading population data for Haiti... this might take a minute.")
            response = requests.get(population_url_gz, stream=True)
            if response.status_code == 200:
                with open(compressed_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print("Download complete!")
            else:
                print(f"Failed to download data. Status code: {response.status_code}")
                return

        # 3. DECOMPRESS THE DATA
        print("Decompressing the file...")
        with gzip.open(compressed_path, 'rb') as f_in:
            with open(raw_gpkg_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print("Decompression complete!")
        # Optional: remove the compressed file to save space
        os.remove(compressed_path)

    # 4. LOAD THE BOUNDARY
    print("Loading Ouest department boundary...")
    haiti_admin1 = gpd.read_file(boundary_path)
    # Filter for only the 'Ouest' department
    ouest_boundary = haiti_admin1[haiti_admin1['adm1_name1'] == 'Ouest']

    if ouest_boundary.empty:
        print("Error: Could not find 'Ouest' department in the boundary file.")
        return

    # 5. LOAD THE POPULATION DATA
    # We use 'mask' to only load hexagons that intersect with our boundary.
    # This is much faster and uses less memory than loading the whole country.
    print("Loading and clipping population hexagons (this takes a moment)...")
    population_ouest = gpd.read_file(raw_gpkg_path, mask=ouest_boundary)

    # 6. CONVERT TO WGS84 (EPSG:4326)
    # Leaflet and most web maps expect coordinates in Latitude/Longitude (4326).
    print("Converting to EPSG:4326...")
    population_ouest = population_ouest.to_crs("EPSG:4326")

    # 7. SAVE THE RESULT
    print(f"Saving the result to {output_path}...")
    population_ouest.to_file(output_path, driver="GeoJSON")
    print("All done! You now have the population data for the Ouest department.")

if __name__ == "__main__":
    # Create the data folder if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
    
    fetch_and_clip_population()
