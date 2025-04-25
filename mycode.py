import pandas as pd
import os

# Step 1: Sample dictionary
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 22, 28],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
}

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Set file path
folder_path = "data"
file_name = "people.csv"
file_path = os.path.join(folder_path, file_name)

# Step 4: Ensure 'data' folder exists
os.makedirs(folder_path, exist_ok=True)

# Step 5: Check and save
if not os.path.exists(file_path):
    df.to_csv(file_path, index=False)
    print(f"✅ File '{file_path}' created and saved.")
else:
    print(f"⚠️ File '{file_path}' already exists. No action taken.")
