# GeoPulse – Hyper-Local Retail Mobility Analytics

**Project 2 | Infotact Solutions**

> Transforming anonymized mobility data into intelligent retail location decisions through geospatial analytics.

## 1. Project Overview

GeoPulse is a geospatial retail mobility analytics platform designed to help retail businesses understand customer movement patterns, analyze store footfall, identify high-traffic areas, and evaluate potential store locations.

The system processes simulated anonymized mobile GPS data using spatial data engineering and analytics technologies. It combines Snowflake, Apache Sedona, PySpark, dbt, Kepler.gl, and React to transform raw GPS coordinates into meaningful retail intelligence.

## 2. Problem Statement

Retail businesses often make store expansion decisions using static demographic information and traditional market research.

However, they lack insights into how people actually move throughout a city during different times of the day.

This creates challenges such as:

- Selecting unsuitable locations for new stores.
- Missing high-footfall areas.
- Overlapping customer catchment areas.
- Cannibalization of existing store traffic.
- Difficulty understanding hourly mobility patterns.

GeoPulse addresses these challenges through geospatial data processing and interactive mobility analytics.

## 3. Project Objectives

- Generate large-scale synthetic mobile GPS datasets.
- Analyze anonymized device movement patterns.
- Store and process geographical coordinates efficiently.
- Identify store catchment areas using 500-meter spatial boundaries.
- Calculate unique visitors for each store.
- Analyze hourly and daily footfall patterns.
- Identify potential customer overlap between retail locations.
- Visualize mobility patterns through interactive geospatial dashboards.
- Support data-driven retail site selection decisions.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | GPS data generation and preprocessing |
| Pandas | Data manipulation and validation |
| NumPy | Synthetic data generation |
| Snowflake | Geospatial data warehouse |
| GEOGRAPHY | Storage of geographical coordinates |
| Apache Sedona | Distributed spatial processing |
| PySpark | Large-scale data processing |
| dbt | Data transformation and modeling |
| SQL | Analytical queries |
| Kepler.gl | Geospatial visualization |
| React | Interactive dashboard frontend |
| GitHub | Version control and collaboration |

## 5. System Architecture

```text
Synthetic GPS Data Generation
             |
             v
      Python / Pandas
             |
             v
       GPS CSV Dataset
             |
             v
          Snowflake
       (Raw GPS Storage)
             |
             v
    Apache Sedona / PySpark
       (Spatial Joins)
             |
             v
          dbt Models
     (Data Transformation)
             |
             v
     Aggregated Footfall Data
             |
             v
       Kepler.gl / React
             |
             v
     Interactive GeoPulse
          Dashboard
             |
             v
   Retail Location Intelligence
```

## 6. Dataset Description

The project initially uses a synthetic GPS mobility dataset.

### Raw GPS Dataset

| Column | Data Type | Description |
|---|---|---|
| DeviceID | String | Unique simulated device identifier |
| Latitude | Float | GPS latitude coordinate |
| Longitude | Float | GPS longitude coordinate |
| Timestamp | Datetime | Date and time of GPS ping |

### Initial Dataset Target

| Parameter | Target |
|---|---|
| Simulated devices | 10,000 |
| Initial GPS records | 1,000,000 |
| Ping interval | 5 minutes |
| Geographic coverage | Selected city area |
| Data format | CSV |
| Data source | Synthetic / Simulated |

*Dataset size and simulation parameters may be expanded during development.*

## 7. Week-wise Development Roadmap

### Week 1 – Data Generation and Snowflake Setup

**Spatial Data Engineering**
- Generate synthetic GPS mobility data.
- Simulate device movement across a city.
- Export GPS records into CSV format.

**Geospatial BI**
- Set up Snowflake.
- Create the database and RAW schema.
- Create tables with GEOGRAPHY data types.
- Upload and load raw GPS data into Snowflake.

**Expected Output:** Synthetic GPS dataset successfully stored in Snowflake.

### Week 2 – Spatial Joins and ELT Modeling

**Spatial Data Engineering**
- Configure Apache Sedona / PySpark.
- Create 500-meter catchment-area polygons around retail locations.
- Perform spatial joins between GPS points and store polygons.

