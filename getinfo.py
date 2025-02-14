import os
import csv
import requests
from bs4 import BeautifulSoup as bs

# Define paths
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get script's directory
data_folder = os.path.join(script_dir, "Scraped Data")  # Folder with PDFs
links_file = os.path.join(script_dir, "nips_papers_link.txt")  # File with links
output_csv = os.path.join(script_dir, "papers_info.csv")  # CSV output file

# Read paper links from file
hash_link_map = {}
with open(links_file, "r", encoding="utf-8") as file:
    for line in file:
        if "/hash/" in line:
            hash_value = line.strip().split("/hash/")[1].split("-")[0]
            hash_link_map[hash_value] = line.strip()

# Prepare CSV file
with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Hash", "Title", "Abstract"])  # CSV Headers

    # Process each PDF in the Scraped Data folder
    for filename in os.listdir(data_folder):
        if filename.endswith("-Paper-Conference.pdf"):
            hash_value = filename.split("-")[0]  # Extract hash before first hyphen

            if hash_value in hash_link_map:
                paper_url = hash_link_map[hash_value]

                try:
                    # Request the page
                    response = requests.get(paper_url)
                    soup = bs(response.text, "html.parser")

                    # Extract title
                    title_tag = soup.find("h4")
                    title = title_tag.text.strip() if title_tag else "Title Not Found"

                    # Extract abstract
                    abstract_tag = soup.find("h4", string="Abstract")
                    abstract = abstract_tag.find_next("p").text.strip() if abstract_tag else "Abstract Not Found"

                    # Write to CSV
                    writer.writerow([hash_value, title, abstract])
                    print(f"Extracted: {hash_value}")

                except Exception as e:
                    print(f"Error processing {hash_value}: {e}")

print("Extraction completed. Check 'papers_info.csv'.")
