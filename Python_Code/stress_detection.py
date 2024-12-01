import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load Stress Data
data = pd.read_csv("stress_data.csv")

# Convert data to numeric
for col in ["heart_rate", "skin_temp", "gsr"]:
    data[col] = pd.to_numeric(data[col], errors="coerce")
data = data.dropna()

# Train Unsupervised Model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(data)

# Detect Stress (Anomalies)
data["stress"] = model.predict(data)
data["stress"] = data["stress"].apply(lambda x: 1 if x == -1 else 0)

# Visualize Stress Levels
plt.figure(figsize=(12, 8))
plt.plot(data.index, data["heart_rate"], label="Heart Rate (BPM)")
plt.scatter(data.index[data["stress"] == 1], 
            data["heart_rate"][data["stress"] == 1], color="red", label="Detected Stress")
plt.legend()
plt.title("Heart Rate with Detected Stress Levels")
plt.show()
