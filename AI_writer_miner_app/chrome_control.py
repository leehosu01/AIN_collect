
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()
def init_page():
    driver.get("https://ainize.ai/teachable-nlp/ai-writers-onboarding")
    pass

def set_input_box(string):
    pass