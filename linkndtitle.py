import unittest
import os.path
import pandas as pd
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from getexceldif import getdiff
from bs4 import BeautifulSoup 


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def test_page_item(self):
        res= getdiff()
        title=[]
        links = [] 
        for query in res:
            n_pages = 5 
            for page in range(0, n_pages):
                url = "http://www.google.com/search?q=" + query + "&start=" +      str((page - 1) * 10)
                self.driver.get(url)
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')

                
                titles = soup.find_all('h3',class_="LC20lb DKV0Md")
                for l in titles:
                    title.append(l.text)
                # print(title)
                search = soup.find_all('div', class_="yuRUbf")
                for h in search:
                    links.append(h.a.get('href'))
                # print(links)
        print(len(title),len(links))
        df=pd.DataFrame()
        df['Title']=title
        df['urls']=links
        df.to_excel(os.path.join(os.getcwd(),'data','c.xlsx'), index=False)
            

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
