# Data Sources

## Haiti Administrative Boundaries

The geographic boundary data for Haiti's borders and administrative levels (0–3) used in this project were retrieved from **OpenStreetMap (OSM)** using **Overpass Turbo**.

During the research phase, several boundary sources were considered:
- **GADM** (Database of Global Administrative Areas)
- **Natural Earth** (Public domain map data)
- **OpenStreetMap (OSM)**

I chose **OpenStreetMap** because it offers the most up-to-date, community-driven administrative boundaries, which are frequently updated to reflect the local geographic reality in Haiti. The administrative boundary files are stored in [data/borders/](data/borders/).

The data includes:
- **Admin Level 0:** National borders
- **Admin Level 1:** Departments
- **Admin Level 2:** Arrondissements
- **Admin Level 3:** Communes
## Population Density (School-Age 6-15)

The population distribution data is sourced from **Kontur Population**, specifically the dataset for Haiti available on the **Humanitarian Data Exchange (HDX)**.

### Choice of Source
During the research phase, several gridded population datasets were evaluated:
- **WorldPop** (High-resolution ML-based demographics)
- **GPWv4** (Gridded Population of the World, Version 4)
- **GHS-POP** (Global Human Settlement Layer)
- **GlobPOP** (Annual global population dataset)
- **Kontur Population** (H3 Hexagonal Grid)

I specifically selected **Kontur Population** because of its use of the **H3 hexagonal grid** (400m resolution). Hexagons provide a higher level of spatial precision and consistency compared to traditional square grids, as the distance between the center of any cell and all its neighbors is identical.

### Age Range Relevance (6-15 Years Old)
For this project, which focuses on **education in armed conflict areas**, total population data was refined to represent children in the typical age range for primary and secondary school (**6 to 15 years old**, inclusive). 

Since spatial age-disaggregated grids are often modeled at lower resolutions, I maintained the high-precision Kontur hexagonal grid and applied a demographic factor of **20.8%** to the total population counts. This percentage is derived from the **UN Population Prospects (2023/2024)** for Haiti, representing the estimated proportion of the population within the 6-15 age bracket. This ensures the map displays information directly relevant to the school-age population most impacted by conflict and educational disruption.

The processed population density file for the Ouest department is stored in `data/population_density/ouest_population_400m.geojson`. For more detailed information on the dataset, you can explore the [data/population_density/](data/population_density/) folder.


## School Locations

The data for school locations in Port-au-Prince is gathered from the **Humanitarian Data Exchange (HDX)**, specifically the **HOTOSM Haiti Education Facilities** dataset.

During the research phase, I investigated several sources for educational infrastructure:
- **UNICEF (Magicbox/GeoSight)**
- **World Bank Open Data**
- **HOTOSM (Humanitarian OpenStreetMap Team)**

I chose **HOTOSM via HDX** as the primary source because it provides the most granular, georeferenced point data for schools in Haiti, allowing for direct integration into the interactive map. The school location files are stored in [data/schools/](data/schools/).

## Armed Conflict Data

For the analysis of armed conflict events, I researched several open-source databases proposed by Gemini, including:
- **GDELT** (Global Database of Events, Language, and Tone)
- **ACLED** (Armed Conflict Location & Event Data Project)
- **UCDP GED** (Uppsala Conflict Data Program - Georeferenced Event Dataset)

Among these options, I chose **UCDP GED** as the primary data source because of its **academic rigour and precision**. This dataset provides highly verified and reliable georeferenced information on conflict events, which is essential for a precise analysis of the security landscape in Haiti.

The armed conflict files are stored in [data/armed_conflicts/](data/armed_conflicts/).
