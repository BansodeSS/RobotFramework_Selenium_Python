from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_chromedriver_path():
    return ChromeDriverManager.install()
