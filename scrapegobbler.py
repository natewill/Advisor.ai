from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

import time
driver = webdriver.Chrome()

# Open the target website
driver.get('https://gobblerconnect.vt.edu/organizations')  # Replace with the actual URL

# Wait until the "Load More" button is present
wait = WebDriverWait(driver, 5)

# Click the "Load More" button until all clubs are loaded
for i in range(2):
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        load_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Load More')]")))
        driver.execute_script("arguments[0].click();", load_more_button)
        time.sleep(2)  # Wait for the new content to load
    except:
        # Break the loop if there's no more "Load More" button to click
        break

# After loading all clubs, collect the clubs' links
club_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/organization/')]")
club_urls = [link.get_attribute('href') for link in club_links]

club_descriptions = []

for club_url in club_urls:
    driver.get(club_url)
    
    # Wait for the description to be present and get it
    try:
        description_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'bodyText-large userSupplied')]/p")))
        description = description_element.text
        club_name = driver.find_element(By.XPATH, "//h1").text  # Assuming the club name is in <h1> tag
        club_descriptions.append({'name': club_name, 'description': description})
    except Exception as e:
        print(f"Description not found for {club_url}: {e}")
    
    # Optionally, go back to the main page
    driver.back()
    time.sleep(1)  # Wait for the page to load

# Print or process the club descriptions
for club in club_descriptions:
    print(f"Club Name: {club['name']}")
    print(f"Description: {club['description']}\n")

# Close the browser
driver.quit()
