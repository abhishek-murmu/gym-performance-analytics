# Gym Performance Analytics System

A Python-based fitness analytics project built to track workout progression, analyze exercise performance, and compare historical gym data using data analysis and visualization techniques.

This project uses Excel-based workout logs and performs performance comparison using Python libraries such as Pandas, Matplotlib, and Seaborn.

---

# Features

- Workout tracking using Excel datasets
- Exercise-wise weight progression analysis
- Reps improvement comparison
- Workout frequency tracking
- Heatmap visualization for workout statistics
- Average workout duration analysis
- Historical workout comparison system
- Automatic performance improvement detection

---

# Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Excel (.xlsx)

---

# Project Structure

```bash
GYM_TRACKER/
│
├── gym_logs.xlsx
├── analysis.py
└── README.md
```

---

# Dataset Information

This project uses a personally maintained workout dataset stored in an Excel file (`gym_logs.xlsx`).

The original dataset has not been uploaded to this repository because it contains personal workout records and private fitness tracking data.

A sample dataset structure is shown below for reference purposes only:

| Date | Exercise | Sets | Reps | Weight_kg | Duration_min |
|------|-----------|------|------|------------|---------------|
| 2026-05-18 | Bench Press | 4 | 8 | 75 | 90 |
| 2026-05-18 | Squat | 5 | 5 | 100 | 110 |

---

# Installation

Install required dependencies:

```bash
pip install pandas matplotlib seaborn openpyxl
```

---

# How to Run

Run the analysis script:

```bash
python analysis.py
```

---

# Analysis Performed

## Basic Analysis

The project performs:
- Average workout duration calculation
- Longest workout detection
- Top weight lifted per exercise
- Exercise-wise statistics aggregation

---

# Visualizations

## Workout Heatmap

The heatmap visualizes:
- Average sets
- Average reps
- Average weight lifted
- Average workout duration

using statistical aggregation and color-based comparisons.

---

## Workout Frequency Analysis

Tracks workout consistency over time using date-based trend visualization.

---

# Performance Comparison System

The project compares:
- Latest workout vs previous workout
- Weight progression across exercises
- Reps progression across exercises

Example output:

```text
Bench Press: +5.0 kg improvement
Squat: No change in weight

Bench Press: +2 reps improvement
Lat Pulldown: -1 reps decrease
```

---

# Libraries Used

## Pandas
Used for:
- Reading Excel data
- Data cleaning
- Grouping and aggregation
- Historical comparison analysis

## Matplotlib
Used for:
- Data visualization
- Workout trend plotting
- Workout frequency graphs

## Seaborn
Used for:
- Statistical heatmap generation
- Advanced visualization styling

---

# Future Improvements

- Interactive dashboard using Streamlit
- Personal Record (PR) tracker
- Monthly workout analytics
- Exercise progression dashboards
- Export analysis reports to PDF
- Advanced statistical analysis using NumPy

---

# Author

Abhishek Murmu
