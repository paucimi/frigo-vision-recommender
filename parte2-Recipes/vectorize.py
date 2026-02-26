import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load the cleaned dataset
# If it's still too slow, you can use nrows=100000 to test first
df = pd.read_csv('final_recipe_index.csv')
df['recipe_features'] = df['recipe_features'].fillna('')

print("Vectorizing ingredients... (this may take a minute)")
# 2. Setup TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['recipe_features'])

def suggest_recipes(user_ingredients, top_n=5):
    # 3. Transform user input into the same numerical format
    user_vec = tfidf.transform([user_ingredients.lower()])
    
    # 4. Calculate Cosine Similarity between input and all recipes
    similarity_scores = cosine_similarity(user_vec, tfidf_matrix).flatten()
    
    # 5. Get indices of the top N highest scores
    top_indices = similarity_scores.argsort()[-top_n:][::-1]
    
    return df.iloc[top_indices]

# --- PROBANDOLO AHORA ---
my_fridge = "tomato, cheese, lettuce, potatos, rice"
suggestions = suggest_recipes(my_fridge)

print(f"\nTop suggestions for: {my_fridge}")
print(suggestions[['title', 'directions', 'link']])
