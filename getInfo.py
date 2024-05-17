from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import time
import pandas as pd

service = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Executar o navegador em modo headless (sem GUI)
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(service=service, options=options)
area = (313, 160, 672+310, 475+158)
path = 'Certificados/'
url_alura = "https://cursos.alura.com.br/user/arilsonsouzacosta0"
cursos = []
nomes = []
data = []
descricao = []
try:
    driver.get(url_alura)
    time.sleep(10)
    elements = driver.find_elements(By.CLASS_NAME, 'course-card__certificate')
    for element in elements:
        "https://cursos.alura.com.br/user/arilsonsouzacosta0/course/relacionamento-pessoal/certificate"
        "https://cursos.alura.com.br/course/relacionamento-pessoal"
        url = element.get_attribute("href")
        url = url.replace("/user/arilsonsouzacosta0","")
        url = url.replace("/certificate","")
        cursos.append(url)
    for curso in cursos:
        print(curso)
        driver.get(curso)
        time.sleep(5)
        nome = driver.find_element(By.CLASS_NAME, 'certificate-front-info__title ')
        nome = nome.text
        nome = nome.replace(":"," -")
        nome = nome.title()
        certificado = f"{path}{nome}.png"
        driver.save_screenshot(certificado)
        img = Image.open(certificado)
        certificado_cortado = img.crop(area)
        certificado_cortado.save(certificado)
        print(f"{elements.index(element)+1}/{len(elements)}")
    driver.quit()
except Exception as e:
    print(e)
finally:
    driver.quit()
