import pandas as pd
import numpy as np

from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

from data_cicids import load_and_clean_data


# ----------------------------
# LOAD DATA
# ----------------------------
df = load_and_clean_data()

# Separate
X = df.drop(columns=['Label'])
y = df['Label']

# ----------------------------
# TRAIN ONLY ON NORMAL DATA
# ----------------------------
normal_data = df[df['Label'] == 0]

X_normal = normal_data.drop(columns=['Label'])

print("Training on normal data:", X_normal.shape)

# ----------------------------
# TRAIN MODEL
# ----------------------------
model = IsolationForest(contamination=0.1, random_state=42)

model.fit(X_normal)

print("Anomaly model trained")

# ----------------------------
# TEST ON FULL DATA
# ----------------------------
pred = model.predict(X)

# Convert output:
# 1 → normal, -1 → anomaly
pred = [0 if p == 1 else 1 for p in pred]

# ----------------------------
# RESULTS
# ----------------------------
print("\nClassification Report:\n")
print(classification_report(y, pred))


# ----------------------------
# TEST ONE SAMPLE
# ----------------------------
sample = X.iloc[0:1]
result = model.predict(sample)

if result[0] == -1:
    print("\n⚠️ Suspicious / Unknown Pattern Detected")
else:
    print("\n✅ Normal Behavior")