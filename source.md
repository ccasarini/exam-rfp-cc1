# Data Sources

## Haiti Administrative Boundaries

The geographic boundary data (coordinates) for Haiti's borders and administrative levels (0–3) used in this project were retrieved from **OpenStreetMap (OSM)** using **Overpass Turbo**.

### Technical Note
These coordinates are essential for rendering the interactive Haiti map required for the RFP. The data includes:
- **Admin Level 0:** National borders
- **Admin Level 1:** Departments
- **Admin Level 2:** Arrondissements
- **Admin Level 3:** Communes

The files are stored in GeoJSON format within the `haiti_borders/` directory and are used to provide the spatial framework for the application's mapping components.
