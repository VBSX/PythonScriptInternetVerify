import time
from internet_test import InternetVerify
from chrome_control import  BrowserController
import threading


class Main():
    
    def __init__(self) -> None:


        self.internet_tester = InternetVerify()


    def configurar_navegador(self):
 
 
        try:
            self.internet_tester.matar_processo_navegador()

            browser = BrowserController()
            self.abrir_navegador(browser)
            browser.configurar_som()
        except:
            pass
        
    
    def abrir_navegador(self, browser):
        browser.open_browser("http://10.17.20.116/psenha")

    
    
    def loop_verifier(self):
        
        if self.internet_tester.check_internet():
            try:
                t1 = threading.Thread(target=self.configurar_navegador)
                t1.start()
            except:
                pass
        loop = True
        loop2 = True
        while loop:    
            if not self.internet_tester.check_internet():
                print('Internet fora do ar!')
                time.sleep(3)
                while not self.internet_tester.check_internet():
                    print('erro net')
                    time.sleep(5)

                print('Internet OK!')
                try:
                    self.internet_tester.matar_processo_navegador()
                    
                    browser = BrowserController()
                    
                    self.abrir_navegador(browser) 
                    
                    browser.configurar_som()
                except:
                    final_funcao= False
                    while not final_funcao:
                        self.internet_tester.matar_processo_navegador()
                        
                        browser = BrowserController()
                        
                        self.abrir_navegador(browser) 
                        
                        browser.configurar_som()
                        final_funcao = True
           

            else:
                print('internet de boa')

                time.sleep(1)
            

start = Main()
start.loop_verifier()