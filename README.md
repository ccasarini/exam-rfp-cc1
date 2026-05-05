# Strengthening Education Continuity in Conflict-Affected Regions
## Response to EBI RFP: A Scalable Strategy for Educational Continuity - Master ICT4D 2026

This repository contains the data and processing pipeline for a geospatial analysis aimed at protecting educational access in Haiti. By integrating high-resolution population data, school locations, and conflict event tracking, this project identifies critical areas where armed conflict threatens the continuity of learning.

## Data Transformation Pipeline

The data in this repository has been found through the data pipeline approach for the find and the get steps. While the data has been transformed and sometimes veryfied - the verify step -  with AI agent by creating the interactive Haiti map. 

**Explore the Interactive Map:** [https://ccasarini.github.io/exam-rfp-cc1/](https://ccasarini.github.io/exam-rfp-cc1/)

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
To analyze the security landscape, raw conflict data is transformed into a longitudinal dataset that supports trend analysis and spatial visualization.
- **Source:** UCDP GED (Uppsala Conflict Data Program).
- **Temporal Scope:** Data spans from **1999 to 2024** (the latest available), enabling a sliding timeline to track conflict evolution and assist in forecasting potential future escalations.
- **Geospatial Focus:** The analysis is localized to the **Ouest department**, capturing specific geocoded coordinates for each event.
- **Data Attributes:** Each record includes detailed information on conflict **participants**, specific **locations**, and the **best estimate of fatalities**.
- **AI-Driven Categorization:** By applying a custom classification algorithm (via Gemini) to raw media headlines, conflict events were grouped into 8 strategic categories:
    1. Targeted Assassinations and Political Repression
    2. Large-Scale Massacres and Neighborhood Raids
    3. Police Operations and State Security Clashes
    4. Inter-Gang Warfare (Inter-necine Conflict)
    5. Kidnappings and Sexual Violence
    6. Attacks on Strategic Infrastructure
    7. Civil Unrest and Protests
    8. Humanitarian Crisis and Mass Displacement.
- **Transformation:** `fetch_haiti_conflict_data.py` retrieves the data, and `convert_conflict_csv.py` converts the processed records into a GeoJSON format for mapping.
- **Output:** `data/armed_conflicts/ouest_conflict.geojson`.

---

## Repository Structure

- `data/`: Contains raw and processed datasets organized by category (borders, schools, population, conflicts).
- `scripts/`: Python scripts used for data acquisition, cleaning, and spatial transformation.
- `source.md`: Detailed documentation of the data sources and the rationale behind their selection.
