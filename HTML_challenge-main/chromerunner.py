# Import Splinter, BeautifulSoup, and Pandas
# from splinter import Browser
# from bs4 import BeautifulSoup as soup
# import pandas as pd
from selenium import webdriver


# In[12]:

pip install selenium
# Set the executable path and initialize Splinter
executable_path = {'executable_path': 'C:/Users/tharu/OneDrive/Documents/11-HTLM/Coursework/HTML_challenge/chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)

driver = webdriver.Chrome('C:/Users/tharu/OneDrive/Documents/11-HTLM/Coursework/HTML_challenge/chromedriver.exe')
# %%
