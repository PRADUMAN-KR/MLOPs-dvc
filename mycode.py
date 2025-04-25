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


df_new_row = {"name":"tom","age":25,"city":"NewYork"}
df.loc[len(df.index)] = df_new_row

df_new_row = {"name":"tobey","age":26,"city":"NewYork2"}
df.loc[len(df.index)] = df_new_row

# Step 3: Set file path
folder_path = "data"
file_name = "people.csv"
file_path = os.path.join(folder_path, file_name)

# Step 4: Ensure 'data' folder exists
os.makedirs(folder_path, exist_ok=True)

if os.path.exists(file_path):
    df_existing = pd.read_csv(file_path)
    
    # Find new rows not in the existing file
    df_combined = pd.concat([df_existing, df], ignore_index=True).drop_duplicates()
    
    if not df_combined.equals(df_existing):
        df_combined.to_csv(file_path, index=False)
        print(f"✅ File '{file_path}' updated with new rows.")
    else:
        print(f"ℹ️ No new rows to add. File '{file_path}' remains unchanged.")
else:
    df.to_csv(file_path, index=False)
    print(f"✅ File '{file_path}' created and saved.")