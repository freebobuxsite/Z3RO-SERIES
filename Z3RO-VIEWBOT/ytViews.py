#you must have a chrome driver and be on windows to use this.

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
import time

driver = webdriver.Chrome(options=chrome_options)


url = str(input("Enter your url \n"))
views = int(input("Enter your view amount \nAnything over 50 will take longer to register, \nas YouTube will catch on. \n"))
watchTime = int(input("Enter the amount of seconds you want the bot to watch your video for. \nAnything below 30 will be detected by YouTube and your video views will take longer to register \nor completely take a pause for a few hours. \n60 is good for a minimum of 100 views."))

def viewBot():
    driver.get(url)
    print("Loading video...")
    
    for view in range(views):
        time.sleep(watchTime)
        print("[!] View added.")
        driver.refresh()
        print("[-]Page refreshed")
        
        
viewBot()
        
        
