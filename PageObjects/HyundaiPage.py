from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from Utilities import configReader


class HyundaiPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

