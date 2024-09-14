import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# The base URL of the page to scrape
base_url = 'https://www.registrar.vt.edu/graduation-multi-brief/checksheets.html'  # Replace with the actual base URL of the page

# Send a GET request to the page
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Create a directory to save the PDFs if it doesn't already exist
os.makedirs('pdfs', exist_ok=True)

# Find all <a> tags within a <td> with text '2022/2023' and download the PDFs
for td in soup.find_all('td'):
    if '2022/2023' in td.text:
        link = td.find('a')
        if link and link.get('href'):
            pdf_url = link.get('href')
            # Construct the full URL if it's a relative path
            full_pdf_url = urljoin(base_url, pdf_url)

            if full_pdf_url.endswith('.pdf'):
                # Download the PDF
                pdf_response = requests.get(full_pdf_url)
                pdf_name = os.path.join('pdfs', pdf_url.split('/')[-1])

                # Save the PDF to the local directory
                with open(pdf_name, 'wb') as pdf_file:
                    pdf_file.write(pdf_response.content)
                    print(f"Downloaded {pdf_name}")
