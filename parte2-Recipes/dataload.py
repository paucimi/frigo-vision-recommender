
import pandas as pd
import re
import os

# 1. Configuration
input_file = 'full_dataset.csv'
output_file = 'cleaned_dataset.csv'
chunk_size = 50000  # Adjust this (smaller if you still crash, larger for speed)

# 2. Define cleaning function
def clean_ingredients(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s,]', '', text)
    return text.strip()

# 3. Process in chunks
# Delete output file if it exists to avoid double-appending
if os.path.exists(output_file):
    os.remove(output_file)

print("Starting processing...")

# Create an iterator
chunks = pd.read_csv(input_file, chunksize=chunk_size)

for i, chunk in enumerate(chunks):
    # Apply cleaning to the current chunk only
    # Change 'ingredients' to your actual column name
    chunk['cleaned_ingredients'] = chunk['ingredients'].apply(clean_ingredients)
    
    # Append to the new file
    # header=True only for the first chunk
    chunk.to_csv(output_file, mode='a', index=False, header=(i==0))
    
    print(f"Finished chunk {i+1} ({((i+1)*chunk_size)} rows processed)")

print(f"Success! Cleaned data saved to: {output_file}")