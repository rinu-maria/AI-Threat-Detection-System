# AI Threat Detection System

An AI-powered cybersecurity threat detection and analytics system built using TensorFlow, Elasticsearch, and Kibana to detect, classify, and visualize suspicious network activity in real time.

---

# Project Overview

This project combines Machine Learning with the ELK Stack (Elasticsearch + Kibana) to simulate a SOC (Security Operations Center)-style cyber threat monitoring dashboard.

The system:
- Trains an AI model on cybersecurity traffic data
- Detects malicious vs normal traffic
- Classifies threat severity
- Stores detection results in Elasticsearch
- Visualizes attack analytics using Kibana dashboards

---

# Features

✅ AI-based threat detection  
✅ TensorFlow neural network model  
✅ Elasticsearch integration  
✅ Kibana dashboard visualization  
✅ Threat vs Normal traffic analysis  
✅ Country-wise attack monitoring  
✅ Source IP tracking  
✅ Severity classification  
✅ Traffic type analytics  
✅ Real-time style cyber monitoring dashboard  

---

#  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core development |
| TensorFlow | Machine Learning model |
| Pandas | Data preprocessing |
| Scikit-learn | Data splitting & preprocessing |
| Elasticsearch | Threat data storage |
| Kibana | Dashboard visualization |
| ELK Stack | Threat analytics platform |

---

# Project Structure

```bash
AI-Threat-Detection-System/
│
├── tensorflow_model.py
├── prediction.py
├── anomaly_detection.py
├── data_cicids.py
├── README.md
├── .gitignore
└── screenshots/
```

---

#  System Architecture

```text
Dataset
   ↓
Data Preprocessing
   ↓
TensorFlow AI Model
   ↓
Threat Prediction
   ↓
Elasticsearch Index
   ↓
Kibana Dashboard
```

---

# Dataset

This project uses cybersecurity network traffic datasets such as CICIDS2017.

Dataset is NOT included in this repository due to size limitations.

Download dataset from:

https://www.unb.ca/cic/datasets/ids-2017.html

After downloading:
1. Place dataset inside project folder
2. Update dataset path in code if necessary

---

# Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/rinu-maria/AI-Threat-Detection-System.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd AI-Threat-Detection-System
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install tensorflow pandas scikit-learn elasticsearch
```

---

#  Elasticsearch Setup

Download Elasticsearch:

https://www.elastic.co/downloads/elasticsearch

Navigate to Elasticsearch bin folder:

```bash
cd elasticsearch-8.x.x\bin
```

Run Elasticsearch:

```bash
elasticsearch.bat
```

Elasticsearch runs at:

```text
http://localhost:9200
```

---

# Kibana Setup

Download Kibana:

https://www.elastic.co/downloads/kibana

Navigate to Kibana bin folder:

```bash
cd kibana-8.x.x\bin
```

Run Kibana:

```bash
kibana.bat
```

Open Kibana:

```text
http://localhost:5601
```

---

#  Running AI Detection System

Inside project folder:

```bash
python tensorflow_model.py
```

The model will:
- Train on dataset
- Predict threats
- Send results to Elasticsearch

---

# Kibana Dashboard Visualizations

The dashboard displays:

- Threat Detected vs Normal Traffic
- Country-wise Attacks
- Severity Levels
- Traffic Type Analysis
- Source IP Monitoring
- Timestamp-based Threat Trends

---

#  Example Threat Types

- DDoS Attacks
- Port Scanning
- Brute Force Attempts
- Bot Traffic
- Suspicious Network Activity

---

---

#  Learning Outcomes

This project demonstrates:
- Machine Learning in Cybersecurity
- Threat Detection Systems
- ELK Stack Integration
- Kibana Dashboard Visualization
- Cyber Threat Analytics
- Security Monitoring Concepts

---

# ⚠️ Disclaimer

This project is created strictly for educational and research purposes only.

Do not use this project for unauthorized network monitoring or malicious activities.
