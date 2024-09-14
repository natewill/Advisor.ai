""" from selenium import webdriver
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

 """
import csv

data = """Quality Rating,Number of Ratings,Professor Name,Department,University,Would Take Again,Level of Difficulty
4.7,82,Jason Sharp,Accounting,Virginia Tech,94%,2
1.3,9,Kimberly Walker,Accounting,Virginia Tech,0%,4.9
3.1,4,Fulton Galer,Accounting,Virginia Tech,50%,3.1
5.0,2,Dianna Ross,Accounting,Virginia Tech,N/A,2
5.0,1,France Belanger,Accounting,Virginia Tech,N/A,3
4.5,1,Sarah Stein,Accounting,Virginia Tech,N/A,3
0.0,0,Floyd Beams,Accounting,Virginia Tech,N/A,0
0.0,0,Reza Bharki,Accounting,Virginia Tech,N/A,0
0.0,0,Ling Lisic,Accounting,Virginia Tech,N/A,0
2.4,63,Cintia Easterwood,Accounting,Virginia Tech,35%,4.1
2.5,12,Marilyn Griffin,Accounting,Virginia Tech,N/A,4.1
2.5,12,John Brozovsky,Accounting,Virginia Tech,0%,4.5
4.1,8,Gregory Kogan,Accounting,Virginia Tech,88%,3.3
4.1,5,Adam Du Pon,Accounting,Virginia Tech,80%,3.4
5.0,4,Nadia Rogers,Accounting,Virginia Tech,100%,3.3
3.0,3,Jing Huang,Accounting,Virginia Tech,34%,3.8
5.0,1,Michele Meckfessel,Accounting,Virginia Tech,N/A,2
5.0,1,Marshall Vance,Accounting,Virginia Tech,100%,3
5.0,1,Ryan Musselman,Accounting,Virginia Tech,100%,2
5.0,1,Wenqi Shen,Accounting,Virginia Tech,100%,4
0.0,0,Mike Truelsen,Accounting,Virginia Tech,N/A,0
0.0,0,Frank Galer,Accounting,Virginia Tech,N/A,0
0.0,0,Matt Cobabe,Accounting,Virginia Tech,N/A,0
3.5,2,Reza Barkhi,Accounting,Virginia Tech,0%,3.5
4.0,2,Donald Compton,Accounting,Virginia Tech,100%,3
5.0,2,E Scott Johnson,Accounting,Virginia Tech,100%,2
1.0,1,Christie Hayne,Accounting,Virginia Tech,0%,4
0.0,0,Ryan Hamilton,Accounting,Virginia Tech,N/A,0
0.0,0,Noah Ehreth,Accounting,Virginia Tech,N/A,0
0.0,0,Sean Hillison,Accounting,Virginia Tech,N/A,0
2.7,132,Jean Lacoste,Accounting,Virginia Tech,84%,3.2
1.4,13,David Tegarden,Accounting,Virginia Tech,0%,5
5.0,6,Randal Gatzke,Accounting,Virginia Tech,100%,3.6
3.5,2,Matthew Cobabe,Accounting,Virginia Tech,50%,3
4.1,20,Lynn Almond,Accounting,Virginia Tech,73%,3.9
4.9,17,Matthew Erickson,Accounting,Virginia Tech,89%,5
3.1,12,James Yardley,Accounting,Virginia Tech,N/A,3.8
2.9,4,Linda Wallace,Accounting,Virginia Tech,75%,3.8
4.6,4,Michelle Harding,Accounting,Virginia Tech,100%,3.6
3.0,3,Dana Garner,Accounting,Virginia Tech,67%,3.4
3.7,3,Francis Ding,Accounting,Virginia Tech,67%,3.3
1.0,1,Jonathan DiYorio,Accounting,Virginia Tech,0%,5
5.0,1,Greg Jenkins,Accounting,Virginia Tech,N/A,3
1.5,1,Sarah Asebedo,Accounting,Virginia Tech,N/A,4
"""

# Specify the file path
file_path = 'professor_ratings.csv'

# Write data to CSV file
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    file.write(data)

print(f"Data has been written to {file_path}")
