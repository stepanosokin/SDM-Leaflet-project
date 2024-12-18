# SDM Leaflet Project

## Table of Contents
- [SDM Leaflet Project](#sdm-leaflet-project)
	- [Table of Contents](#table-of-contents)
	- [Description](#description)
	- [Installation](#installation)
	- [Usage](#usage)

## Description
This project was implemented as part of the Spatial Data Management course.

This project utilizes the Leaflet.js library to create interactive maps. The application is built using Flask, a lightweight WSGI web application framework in Python. The data used in this project includes various spatial datasets that are visualized on the map. Key libraries used in this project include:

- **Flask**: For creating the web application and handling HTTP requests.
- **Leaflet.js**: For rendering interactive maps.
- **pandas**: For data manipulation and analysis.
- **GeoPandas**: For working with geospatial data.
- **Folium**: For integrating Leaflet maps with Python.
- **rasterio**: For working with raster data.

The project demonstrates how to integrate these libraries to build a web-based spatial data visualization tool.

## Installation
To install this project, follow these steps:

1. Clone the repository:
	```bash
	git clone https://github.com/Danessely/SDM-Leaflet-project.git
	```
2. Navigate to the project directory:
	```bash
	cd SDM-project
	```
3. Create venv and install the dependencies:
	```bash
	python -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt
	```

## Usage
To use this project, follow these steps:

1. Start the application:
	```bash
	python app.py
	```
2. Open your browser and navigate to `http://127.0.0.1:5000/`.