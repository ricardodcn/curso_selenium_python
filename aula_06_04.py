from selenium.webdriver import Firefox
from time import sleep

b = Firefox()

url = 'http://selenium.dunossauro.live/aula_06.html'

b.get(url)
