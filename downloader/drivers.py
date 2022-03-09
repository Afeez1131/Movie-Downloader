from http.server import executable
from selenium.webdriver import PhantomJS, Firefox
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


url = 'https://www.thenetnaija.co/videos/movies/15783-taylor-tomlinson-look-at-you-2022/download'
driver = PhantomJS(executable_path='/usr/local/bin/phantomjs')
driver.get(url)
# wait = WebDriverWait(driver, 10)

try:
    WebDriverWait(driver, 60).until(EC.url_contains("sabishare"))
    soup = BeautifulSoup(driver.page_source, features='lxml')
    print(soup)
except TimeoutException:
    print("Desired url was not rendered with in allocated time")