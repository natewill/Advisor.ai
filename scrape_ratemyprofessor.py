import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the target website
driver.get('https://www.ratemyprofessors.com/search/professors/1349?q=*')

# Wait for the page to load
wait = WebDriverWait(driver, 15)

# Close cookie consent banner
try:
    cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept All Cookies')]")))
    cookie_button.click()
    print("Cookie consent banner dismissed")
except Exception as e:
    print(f"Cookie banner not found or could not be dismissed: {e}")

# Function to scrape professor data from the current page
def scrape_professors():
    professors = []
    cards = driver.find_elements(By.XPATH, "//div[@class='Card__StyledCard-sc-1gyrjd-0']")
    
    for card in cards:
        try:
            quality = card.find_element(By.XPATH, ".//div[contains(text(), 'QUALITY')]/following-sibling::div").text
            num_ratings = card.find_element(By.XPATH, ".//div[contains(text(), 'ratings')]").text.split()[0]
            prof_name = card.find_element(By.XPATH, ".//div[@class='CardName__StyledCardName-sc-1gyrjd-1']").text
            department = card.find_element(By.XPATH, ".//div[@class='CardSchool__Department-sc-1gyrjd-3']").text
            university = card.find_element(By.XPATH, ".//div[@class='CardSchool__School-sc-1gyrjd-4']").text
            would_take_again = card.find_element(By.XPATH, ".//div[contains(text(), '%')]").text
            difficulty = card.find_element(By.XPATH, ".//div[contains(text(), 'level of difficulty')]/preceding-sibling::div").text
            
            professors.append({
                'Quality Rating': quality,
                'Number of Ratings': num_ratings,
                'Professor Name': prof_name,
                'Department': department,
                'University': university,
                'Would Take Again': would_take_again,
                'Level of Difficulty': difficulty
            })
        except Exception as e:
            print(f"Error extracting data for one of the cards: {e}")
    
    return professors

# Example: Wait until the "Load More" button is present and continue scraping
all_professors = []
try:
    # First, scrape the data from the current page
    all_professors.extend(scrape_professors())
    
    # Try to load more data (if available) by clicking the "Load More" button multiple times
    while True:
        load_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Load More')]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", load_more_button)
        load_more_button.click()
        
        # Wait for the new content to load
        time.sleep(3)
        
        # Scrape data again after loading more content
        all_professors.extend(scrape_professors())
except Exception as e:
    print(f"No more 'Load More' button or scraping error: {e}")

# Save the scraped data into a CSV file
csv_file = 'professors_data.csv'
keys = ['Quality Rating', 'Number of Ratings', 'Professor Name', 'Department', 'University', 'Would Take Again', 'Level of Difficulty']

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(all_professors)

print(f"Data has been saved to {csv_file}")

# Close the driver at the end
driver.quit()



