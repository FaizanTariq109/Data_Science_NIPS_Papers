import os
import requests
from bs4 import BeautifulSoup as bs

# Define paths
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get script's directory
data_folder = os.path.join(script_dir, "Scraped Data")  # Define target folder

# Ensure the directory exists
os.makedirs(data_folder, exist_ok=True)

# Path to text file containing paper links
nips_links_file = os.path.join(script_dir, "nips_papers_link.txt")

# Read paper links from file
with open(nips_links_file, "r", encoding="utf-8") as file:
    paper_links = file.read().splitlines()

# Process each paper link
for paper_link in paper_links:
    try:
        # Request the page
        response = requests.get(paper_link)
        soup = bs(response.text, 'html.parser')

        # Find the paper download button
        paper_button = soup.select_one('a.btn.btn-primary.btn-spacer[href*="/paper_files/paper/"]')

        if paper_button:
            pdf_link = "https://papers.nips.cc" + paper_button["href"]
            pdf_filename = pdf_link.split("/")[-1]  # Extract filename from URL
            pdf_path = os.path.join(data_folder, pdf_filename)

            # Download the PDF
            pdf_response = requests.get(pdf_link)

            # Save the PDF file
            with open(pdf_path, "wb") as pdf_file:
                pdf_file.write(pdf_response.content)

            print(f"Downloaded: {pdf_filename}")

        else:
            print(f"No paper found for {paper_link}")

    except Exception as e:
        print(f"Error processing {paper_link}: {e}")

print("Download process completed.")