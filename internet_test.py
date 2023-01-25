import requests
import subprocess
import time



class InternetVerify():



    def check_internet(self):
        ''' checar conexão de internet '''
        url = 'http://10.17.20.116/public'
        timeout = 5
        try:
            requests.get(url, timeout=timeout)
            return True
        except:
            return False



    def matar_processo_navegador(self):
        try:
            subprocess.run("taskkill /f /im chrome.exe", shell=True, check=True) #se for windows use esse comando
            # subprocess.run("pkill --oldest chrome", shell=True, check=True) # caso seja linux

        except:
            pass
        time.sleep(2)
        
        
        
if __name__ == '__main__':
    internet = InternetVerify()


    while not internet.check_internet():
        print('erro net')
        # internet.matar_processo_navegador()
    else:
        print('certo')
       
