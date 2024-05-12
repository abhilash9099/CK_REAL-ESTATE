import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_valid_login(self):
        user = "test"
        pwd = "test123"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")