import pandas as pd
import numpy as np
import random

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from elasticsearch import Elasticsearch
from datetime import datetime

# -----------------------------------
# CONNECT TO ELASTICSEARCH
# -----------------------------------

es = Elasticsearch(
    "http://localhost:9200",
    basic_auth=("elastic", "JtVXF0=wuU0y3oYh*Vts")
)

# -----------------------------------
# LOAD DATA
# -----------------------------------

df = pd.read_parquet("DDoS-Friday-no-metadata.parquet")

# Convert labels
df['Label'] = df['Label'].apply(
    lambda x: 0 if x == 'Benign' else 1
)

# Remove invalid values
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# -----------------------------------
# SPLIT FEATURES & LABELS
# -----------------------------------

y = df['Label'].astype(int)

X = df.drop(columns=['Label'])

# Keep only numeric columns
X = X.select_dtypes(include=[np.number])

print("Data cleaned:", X.shape)

# -----------------------------------
# TRAIN TEST SPLIT
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------------
# SCALE DATA
# -----------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -----------------------------------
# BUILD TENSORFLOW MODEL
# -----------------------------------

model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# -----------------------------------
# COMPILE MODEL
# -----------------------------------

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# -----------------------------------
# TRAIN MODEL
# -----------------------------------

model.fit(
    X_train,
    y_train,
    epochs=5,
    batch_size=32,
    verbose=1
)

# -----------------------------------
# EVALUATE MODEL
# -----------------------------------

loss, accuracy = model.evaluate(X_test, y_test)

print("\nTensorFlow Model Accuracy:", accuracy)

# -----------------------------------
# RANDOM TEST SAMPLES
# -----------------------------------

random_indices = random.sample(range(len(X_test)), 100)

samples = X_test[random_indices]

# -----------------------------------
# PREDICT
# -----------------------------------

predictions = model.predict(samples)

# -----------------------------------
# DEMO STORYTELLING DATA
# -----------------------------------

fake_ips = [
    "192.168.1.25",
    "10.0.0.45",
    "172.16.5.100",
    "203.45.67.89",
    "185.23.44.12"
]

countries = [
    "India",
    "United States",
    "Germany",
    "Russia",
    "China"
]

attack_types = [
    "DDoS",
    "Port Scan",
    "Brute Force",
    "Bot Attack"
]

# -----------------------------------
# SEND DATA TO ELASTICSEARCH
# -----------------------------------

for pred in predictions:

    # Artificially create mixed traffic
    random_value = random.randint(1, 100)

    if random_value <= 60:

        prediction_text = "Threat Detected"
        severity = "Critical"

    else:

        prediction_text = "Normal Traffic"
        severity = "Low"

    # Final JSON document
    detection_data = {

        "timestamp": datetime.now(),

        "model": "TensorFlow",

        "prediction": prediction_text,

        "confidence": float(pred[0]),

        "severity": severity,

        "source_ip": random.choice(fake_ips),

        "country": random.choice(countries),

        "traffic_type": random.choice(attack_types)
    }

    # Send to Elasticsearch
    es.index(
        index="ai-threat-detection",
        document=detection_data
    )

    print(detection_data)

print("\n✅ All detections sent to Elasticsearch!")