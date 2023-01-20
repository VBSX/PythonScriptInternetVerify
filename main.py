import time
from internet_test import InternetVerify
from chrome_control import  BrowserController



class Main():
    def __init__(self) -> None:
            
        
        self.internet_tester = InternetVerify()
        
        
    
    def abrir_navegador(self, browser):
        browser.open_browser("http://10.17.20.116/psenha")
        
    def loop_verifier(self):
        
        loop = True
        
        while loop:    
            if not self.internet_tester.check_internet():
                print('Internet fora do ar!')
                time.sleep(3)
                while not self.internet_tester.check_internet():
                    print('erro net')
                    time.sleep(5)
                
                print('Internet OK!')
                self.internet_tester.matar_processo_navegador()
                
                browser = BrowserController()
                browser.full_screen()
                self.abrir_navegador(browser) 
                
                    
            else:
                print('internet de boa')

                time.sleep(1)

start = Main()
start.loop_verifier()