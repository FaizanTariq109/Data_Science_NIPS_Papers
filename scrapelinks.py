from bs4 import BeautifulSoup as bs
import requests as req

# Step 1: Get the HTML content of the main NeurIPS page
html_link = req.get('https://papers.nips.cc/').text
soup = bs(html_link, 'html.parser')

# Step 2: Extract year-wise paper links
nips_years = soup.select('div.col-sm ul li a')
nips_links = ["https://papers.nips.cc" + link['href'] for link in nips_years]

# Step 3: Extract individual paper links
nips_papers_link = []

for link in nips_links:
    year_page = req.get(link).text
    soup = bs(year_page, 'html.parser')

    # Extract correct paper links
    papers = soup.select('a[href*="/paper_files/paper/"]')

    # Append only the URLs (titles are ignored)
    nips_papers_link.extend(["https://papers.nips.cc" + paper['href'] for paper in papers])

# Save yearly links
with open("nips_links.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(nips_links))

# Save paper links
with open("nips_papers_link.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(nips_papers_link))

# Print confirmation
print(f"Extracted {len(nips_links)} yearly links and {len(nips_papers_link)} paper links.")
