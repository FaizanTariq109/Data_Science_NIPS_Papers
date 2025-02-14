import pandas as pd
import os
from google import genai
import time

client = genai.Client(api_key="AIzaSyDuRu6KMvdw3XVvsu3UdNyiSrcYaAOETMs")

# Define the model and predefined categories
CATEGORIES = ["Deep Learning", "Computer Vision", "Reinforcement Learning", "NLP", "Optimization"]

# Path to the dataset
CSV_FILE = "E:/Uni/6th Sem/Data Science/Assignment1/papers_raw.csv"
OUTPUT_CSV = "E:/Uni/6th Sem/Data Science/Assignment1/papers_annotated.csv"

# Function to classify a paper using the LLM
def classify_paper(title, abstract):
    prompt = f"""
    You are an expert in machine learning research. Given the title and abstract of a paper, classify it into ONE of these categories: {', '.join(CATEGORIES)}.
    
    Title: {title}
    Abstract: {abstract}
    
    Return ONLY a single word from the provided list. Do NOT include any explanations, formatting, or extra words. Just return the category name.
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    category = response.text
    return category

# Load dataset
if not os.path.exists(CSV_FILE):
    print(f"File not found: {CSV_FILE}")
    exit()

df = pd.read_csv(CSV_FILE)

# Ensure required columns exist
if "Title" not in df.columns or "Abstract" not in df.columns:
    print("Dataset does not contain required columns: 'Title' and 'Abstract'.")
    exit()

if "Category" not in df.columns:
    df.insert(3, "Category", "")  # Insert at 4th position (index 3)

# Process only the first n rows for testing
df_sample = df.head(100).copy()

# Counter for progress tracking
counter = 0
sleep_counter = 1

# Classify each paper
for index, row in df_sample.iterrows():
    print(sleep_counter%15)
    if(sleep_counter%15 == 0):
        time.sleep(60)
    df.loc[index, "Category"] = classify_paper(row["Title"], row["Abstract"])
    counter += 1
    sleep_counter += 1
    print(f"Processed {counter}/100")

# Save results to a new file to avoid overwriting original data
df.to_csv(OUTPUT_CSV, index=False)
print(f"Classification complete for 100 entries. Results saved to {OUTPUT_CSV}")