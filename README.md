# AI-Powered Predictive Maintenance System for IoT Devices

## Overview

This project implements a **machine learning–based predictive maintenance system** that analyzes simulated IoT sensor data to detect early signs of industrial machine failures.

Predictive maintenance helps industries avoid unexpected machine breakdowns by analyzing sensor data and predicting failures before they occur.

The system trains a **Random Forest machine learning model** to classify machines as **normal or likely to fail**, based on sensor readings such as temperature, rotational speed, torque, and tool wear.

---

# Problem Statement

In industrial environments, unexpected equipment failures can cause:

* Production downtime
* Increased maintenance costs
* Safety risks
* Reduced operational efficiency

Traditional maintenance approaches include:

* **Reactive maintenance** – fixing machines after they break
* **Preventive maintenance** – servicing machines at fixed intervals

Both approaches are inefficient.

Predictive maintenance uses **data-driven machine learning models** to predict failures in advance.

---

# Solution

This project builds a predictive maintenance pipeline that:

1. Collects machine sensor data
2. Preprocesses and cleans the dataset
3. Trains a machine learning model
4. Predicts machine failures
5. Generates performance metrics
6. Visualizes sensor relationships and predictions

The system helps identify **machines at risk of failure before breakdown occurs.**

---

# Dataset

Dataset used:

**AI4I 2020 Predictive Maintenance Dataset**

The dataset simulates sensor data from industrial machines.

### Features

| Sensor              | Description                              |
| ------------------- | ---------------------------------------- |
| Air temperature     | Environmental temperature around machine |
| Process temperature | Temperature during machine operation     |
| Rotational speed    | RPM of machine motor                     |
| Torque              | Rotational force                         |
| Tool wear           | Tool degradation over time               |

### Target Variable

```
Machine failure
```

Values:

```
0 = Normal operation
1 = Machine failure
```

---

# Project Architecture

```
IoT Sensor Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Machine Learning Model
(Random Forest)
        │
        ▼
Failure Prediction
        │
        ▼
Visualization & Analysis
```

---

# Tech Stack

Programming Language

* Python

Libraries Used

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

Development Tools

* VS Code
* Git
* GitHub

---

# Machine Learning Model

Model used:

```
Random Forest Classifier
```

Why Random Forest?

* Handles structured data well
* Robust against overfitting
* Works well for classification problems
* Provides feature importance insights

---

# Results

Model performance:

```
Accuracy ≈ 90% – 99%
```

The model successfully identifies machine failures with high accuracy and minimal false alarms.

---

# Visualizations

The project generates several visual analytics graphs:

### Confusion Matrix

Shows correct and incorrect predictions.

![Confusion Matrix](images/confusion_matrix.png)

---

### Failure Distribution

Shows the distribution of normal vs failed machines.

![Failure Distribution](images/failure_distribution.png)

---

### Sensor Correlation Heatmap

Displays relationships between sensor variables.

![Correlation Heatmap](images/correlation_heatmap.png)

---

### Feature Importance

Shows which sensor features influence failure predictions the most.

![Feature Importance](images/feature_importance.png)

---

### Sensor Trends

Shows how sensor values vary over time.

![Sensor Trends](images/sensor_trends.png)

---

# Project Structure

```
AI-Predictive-Maintenance-IoT
│
├── data
│   └── predictive_maintenance.csv
│
├── src
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── train_model.py
│   ├── predict.py
│   └── visualize.py
│
├── images
│   ├── confusion_matrix.png
│   ├── failure_distribution.png
│   ├── correlation_heatmap.png
│   ├── feature_importance.png
│   └── sensor_trends.png
│
├── models
│   └── predictive_model.pkl
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```
git clone https://github.com/YOUR_USERNAME/AI-Predictive-Maintenance-IoT.git
```

Navigate to project folder

```
cd AI-Predictive-Maintenance-IoT
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Run the Project

Run the main program

```
python main.py
```

The script will:

* Train the machine learning model
* Evaluate model performance
* Generate visualizations
* Save the trained model

---

# Output

The project generates:

* Machine failure predictions
* Model evaluation metrics
* Visualization graphs
* Saved trained model

Generated files:

```
models/predictive_model.pkl
images/*.png
```

---

# Industry Applications

Predictive maintenance systems like this are used in:

* Manufacturing plants
* Power plants
* Automotive industry
* Aviation maintenance
* Smart factories

Companies use similar systems to reduce downtime and maintenance costs.

---

# Future Improvements

Possible enhancements:

* Real-time IoT sensor data simulation
* Deep learning models for time-series prediction
* Streamlit dashboard for interactive monitoring
* Anomaly detection systems
* Deployment as a web application

---

# Author

Priyanka Badagavi

Engineering Student | Machine Learning Enthusiast

GitHub:
https://github.com/priyankabadagavi101-png
