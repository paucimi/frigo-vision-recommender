import pandas as pd
import ast

input_file = 'full_dataset.csv'
output_file = 'final_recipe_index.csv'
chunk_size = 50000

# This function converts the string "['salt', 'pepper']" into a real list ['salt', 'pepper']
def parse_ner(ner_string):
    try:
        return " ".join(ast.literal_eval(ner_string))
    except:
        return ""

# Process chunks
chunks = pd.read_csv(input_file, chunksize=chunk_size)

for i, chunk in enumerate(chunks):
    # 1. Clean the NER column: convert string-list to a simple space-separated string
    # This makes it ready for the Machine Learning Vectorizer later
    chunk['recipe_features'] = chunk['NER'].apply(parse_ner)
    
    # 2. Keep only the columns we need for the suggestion engine to save memory
    cols_to_keep = ['title', 'recipe_features', 'ingredients', 'directions', 'link']
    simplified_chunk = chunk[cols_to_keep]
    
    # 3. Save
    simplified_chunk.to_csv(output_file, mode='a', index=False, header=(i==0))
    print(f"Processed {i+1} chunks...")

print("Done! Your optimized dataset is ready in final_recipe_index.csv")