**Geospatial BI**
- Configure dbt with Snowflake.
- Create transformation models.
- Aggregate unique visitors per store per hour.

**Expected Output:** Processed GPS data with store-level hourly visitor metrics.

### Week 3 – Cannibalization Analysis and Dashboard

**Spatial Data Engineering**
- Analyze unique DeviceIDs visiting multiple stores.
- Calculate customer overlap between retail locations.
- Develop cannibalization analysis logic.

**Geospatial BI**
- Integrate Kepler.gl into a React frontend.
- Connect the dashboard to Snowflake aggregated tables.
- Develop interactive mobility maps.

**Expected Output:** Interactive geospatial dashboard with store footfall and customer overlap insights.

### Week 4 – Automation and Final Refinement

**Spatial Data Engineering**
- Configure Apache Airflow to orchestrate PySpark and dbt jobs.
- Automate daily data processing.

**Geospatial BI**
- Configure a 3D H3 Hexagon map using Uber's grid system.
- Add animated foot traffic visualization.
- Implement a 24-hour time slider.

**Expected Output:** Automated geospatial analytics pipeline and interactive 3D mobility dashboard.

## 8. Team Responsibilities

| Team Member | Primary Responsibility | Technologies |
|---|---|---|
| Member 1 | Synthetic GPS data generation | Python, Pandas, NumPy |
| Member 2 | GPS validation and movement simulation | Python, Pandas, Matplotlib |
| Member 3 | Snowflake database and schema setup | Snowflake, SQL |
| Member 4 | GPS data loading and integration | Snowflake, SQL, Python |

*Responsibilities can be expanded and adjusted as the project progresses.*

## 9. Initial Project Folder Structure

```text
GeoPulse/
│
├── data/
│   ├── sample_gps_pings.csv
│   └── README.md
│
├── scripts/
│   ├── generate_gps_data.py
│   ├── validate_gps_data.py
│   └── visualize_gps_data.py
│
├── sql/
│   ├── snowflake_setup.sql
│   ├── create_tables.sql
│   ├── create_stage.sql
│   └── load_gps_data.sql
│
├── reports/
│   ├── data_generation_summary.md
│   ├── data_quality_report.md
│   └── snowflake_loading_report.md
│
├── visualizations/
│   └── gps_movement_preview.png
│
├── docs/
│   ├── architecture.md
│   ├── data_dictionary.md
│   └── week1_progress.md
│
├── requirements.txt
└── README.md
```

## 10. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### Step 2: Navigate to the Project

```bash
cd GeoPulse
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run GPS Data Generation

```bash
python scripts/generate_gps_data.py
```

## 11. Expected Final Outcome

GeoPulse aims to deliver an end-to-end geospatial retail mobility analytics solution capable of:

- Processing large-scale GPS mobility datasets.
- Identifying footfall around retail locations.
- Measuring unique visitors and hourly traffic.
- Detecting potential customer cannibalization.
- Visualizing movement patterns on interactive 2D and 3D maps.
- Supporting retail expansion and location selection decisions.

## 12. Project Status

**Current Phase:** Week 1 – Data Generation and Snowflake Setup

**Development Status:** Initial Setup / In Progress

Upcoming milestones:
- [ ] Synthetic GPS dataset generation.
- [ ] GPS validation and visualization.
- [ ] Snowflake database configuration.
- [ ] Raw GPS data ingestion.
- [ ] Spatial joins and catchment-area analysis.
- [ ] dbt ELT modeling.
- [ ] Cannibalization analysis.
- [ ] Interactive dashboard development.
- [ ] Pipeline automation.

## 13. Team Collaboration

All team members contribute through the shared GitHub repository.

Development workflow:

1. Create a separate branch for assigned work.
2. Commit code and documentation regularly.
3. Push changes to GitHub.
4. Create Pull Requests.
5. Review and merge approved changes into the main branch.

## 14. Acknowledgement

Developed as part of the **Infotact Solutions Project-Based Internship**.

**Project Name:** GeoPulse – Hyper-Local Retail Mobility Analytics

**Domain:** Retail Strategy & Geospatial Analytics

---

*GeoPulse – Turning Mobility Data into Smarter Retail Decisions.*
