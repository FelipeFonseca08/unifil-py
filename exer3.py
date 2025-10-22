from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
navegador = webdriver.Edge()

navegador.get("https://www.youtube.com/")

campo = navegador.find_element(By.NAME,"search_query")
campo.send_keys("7 Minutoz")
campo.send_keys(Keys.ENTER)


time.sleep(5)

primeiro_video = navegador.find_element(By.ID,"video-title")
primeiro_video.click()

time.sleep(10)