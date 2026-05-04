# Data Sources

## Haiti Administrative Boundaries

The geographic boundary data (coordinates) for Haiti's borders and administrative levels (0–3) used in this project were retrieved from **OpenStreetMap (OSM)** using **Overpass Turbo**.

### Technical Note
These coordinates are essential for rendering the interactive Haiti map required for the RFP.

The data includes:
- **Admin Level 0:** National borders
- **Admin Level 1:** Departments
- **Admin Level 2:** Arrondissements
- **Admin Level 3:** Communes

The administrative boundary files are stored in `data/borders/`.

## Population Density

The population distribution data is sourced from **Kontur Population**, specifically the dataset for Haiti available on the **Humanitarian Data Exchange (HDX)**.

### Choice of Source
During the research phase, several gridded population datasets were evaluated (such as WorldPop and GPWv4). **Kontur Population** has been selected because of its use of the **H3 hexagonal grid** (400m resolution). Hexagons provide a higher level of spatial precision and consistency compared to traditional square grids, as the distance between the center of any cell and all its neighbors is identical. This makes the population density layer much more accurate for analyzing local clusters and urban distribution, that in this project is about the Ouest department in Port-au-Prince capital, Haiti.

The processed population density file for the Ouest department is stored in `data/ouest_population_400m.geojson`.

## School Locations

The data for school locations in Port-au-Prince is gathered from the **Humanitarian Data Exchange (HDX)**, specifically the **HOTOSM Haiti Education Facilities** dataset. These points provide the geographic coordinates of schools to be displayed on the project map.

The school location files are stored in `data/schools/`.

## Armed Conflict Data

For the analysis of armed conflict events, I researched several open-source databases proposed by Gemini, including:
- **GDELT** (Global Database of Events, Language, and Tone)
- **ACLED** (Armed Conflict Location & Event Data Project)
- **UCDP GED** (Uppsala Conflict Data Program - Georeferenced Event Dataset)

Among these options, I chose **UCDP GED** as the primary data source because of its **academic rigour and precision**. This dataset provides highly verified and reliable georeferenced information on conflict events, which is essential for a precise analysis of the security landscape in Haiti.

The armed conflict files are store in `data/armed_conflicts/`.
