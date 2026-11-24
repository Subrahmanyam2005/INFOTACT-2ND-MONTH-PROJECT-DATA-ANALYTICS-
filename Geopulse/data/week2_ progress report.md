Week 2 – Spatial Data Preparation and Validation

Objective

To prepare GPS and store datasets for spatial analysis by converting geographic coordinates into projected coordinates, creating point geometries and validating the prepared spatial data.

Work Completed

Spatial Data Preparation

Worked on preparing GPS and store datasets for spatial operations.

Loaded the datasets using Python and Pandas.

Implemented coordinate validation and data-cleaning checks.

Separated invalid and duplicate records for further examination.

Coordinate Reference System Transformation

Used PyProj to transform geographic coordinates from EPSG:4326 to EPSG:32644 (WGS 84 / UTM Zone 44N).

Generated projected UTM_X and UTM_Y coordinates in metres.

Prepared the data for distance-based spatial operations.

Geometry Creation

Generated WKT point geometries using projected coordinates.

Created spatial point representations for GPS records and retail stores.

Prepared the datasets for store catchment analysis.

Spatial Data Validation

Developed a separate validation workflow.

Checked missing spatial values and invalid coordinate ranges.

Validated project-area boundaries.

Checked duplicate PingIDs and StoreIDs.

Verified UTM coordinate transformations against the original latitude and longitude.

Checked WKT geometry consistency.

Generated record-level validation statuses and failure reasons.

Output Management

Configured automatic output-directory creation in Google Colab.

Prepared CSV output workflows for cleaned GPS records, store records, rejected records, duplicate records and validation summaries.

Corrected execution issues involving __file__ and an undefined coordinate transformer.

Scripts Developed

prepare_spatial_data.py

validate_spatial_data.py

Planned Output Files

gps_points_utm.csv

store_points_utm.csv

gps_rejected.csv

gps_duplicates.csv

stores_rejected.csv

stores_duplicates.csv

preparation_summary.csv

gps_spatial_validation.csv

store_spatial_validation.csv

spatial_validation_summary.csv

Week 2 Outcome

Developed the spatial preparation and validation workflows required to convert the original GPS and store datasets into projected spatial datasets. Prepared the data-processing outputs for the next stage of spatial analysis.

Skills and Technical Concepts Applied

Python programming and data processing

Pandas and NumPy

Data profiling and data-quality validation

Missing-value and duplicate detection

Geographic coordinate systems

Coordinate Reference System (CRS) transformation

EPSG:4326 and EPSG:32644

UTM coordinate conversion

WKT point geometry creation

Spatial data validation

Google Colab execution and output management

Overall Progress – First Two Weeks

During the first two weeks, my primary responsibility was understanding, preparing and validating the GPS movement and retail store datasets.

In Week 1, I focused on dataset profiling and initial data-quality checks. In Week 2, I progressed to spatial data preparation, coordinate transformation, geometry creation and spatial validation.

These activities establish the data foundation required for the upcoming store catchment creation, GPS-to-store spatial joins and footfall analysis.

My individual contribution: Dataset profiling, initial validation, spatial data preparation, coordinate transformation, point geometry creation, spatial validation and preparation of output reports.
