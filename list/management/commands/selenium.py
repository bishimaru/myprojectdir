from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# driver = webdriver.Chrome('chromedriver')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://p-ken.jp/p-charakawa/bonus/detail?ps_div=2&cost=21.28&model_nm=%CF%B2%BC%DE%AC%B8%DE%D7%B0III&day=0&lot_no=253&mode=')
