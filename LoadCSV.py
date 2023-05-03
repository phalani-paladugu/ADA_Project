import pandas as pd
# Load JSON data from file
with open('data_Jan.json', 'r') as file:
    json_data = file.read()

# Convert JSON data to DataFrame
df = pd.read_json(json_data)

# Save DataFrame to CSV file
df.to_csv('data_Jan.csv', index=False)