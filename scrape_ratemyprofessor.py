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
wait = WebDriverWait(driver, 10)

# Close cookie consent banner
try:
    # Use the class name of the button to locate it
    cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='Buttons__Button-sc-19xdot-1 CCPAModal__StyledCloseButton-sc-10x9kq-2 eAIiLw']")))
    cookie_button.click()
    print("Cookie consent banner dismissed")
except Exception as e:
    print(f"Cookie banner not found or could not be dismissed: {e}")

# Proceed with your scraping logic here

# Example: Wait until the "Load More" button is present and continue scraping
try:
    load_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Load More')]")))
    load_more_button.click()
except Exception as e:
    print(f"Load more button not found: {e}")

# Close the driver at the end
driver.quit()


