# Data Sources

## Haiti Administrative Boundaries

The geographic boundary data (coordinates) for Haiti's borders and administrative levels (0–3) used in this project were retrieved from **OpenStreetMap (OSM)** using **Overpass Turbo**.

### Technical Note
These coordinates are essential for rendering the interactive Haiti map required for the RFP. The administrative boundary files are stored in `data/borders/`.

The data includes:
- **Admin Level 0:** National borders
- **Admin Level 1:** Departments
- **Admin Level 2:** Arrondissements
- **Admin Level 3:** Communes

## School Locations

The data for school locations in Port-au-Prince is gathered from the **Humanitarian Data Exchange (HDX)**, specifically the **HOTOSM Haiti Education Facilities** dataset. These points provide the geographic coordinates of schools to be displayed on the project map.

The school location files are stored in `data/schools/`.

## Armed Conflict Data

For the analysis of armed conflict events, I researched several open-source databases proposed by Gemini, including:
- **GDELT** (Global Database of Events, Language, and Tone)
- **ACLED** (Armed Conflict Location & Event Data Project)
- **UCDP GED** (Uppsala Conflict Data Program - Georeferenced Event Dataset)

Among these options, I chose **UCDP GED** as the primary data source because of its **academic rigour and precision**. This dataset provides highly verified and reliable georeferenced information on conflict events, which is essential for a precise analysis of the security landscape in Haiti.
