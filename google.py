from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import sys
from urllib.parse import urlparse

#hacer uno de estos para youtube tambien
#meterle para que te busque archivos por formato
#green_color = "\033[1;32m"
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Scraper(object):
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument("--start-maximized")
        self.green_color = "\033[1;32m"
        self.white_color = '\033[0m'
        option.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        self.driver = webdriver.Chrome(
            executable_path= r"C:\Users\jf_mo\Desktop\automation\chromedriver.exe", chrome_options=option)



    def read_string(self):
        # function to convert a list into string
        # Assign the arguments passed to a variable search_string
        search ="".join(sys.argv[1]) 
        s_domain = "".join(sys.argv[2])
        # The argument passed to the program is accepted
        # as list, it is needed to convert that into string
        #search_string = convert(search_string)
        
        # This is done to structure the string 
        # into search url.(This can be ignored)
        #search_string = search_string.replace(' ', '+')
        complete_link = f"https://www.google.com/search?q={search} site: {s_domain}.com"
        complete_link = complete_link.replace(' ', '+')
        print(complete_link)
        self.driver.get(complete_link)
        #aceptas cookies
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="L2AGLb"]'))).click()
        return s_domain

    def page_is_loaded(self):
        x = self.driver.execute_script("return document.readyState")
        if x == "complete":
            return True
        else:
            return False

    def scrape(self, s_domain):
        if self.page_is_loaded():
            s = BeautifulSoup(self.driver.page_source, "html.parser")
            counter = 0
            link_list = []
            for a in s.find_all('a', href=True):
                link = a['href']
                domain = urlparse(str(link)).netloc
                
                if s_domain in domain:
                    #self.driver.execute_script(f"window.open(\"{link}\",\"_blank\");")
                    #cuentas resultados, guardas y abres
                    link_list.append(link)
                    counter +=1
            results = input(f"{color.BOLD}Cuántos resultados quieres ver?, la primera página tiene {counter}, all, si quieres verlos todos{color.END}")
            if results != None:
                for result in link_list[:int(results)]:
                    self.driver.execute_script(f"window.open(\"{result}\",\"_blank\");")


if __name__ == '__main__':
    scraper = Scraper()
    complete_link = scraper.read_string()
    scraper.scrape(complete_link)