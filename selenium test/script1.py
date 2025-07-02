import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Your text to type (split by spaces)
text = ("The old oak tree had stood at the edge of the meadow for longer than anyone could remember. "
        "Its massive branches stretched skyward, a shelter for birds and squirrels, a gathering place for those seeking shade. "
        "Generations had carved their initials into its bark, their love stories and friendships etched into its weathered skin. "
        "In the summer, children built tire swings from its sturdy limbs, their laughter ringing through the warm air. "
        "In autumn, golden leaves rained down like confetti, blanketing the ground in a crisp, colorful carpet. "
        "During the quiet of winter, the tree stood bare but strong, waiting patiently for spring's renewal. "
        "A young woman sat beneath it now, her back against the rough bark, a book resting in her lap. "
        "The tree had seen").split()

# Setup Chrome options to hide automation banner and keep browser open
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("detach", True)  # Keeps browser open after script finishes
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

# Bypass navigator.webdriver detection
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    })
    """
})

driver.get("https://somewheretypingtest.com/")

wait = WebDriverWait(driver, 20)

# Wait for and click the "Start Test" button
start_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Start Test')]")))
start_button.click()

# Wait for the typing input box to appear (adjust selector accordingly)
typing_input = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))

# Function to simulate typing a word with a 2% error rate
def type_word_with_errors(word, input_element, error_rate=0.02):
    for char in word:
        # Decide whether to introduce an error
        if random.random() < error_rate:
            # Type a wrong char (random letter different from the correct char)
            wrong_char = random.choice("abcdefghijklmnopqrstuvwxyz".replace(char.lower(), ""))
            input_element.send_keys(wrong_char)
            time.sleep(random.uniform(0.05, 0.12))
            # Backspace to fix the mistake
            input_element.send_keys("\b")
            time.sleep(random.uniform(0.05, 0.12))
        # Type the correct character
        input_element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.12))

# Type words separated by spaces until 60 seconds pass
start_time = time.time()
for word in text:
    if time.time() - start_time > 60:
        print("1 minute elapsed, stopping typing.")
        break
    type_word_with_errors(word, typing_input)
    # Type space between words
    typing_input.send_keys(" ")
    time.sleep(random.uniform(0.1, 0.2))

print("Done typing. Browser remains open for inspection.")
print("Close the browser manually when finished.")
input("Press ENTER to exit and close the browser...")
driver.quit() 