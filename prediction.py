import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

from data_cicids import load_and_clean_data


# ----------------------------
# LOAD DATA
# ----------------------------
df = load_and_clean_data()

X = df.drop(columns=['Label'])
y = df['Label']

# ----------------------------
# SPLIT
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)

# ----------------------------
# MODEL
# ----------------------------
model = RandomForestClassifier(n_estimators=50, random_state=42)

model.fit(X_train, y_train)

print("\nModel trained successfully")

# ----------------------------
# PREDICT
# ----------------------------
y_pred = model.predict(X_test)

# ----------------------------
# RESULTS
# ----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


# ----------------------------
# TEST ONE SAMPLE
# ----------------------------
sample = X_test.iloc[0:1]
pred = model.predict(sample)

if pred[0] == 1:
    print("\n⚠️ Threat Detected")
else:
    print("\n✅ Normal Traffic")