from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import sys
from urllib.parse import urlparse



class Scraper(object):
    def __init__(self):
        #self.driver = webdriver.PhantomJS('./phantomjs')
        option = webdriver.ChromeOptions()
        option.add_argument("--start-maximized")
        option.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        #option.add_argument('--headless')
        #option.add_argument('window-size=1120x550')
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
            }
        self.driver = webdriver.Chrome(
            executable_path= r"C:\Users\jf_mo\Desktop\automation\chromedriver.exe", chrome_options=option)



    def read_string(self):
        # function to convert a list into string
                
        # Assign the arguments passed to a variable search_string
        search_string ="".join(sys.argv[1:]) 
        print(search_string)
        # The argument passed to the program is accepted
        # as list, it is needed to convert that into string
        #search_string = convert(search_string)
        
        # This is done to structure the string 
        # into search url.(This can be ignored)
        search_string = search_string.replace(' ', '+')
        complete_link = "https://www.bing.com/search?q=" + search_string + " site:reddit.com"
        self.driver.get(complete_link)
        #aceptas cookies
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bnp_btn_accept"]'))).click()
        return complete_link

    def page_is_loaded(self):
        x = self.driver.execute_script("return document.readyState")
        if x == "complete":
            return True
        else:
            return False

    def scrape(self, complete_link):
        #sleep(10)
        if self.page_is_loaded():
            s = BeautifulSoup(self.driver.page_source, "html.parser")
            #print(s)
            snippet = s.find_all('h2')
            for h2 in snippet:
                for a in h2.find_all('a', href=True):
                    link = a['href']
                    domain = urlparse(str(link)).netloc
                    print(domain) # --> www.example.test
                    if 'reddit' in domain:
                        self.driver.execute_script(f"window.open(\"{link}\",\"_blank\");")
            snippet.clear()
            #elf.driver.quit()

if __name__ == '__main__':
    scraper = Scraper()
    complete_link = scraper.read_string()
    scraper.scrape(complete_link)