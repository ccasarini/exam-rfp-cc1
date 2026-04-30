import geopandas as gpd

# 1. Load the full communes dataset
data = gpd.read_file("haiti_borders/hti_admin2.geojson")

# 2. Extract just Port-au-Prince
# We use the 'adm2_name' column to find the city
paup = data[data['adm2_name'] == 'Port-au-Prince']

# 3. Save it to a new, small file
paup.to_file("haiti_borders/port_au_prince.geojson", driver='GeoJSON')

print("Port-au-Prince data extracted successfully!")
