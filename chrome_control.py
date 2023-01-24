from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from internet_test import InternetVerify
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

class BrowserController():


    def __init__(self) -> None:
        self.path_user = os.getenv('APPDATA')
        self.navegador = self.browser()
        
        

    def browser(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--kiosk")
        options.add_argument("--profile-directory=Default")
        options.add_argument(f'--user-data-dir={self.path_user}\cache')
        # options.add_argument('--user-data-dir=tmp/browser') #no caso do windows
        navegador = webdriver.Chrome("chromedriver.exe", options=options)
        return navegador
    
    def open_browser(self, url):

        self.navegador.get(url)
        sleep(5)


    def full_screen(self):
        wait = WebDriverWait(self.navegador, 10)
        self.navegador.maximize_window()
        sleep(5)
        
        
        # wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/a'))).send_keys(Keys.F11)
        # self.navegador.find_element(By.XPATH,'/html/body').send_keys(Keys.F11)
        sleep(20)

    def configurar_som(self):
        wait = WebDriverWait(self.navegador, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/a'))).click()
        clicar_no_som = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/aside/ul/li[4]/a')))
        
        clicar_no_som.click()
        
        clicar_no_botao_de_sair_som = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[1]/div/a/span')))
        
        clicar_no_botao_de_sair_som.click()
        sleep(3)
        clicar_no_botao_de_sair_som.click()
        sleep(3)
        clicar_no_botao_de_sair_som.click()
        sleep(3)
        
        clicar_em_salvar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[2]/div/button')))
        clicar_em_salvar.click()
        sleep(2)
        clicar_em_ok = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[4]/div/button'))) 
        clicar_em_ok.click()
        sleep(5)
        clicar_em_voltar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/aside/a')))
        clicar_em_voltar.click()
        
        
        
if __name__ == "__main__":
    internet = InternetVerify()
    browser = BrowserController()

    browser.open_browser("http://10.17.20.116/psenha")
 
    browser.configurar_som()
    sleep(600)
    while not internet.check_internet():
        print('erro net')
        sleep(5)