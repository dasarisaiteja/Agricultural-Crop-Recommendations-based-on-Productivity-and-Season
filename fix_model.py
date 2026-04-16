import pandas as pd
from sklearn.ensemble import RandomForestClassifier # Changed to Random Forest
import pickle
import os

# 1. Load your data
print("Reading data...")
df = pd.read_csv('Data/crop_recommendation.csv')

# 2. Split data (using 'label' as the target)
X = df.drop('label', axis=1)
y = df['label']

# 3. Train a Random Forest model (this is likely what app.py wants)
print("Training new Random Forest model...")
model = RandomForestClassifier() 
model.fit(X, y)

# 4. Save it as RandomForest.pkl
model_path = 'models/RandomForest.pkl' 
os.makedirs('models', exist_ok=True)

with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"✅ Success! New model saved to {model_path}")