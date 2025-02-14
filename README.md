📌 Overview

This project classifies research papers into predefined machine learning categories using Google's Gemini AI. Given a dataset with paper titles and abstracts, the model predicts one of the following categories:

Deep Learning

Computer Vision

Reinforcement Learning

NLP (Natural Language Processing)

Optimization

🔍 How It Works

Load Research Paper Data: Reads a CSV file containing Title and Abstract fields.

Use Google Gemini API: Sends each paper's title and abstract to the Gemini model.

Classification: The model returns one of the predefined categories.

Save Results: Outputs the classified dataset as a new CSV file.

🛠 Installation

Ensure you have Python 3.7+ installed.

Install Required Libraries

pip install pandas google-generativeai

Clone the Repository

git clone https://github.com/yourusername/ResearchPaperClassifier.git
cd ResearchPaperClassifier

🚀 Usage

Set Up Your API Key

Obtain a Google Gemini API key from Google AI Studio.

Replace MY_API_KEY in the code with your actual API key.

Run the Script

python classify_papers.py

📜 Code Structure

📂 ResearchPaperClassifier
├── 📄 classify_papers.py  # Main script
├── 📄 requirements.txt    # List of dependencies
├── 📂 data
│   ├── papers_raw.csv      # Input dataset
│   ├── papers_annotated.csv # Output dataset (after classification)
└── 📜 README.md            # Documentation (this file)

🔧 Troubleshooting

AttributeError: 'Client' object has no attribute 'generate_content'

Ensure you are using the correct method in Google Gemini API:

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt
)

Extra Column "Unnamed: 3" in CSV

Prevent this issue by modifying to_csv with:

df.to_csv(OUTPUT_CSV, index=False)

📌 Future Improvements

Support more categories.

Use fine-tuned LLMs for better accuracy.

Develop a web interface for easy classification.

📜 License

This project is licensed under the MIT License.

🤝 Contributing

Feel free to fork this repo and submit a pull request! Contributions are welcome. 😊
