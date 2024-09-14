import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (Make sure you have the appropriate ChromeDriver installed)
driver = webdriver.Chrome()

# Open the target website
driver.get('https://www.ratemyprofessors.com/search/professors/1349?q=*')

# Initialize WebDriverWait with a timeout
wait = WebDriverWait(driver, 10)

# Keep track of the professors' details
professors = []

# Scroll and load professors
while True:
    try:
        # Scroll down to load more content
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait for the new content to load
        time.sleep(2)

        # Try to find the "Load More" button (if it exists) and click it
        load_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Load More')]")))
        load_more_button.click()
        
    except Exception as e:
        print(f"No more 'Load More' button found or error occurred: {e}")
        break

# Collect professor details (Assuming each professor's info is inside an anchor tag with a specific href pattern)
professor_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/professor/')]")

# Iterate through each professor and gather their details
for professor in professor_elements:
    try:
        # Get the professor page URL
        professor_url = professor.get_attribute('href')
        driver.get(professor_url)
        
        # Wait for the professor's name to load
        name_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='NameTitle__Name-dowf0z-0']")))
        professor_name = name_element.text
        
        # Extract rating if available (using an appropriate XPath)
        try:
            rating_element = driver.find_element(By.XPATH, "//div[@class='RatingValue__Numerator-qw8sqy-2']")
            rating = rating_element.text
        except Exception as e:
            rating = "No rating"
            print(f"Rating not found for {professor_name}: {e}")
        
        # Add the professor's info to the list
        professors.append({'name': professor_name, 'rating': rating, 'url': professor_url})
        print(f"{professor_name} has been downloaded with rating {rating}")
        
    except Exception as e:
        print(f"Error occurred while processing professor: {e}")

    # Optionally go back to the main page (if scraping one by one from the list)
    driver.back()

# Close the browser after scraping
driver.quit()

# Write the scraped data to a CSV file
csv_file_path = 'professors.csv'
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'rating', 'url'])
    writer.writeheader()
    for professor in professors:
        writer.writerow(professor)

print(f"Data has been written to {csv_file_path}")
