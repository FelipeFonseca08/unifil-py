from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
navegador = webdriver.Edge()

navegador.get("https://books.toscrape.com/")

livro = navegador.find_element(By.ID,"video-title")

time.sleep(10)

