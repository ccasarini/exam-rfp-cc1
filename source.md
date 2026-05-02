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

For the analysis of armed conflict events, I researched several open-source databases, including:
- **ACLED** (Armed Conflict Location & Event Data Project)
- **UCDP GED** (Uppsala Conflict Data Program - Georeferenced Event Dataset)
- **GDELT** (Global Database of Events, Language, and Tone)

I chose **ACLED** as the primary data source because it provides highly detailed information about the specific types of conflict events (e.g., battles, violence against civilians, and riots), which is essential for understanding the security landscape in Haiti.

Following instructions from Gemini, I registered for an ACLED account and downloaded the comprehensive dataset for the region:
- **Dataset:** [Latin-America-the-Caribbean_aggregated_data_up_to_week_of-2026-04-18.csv](./Latin-America-the-Caribbean_aggregated_data_up_to_week_of-2026-04-18.csv)
