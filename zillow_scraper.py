import random
import time
import numpy as np
import pandas as pd
from selenium_stealth import stealth
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException


class Zillow_scraper:
    def __init__(self,url,timeout=10):
        self.url = url
        self.data = []
        self.driver = self._initialize_driver()
        self.wait = WebDriverWait(self.driver,timeout)




    def _initialize_driver(self):
        USER_AGENTS = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

            ]
        options = uc.ChromeOptions()
        options.add_argument(f"--user-agent={random.choice(USER_AGENTS)}")


        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-translate")


        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_settings.popups": 0,
        }
        options.add_experimental_option("prefs", prefs)

        driver = uc.Chrome(options=options)
        driver.maximize_window()
        return driver

    def apply_stealth(self):
        stealth(
            self.driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )

        self.driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                });
                """
            }
        )

    def acces_website(self):
        self.driver.get(self.url)
        time.sleep(2)
    

    def enter_search_details(self,texts):

        url = "https://www.zillow.com/"
        self.driver.get(url)
        time.sleep(2)


        search_bar = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//input[contains(@class,'StyledFormControl-c11n-8-111-2__sc-w61kvv-0 cAbjTM Input-c11n-8-111-2__sc-4ry0fw-0 hQEDWz')]",
                )
            )
        )
        search_bar.send_keys(texts + Keys.ENTER)
        time.sleep(3)
        
        skip_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class,'StyledTextButton-c11n-8-111-2__sc-1nwmfqo-0 hqcokm')]",
                )
            )
        )
        skip_button.click()
        time.sleep(1)
    
    
    def human_scroll(self):
        for _ in range(random.randint(2, 4)):
            scroll = random.randint(300, 900)
            self.driver.execute_script(f"window.scrollBy(0, {scroll});")
            time.sleep(random.uniform(1.5, 3))
    

    def scrapig_data(self):
       
        dom = self.driver.find_elements(
            By.XPATH, "//li[contains(@class,'c11n')]"
        )


        for doms in dom:
            try:
                price = doms.find_element(
                    By.XPATH,
                    ".//div[contains(@class,'srp-cYdhWw srp-dNIosp')]",
                ).text
            except:
                price = np.nan

            try:
                ul_tag = doms.find_element(
                    By.XPATH,
                    ".//ul[contains(@class,'StyledPropertyCardHomeDetailsList-c11n-8-109-3__sc-1j0som5-0 dFYPvN')]",
                )
                li = ul_tag.find_elements(
                    By.CSS_SELECTOR, "li b"
                )
                bds = li[0].text
                ba = li[1].text
                sqft = li[2].text
            except:
                bds = np.nan
                ba = np.nan
                sqft = np.nan

            try:
                address = doms.find_element(
                    By.XPATH,
                    ".//a[contains(@class,'property-card-link')]",
                ).text
                print(address)
            except:
                address = np.nan

            property_data = {
                "address": address,
                "price_dollar": price,
                "beds": bds,
                "baths": ba,
                "sqft": sqft,
            }


            self.data.append(property_data)

        
    def scrolling_and_pagenation(self):

        for page in range(1, 21):
            self.human_scroll()

            right_panel = self.driver.find_element(
                    By.XPATH, "//div[@data-testid='search-page-list-container']"
            )
            try:
                for i in range(4):
                    self.driver.execute_script(
                        "arguments[0].scrollTop+=1000", right_panel
                    )
                    time.sleep(2.5)
                    self.scrapig_data()
                    next_button = self.driver.find_element(By.XPATH, "//a[@title='Next page' and @aria-disabled='false']")
                    self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", next_button)
                    time.sleep(1.5)
                    next_button.click()
                    print(f"Page {page} clicked")
                    time.sleep(3)
            except NoSuchElementException:
                break

    
    def save_to_csv(self):
        df = pd.DataFrame(self.data)
        df.to_csv("Zillow_Propertys_data.csv", index=False)
        print("scraping is compleate")



    def script_rum(self, texts="TX"):

        try:
            self.apply_stealth()
            self.acces_website()
            self.enter_search_details(texts)
            self.scrolling_and_pagenation()
            self.save_to_csv()
        finally:
            self.driver.quit()
        
if __name__ == "__main__":
    scraper = Zillow_scraper(url="https://www.zillow.com/")
    scraper.script_rum(texts="TX")




            







