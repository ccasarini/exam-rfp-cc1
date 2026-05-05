# Strengthening Education Continuity in Conflict-Affected Regions
## Response to EBI RFP: A Scalable Strategy for Educational Continuity - Master ICT4D 2026

This repository contains the data and processing pipeline for a geospatial analysis aimed at protecting educational access in Haiti. By integrating high-resolution population data, school locations, and conflict event tracking, this project identifies critical areas where armed conflict threatens the continuity of learning.

## Data Transformation Pipeline

The data in this repository has been transformed through a multi-step pipeline to ensure precision and relevance to the educational sector in the Ouest department of Haiti.

### 1. Administrative Boundary Extraction
The project focuses on the **Ouest** department and **Port-au-Prince**. 
- **Action:** Using `extract_city.py`, the Port-au-Prince commune was isolated from the national administrative level 2 (communes) dataset.
- **Output:** `data/borders/port_au_prince.geojson`.

### 2. Demographic Refinement (School-Age Population)
Raw population density data provides a total count, which is not specific enough for educational planning.
- **Source:** Kontur Population (H3 Hexagonal Grid, 400m).
- **Transformation:** The script `fetch_ouest_population.py` clips the national grid to the Ouest department and applies a demographic factor of **20.8%** (based on UN Population Prospects) to isolate children aged **6–15**.
- **Output:** `data/population_density/ouest_population_400m.geojson`.

### 3. Infrastructural Categorization
To focus on primary and secondary education, the full dataset of educational facilities required rigorous filtering.
- **Source:** HOTOSM Haiti Education Facilities via HDX.
- **Transformation:** `fetch_schools.py` filters facilities by amenity type (`school`, `college`) and excludes keywords related to universities or kindergartens. It also standardizes school names and clips the results to the Ouest department.
- **Output:** `data/schools/ouest_schools.geojson`.

### 4. Conflict Event Geoprocessing
Raw conflict data from UCDP is processed to enable spatial analysis of fatalities and frequency.
- **Source:** UCDP GED (Uppsala Conflict Data Program).
- **Transformation:** `fetch_haiti_conflict_data.py` retrieves the data, and `convert_conflict_csv.py` transforms the cleaned CSV records into a GeoJSON format, preserving key metrics like fatality counts and event types for mapping.
- **Output:** `data/armed_conflicts/ouest_conflict.geojson`.

---

## Repository Structure

- `data/`: Contains raw and processed datasets organized by category (borders, schools, population, conflicts).
- `scripts/`: Python scripts used for data acquisition, cleaning, and spatial transformation.
- `source.md`: Detailed documentation of the data sources and the rationale behind their selection.
