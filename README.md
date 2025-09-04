# London Bike Sharing Data Cleaning & Preparation

## 📌 Overview
This project focuses on cleaning and preparing the **London Bike Sharing dataset** for analysis and visualization. The goal is to transform raw data into a structured format that can be used in **Tableau** dashboards and other analytical workflows.

## 🚲 Dataset
- Source: [London Bike Sharing Dataset](https://www.kaggle.com/datasets/hmavrodiev/london-bike-sharing-dataset)  
- Contains hourly bike rental counts with associated **weather**, **temperature**, **season**, and **holiday/weekend** indicators.

## 🔧 Data Cleaning Steps
- Loaded dataset with `pandas`
- Renamed columns for clarity:
  - `cnt` → `count`
  - `t1` → `temp_real_C`
  - `t2` → `temp_feels_like_C`
  - `hum` → `humidity_percent`
  - `wind_speed` → `wind_speed_kph`
- Converted humidity from 0–100 scale to decimal (0–1)
- Mapped season codes to labels: `0=Spring, 1=Summer, 2=Autumn, 3=Winter`
- Mapped weather codes to labels (e.g., `1=Clear`, `7=Rain`, `26=Snowfall`)
- Exported the cleaned dataset to Excel for Tableau visualization

## 📂 Output
- `london_bikes_final.xlsx` – cleaned dataset ready for Tableau or other BI tools

## 📊 Example Use Case
This dataset was later used to build:
- **Interactive dashboards** (e.g., time-series trends, weather impact on ridership)
- **Exploratory analysis** (seasonality, peak riding hours, weather conditions)

## 🛠️ Tech Stack
- Python (pandas)
- Excel (final dataset export)
- Tableau (for visualization)
  ## 📊 Tableau Dashboard
You can interact with the live dashboard here:  
[London Bike Sharing Dashboard on Tableau Public](https://public.tableau.com/app/profile/mohamed.abdullah4356/viz/LondonBikeRides_17567181867180/LondonBikeRides)

  
![Tableau Viz Example](https://github.com/Mohamed-Abdullah-Data/bike-sharing-analysis/blob/0f666bd815bd1464fd0be753df9a2425824d7591/Screenshot%202025-09-01%20093756.png)
![Tableau Viz Example](https://github.com/Mohamed-Abdullah-Data/bike-sharing-analysis/blob/0f666bd815bd1464fd0be753df9a2425824d7591/Screenshot%202025-09-01%20093820.png)
![Tableau Viz Example](https://github.com/Mohamed-Abdullah-Data/bike-sharing-analysis/blob/0f666bd815bd1464fd0be753df9a2425824d7591/Screenshot%202025-09-01%20093832.png)

## 📧 Author
Created by *Mohamed Abdullah* – aspiring Data Analyst / Data Scientist.
