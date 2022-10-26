from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https:/google.com")
## Encontrar Elementos

google_text = driver.find_element(By.CLASS_NAME, "MV3Tnb").text

print(google_text)

input_box = driver.find_element(By.NAME, "q")

input_box.send_keys("byron")

input_box.send_keys(Keys.ENTER)
## Pausa de 5 segundos

import time


print('esperaremos 5 segundos' )
#time.sleep(5)

## Volvemos a la home page

home_link = driver.find_element(By.ID, "logo")

home_link.click()


## Buscar


input_box = driver.find_element(By.NAME, "q")

input_box.send_keys("selenium")

input_box.send_keys(Keys.ENTER)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "dev")

print(link.text)

link.click()
driver.get("https://es.wikipedia.org")
time.sleep(5)

driver.get("https:/www.contraloria.cl")



cgr_cerrar = driver.find_element(By.CLASS_NAME, "fa-times-circle-o")
cgr_cerrar.click()
#print(cgr_text)


input_box = driver.find_element(By.CLASS_NAME, "_1qG0")
input_box.send_keys("cgr")
input_box.click()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

input_text = driver.find_element(By.ID, "my-text-id")
input_text.send_keys("texto")
input_pass = driver.find_element(By.NAME, "my-password")
input_pass.send_keys("secreto")
input_area = driver.find_element(By.NAME, "my-textarea")
input_area.send_keys("texto super largo")
input_area = driver.find_element(By.CLASS_NAME, "form-select")
input_area.send_keys("2")

btm_enviar = driver.find_element(By.CLASS_NAME, "btn-outline-primary")
btm_enviar.click()
