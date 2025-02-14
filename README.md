# 📚 Research Paper Classifier using Google Gemini AI

## 🚀 Overview
This project classifies research papers into predefined **machine learning categories** using **Google Gemini AI**. The classification is based on the **title and abstract** of each paper. The results are stored in a CSV file for further analysis.

---

## 🎯 Features
- ✅ Uses **Google Gemini AI** for automatic classification
- ✅ Supports five categories: `Deep Learning`, `Computer Vision`, `Reinforcement Learning`, `NLP`, and `Optimization`
- ✅ Reads research paper data from a CSV file
- ✅ Ensures structured output and saves results to a new CSV file
- ✅ Processes a sample of **5 papers** for testing

---

## 🛠️ Setup & Installation
### 1️⃣ Install Dependencies
Make sure you have **Python 3.x** installed. Then, install required dependencies:
```bash
pip install pandas google-generativeai
```

### 2️⃣ Set Up Google Gemini AI
- Get an API key from [Google AI Studio](https://ai.google.dev/)
- Replace `MY_API_KEY` in the script with your actual API key

---

## 📜 Usage
### 1️⃣ Update File Paths
Modify the CSV file paths in the script to match your dataset location:
```python
CSV_FILE = "E:/Uni/6th Sem/Data Science/Assignment1/papers_raw.csv"
OUTPUT_CSV = "E:/Uni/6th Sem/Data Science/Assignment1/papers_annotated.csv"
```

### 2️⃣ Run the Script
Execute the Python script to classify the research papers:
```bash
python classify_papers.py
```

### 3️⃣ Check Output
After execution, the results will be saved in:
```
E:/Uni/6th Sem/Data Science/Assignment1/papers_annotated.csv
```
This file will contain an additional column `Category`, indicating the classified label.

---

## 🖥️ Code Explanation
### 🔹 Import Dependencies
```python
import pandas as pd
import os
from google import genai
```

### 🔹 Initialize Google Gemini API Client
```python
client = genai.Client(api_key="MY_API_KEY")
```

### 🔹 Define Categories
```python
CATEGORIES = ["Deep Learning", "Computer Vision", "Reinforcement Learning", "NLP", "Optimization"]
```

### 🔹 Classification Function
```python
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
    category = response.text.strip()
    return category
```

### 🔹 Load Dataset & Process Papers
```python
df = pd.read_csv(CSV_FILE)
if "Category" not in df.columns:
    df.insert(3, "Category", "")

df_sample = df.head(5).copy()
for index, row in df_sample.iterrows():
    df.loc[index, "Category"] = classify_paper(row["Title"], row["Abstract"])
```

### 🔹 Save Results
```python
df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8", quoting=1)
```

---

## 🐞 Troubleshooting
### ❌ Issue: `Unnamed: 3` column appears in CSV
**Fix:** Ensure the category values do not have extra spaces or newlines:
```python
df["Category"] = df["Category"].str.strip()
df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8", quoting=1)
```

---

## 📌 Future Improvements
- 🔹 Extend to more research categories
- 🔹 Process the full dataset instead of a sample
- 🔹 Improve classification accuracy with fine-tuned prompts

---

## 📄 License
This project is **open-source** and available under the MIT License.

---

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

Happy coding! 🚀

