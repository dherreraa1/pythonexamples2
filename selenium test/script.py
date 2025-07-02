import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")

# Your paragraph to type
text = (
    "The old oak tree had stood at the edge of the meadow for longer than anyone could remember. "
    "Its massive branches stretched skward, a shelter for birds and squirrels, a gathering place for those seeking shade. "
    "Generations had carved their initials into its bork, their love stories and friendships etched into its weathered skin. "
    "In the summer, children built tire swings from its sturdy limbs, their laughter ringing through the warm air. "
    "In autumn, golden leaves rained down like confetti, blanketing the ground in a crisp, colorful carpet. "
    "During the quiet of winter, the tree stood bare but strang, waiting patiently for spring's renewal. "
    "A young woman sat beneath it now, her back against the rough bark, a book resting in her lap. The tree had seen "
)
words = text.split()

# Set up Selenium WebDriver (Chrome)
driver = webdriver.Chrome(options=options)
driver.get("https://somewheretypingtest.com/")

wait = WebDriverWait(driver, 10)

# Wait for and click the "Start Test" button
start_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Start Test')]")))
start_button.click()

# Optional: small delay before starting to type
time.sleep(3)

# Typing for 60 seconds max
start_time = time.time()
for word in words:
    # Stop typing after 60 seconds
    if time.time() - start_time > 60:
        print("Typing stopped after 60 seconds.")
        break
    # Type each character in the word
    for char in word:
        driver.switch_to.active_element.send_keys(char)
        time.sleep(0.11)
    # Press space after each word
    driver.switch_to.active_element.send_keys(Keys.SPACE)
    time.sleep(0.11)

print("Done typing. Browser remains open for inspection.")
print("Close the browser manually when finished.")
input("Press ENTER to exit and close the browser...")
driver.quit() 
