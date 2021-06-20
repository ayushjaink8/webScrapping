from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
from time import sleep

url = "https://www.4devs.com.br/gerador_de_cpf"

def get_cpf():
    driver = webdriver.Chrome("/home/felipe/Downloads/chromedriver")
    driver.get(url)
    driver.find_element_by_id('bt_gerar_cpf').click()
    sleep(10)
    text=driver.find_element_by_id('texto_cpf').text
    print(text)
get_cpf()