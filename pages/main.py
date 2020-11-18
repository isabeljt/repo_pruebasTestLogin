"""
This module contains ProductStoreMain,
the page object for the ProductStore main page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ProductStoreMainPage:

  # URL

  URL = 'https://www.demoblaze.com/index.html'

  # Locators

  LOGIN_BUTTON = (By.ID, 'login2')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def login(self):
    login_button = self.browser.find_element(*self.LOGIN_BUTTON)
    login_button.send_keys(Keys.RETURN)
