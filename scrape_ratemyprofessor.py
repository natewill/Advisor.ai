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

data = """Professor Name,Department,University,Quality Rating,Number of Ratings,Would Take Again,Level of Difficulty
Jason Sharp,Accounting,Virginia Tech,4.7,82,94%,2
Kimberly Walker,Accounting,Virginia Tech,1.3,9,0%,4.9
Fulton Galer,Accounting,Virginia Tech,3.1,4,50%,3.1
Dianna Ross,Accounting,Virginia Tech,5.0,2,N/A,2
France Belanger,Accounting,Virginia Tech,5.0,1,N/A,3
Sarah Stein,Accounting,Virginia Tech,4.5,1,N/A,3
Floyd Beams,Accounting,Virginia Tech,0.0,0,N/A,0
Reza Bharki,Accounting,Virginia Tech,0.0,0,N/A,0
Ling Lisic,Accounting,Virginia Tech,0.0,0,N/A,0
Cintia Easterwood,Accounting,Virginia Tech,2.4,63,35%,4.1
Marilyn Griffin,Accounting,Virginia Tech,2.5,12,N/A,4.1
John Brozovsky,Accounting,Virginia Tech,2.5,12,0%,4.5
Gregory Kogan,Accounting,Virginia Tech,4.1,8,88%,3.3
Adam Du Pon,Accounting,Virginia Tech,4.1,5,80%,3.4
Nadia Rogers,Accounting,Virginia Tech,5.0,4,100%,3.3
Jing Huang,Accounting,Virginia Tech,3.0,3,34%,3.8
Michele Meckfessel,Accounting,Virginia Tech,5.0,1,N/A,2
Marshall Vance,Accounting,Virginia Tech,5.0,1,100%,3
Ryan Musselman,Accounting,Virginia Tech,5.0,1,100%,2
Wenqi Shen,Accounting,Virginia Tech,5.0,1,100%,4
Mike Truelsen,Accounting,Virginia Tech,0.0,0,N/A,0
Frank Galer,Accounting,Virginia Tech,0.0,0,N/A,0
Matt Cobabe,Accounting,Virginia Tech,0.0,0,N/A,0
Reza Barkhi,Accounting,Virginia Tech,3.5,2,0%,3.5
Donald Compton,Accounting,Virginia Tech,4.0,2,100%,3
E Scott Johnson,Accounting,Virginia Tech,5.0,2,100%,2
Christie Hayne,Accounting,Virginia Tech,1.0,1,0%,4
Ryan Hamilton,Accounting,Virginia Tech,0.0,0,N/A,0
Noah Ehreth,Accounting,Virginia Tech,0.0,0,N/A,0
Sean Hillison,Accounting,Virginia Tech,0.0,0,N/A,0
Jean Lacoste,Accounting,Virginia Tech,2.7,132,84%,3.2
David Tegarden,Accounting,Virginia Tech,1.4,13,0%,5
Randal Gatzke,Accounting,Virginia Tech,5.0,6,100%,3.6
Matthew Cobabe,Accounting,Virginia Tech,3.5,2,50%,3
Lynn Almond,Accounting,Virginia Tech,4.1,20,73%,3.9
Matthew Erickson,Accounting,Virginia Tech,4.9,17,89%,5
James Yardley,Accounting,Virginia Tech,3.1,12,N/A,3.8
Linda Wallace,Accounting,Virginia Tech,2.9,4,75%,3.8
Michelle Harding,Accounting,Virginia Tech,4.6,4,100%,3.6
Dana Garner,Accounting,Virginia Tech,3.0,3,67%,3.4
Francis Ding,Accounting,Virginia Tech,3.7,3,67%,3.3
Jonathan DiYorio,Accounting,Virginia Tech,1.0,1,0%,5
Greg Jenkins,Accounting,Virginia Tech,5.0,1,N/A,3
Sarah Asebedo,Accounting,Virginia Tech,1.5,1,N/A,4
Owen Hughes,Aerospace Studies,Virginia Tech,4.0,1,N/A,4
Shane Ross,Aerospace Studies,Virginia Tech,5.0,1,100%,2
William Devenport,Aerospace Studies,Virginia Tech,5.0,1,100%,2
Michael Philen,Aerospace Studies,Virginia Tech,3.2,12,59%,2.9
Scott England,Aerospace Studies,Virginia Tech,5.0,4,100%,3.4
Ella Atkins,Aerospace Studies,Virginia Tech,2.0,2,0%,4
Jie Song,Aerospace Studies,Virginia Tech,4.0,2,100%,2
Aurelien Borgoltz,Aerospace Studies,Virginia Tech,3.0,1,0%,3
Mathieu Joerger,Aerospace Studies,Virginia Tech,5.0,1,100%,4
Christine Gilbert,Aerospace Studies,Virginia Tech,0.0,0,N/A,0
Gary Seidel,Aerospace Studies,Virginia Tech,5.0,3,100%,3.8
Lili Ma,Aerospace Studies,Virginia Tech,1.5,2,N/A,4
Kevin Wang,Aerospace Studies,Virginia Tech,1.0,2,0%,5
Riley Fitzgerald,Aerospace Studies,Virginia Tech,5.0,1,100%,2
Nanyaporn Intaratep,Aerospace Studies,Virginia Tech,4.0,1,100%,4
Pat Artis,Aerospace Studies,Virginia Tech,3.8,9,67%,4
Eric Paterson,Aerospace Studies,Virginia Tech,2.5,4,25%,4.3
Wayne Neu,Aerospace Studies,Virginia Tech,1.0,1,N/A,4
Pradeep Raj,Aerospace Studies,Virginia Tech,3.0,1,0%,2
Yao Fu,Aerospace Studies,Virginia Tech,4.0,1,100%,3
Stefano Brizzolara,Aerospace Studies,Virginia Tech,0.0,0,N/A,0
Christopher Roy,Aerospace Studies,Virginia Tech,5.0,3,100%,2.7
Heng Xiao,Aerospace Studies,Virginia Tech,4.0,2,0%,3.5
Inga Schlier,Aerospace Studies,Virginia Tech,5.0,1,100%,2
Mayuresh Patil,Aerospace Studies,Virginia Tech,0.0,0,N/A,0
Michael Fowler,Aerospace Studies,Virginia Tech,0.0,0,N/A,0
Colin Adams,Aerospace Studies,Virginia Tech,0.0,0,N/A,0
Cheryl Montgomery,African Studies,Virginia Tech,5.0,1,100%,3
Dennis Halpin,African Studies,Virginia Tech,4.0,1,100%,2
Paula Seniors,African Studies,Virginia Tech,1.9,11,17%,2.6
Komal Dhillon,African Studies,Virginia Tech,3.4,3,67%,2.8
Jariah Strozier,African Studies,Virginia Tech,2.0,1,0%,1


"""

# Specify the file path
file_path = 'professor_ratings.csv'

# Write data to CSV file
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    file.write(data)

print(f"Data has been written to {file_path}")
