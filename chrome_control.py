from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from internet_test import InternetVerify


class BrowserController():
    

    def __init__(self) -> None:
        self.navegador = self.browser()
        
    
    def browser(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--profile-directory=Default")
        # options.add_argument('--user-data-dir=C:\Users\09673479984\AppData\Roaming\cache')
        options.add_argument('--user-data-dir=tmp/browser') #no caso do windows
        navegador = webdriver.Chrome("chromedriver.exe", options=options)
        return navegador
    def open_browser(self, url):
        
        self.navegador.get(url)
        sleep(5)

    
    def full_screen(self):
        self.navegador.maximize_window()
        self.navegador.find_element(By.TAG_NAME,'body').send_keys(Keys.F11)
        sleep(600)
    
if __name__ == "__main__":
    internet = InternetVerify()
    browser = BrowserController()
    
    browser.open_browser("http://10.17.20.116/psenha")
    browser.full_screen()
    
    while not internet.check_internet():
        print('erro net')
        sleep(5)
            
