from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# ChromeDriver設定
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://p-ken.jp/p-charakawa/bonus/detail?ps_div=2&cost=21.28&model_nm=%CF%B2%BC%DE%AC%B8%DE%D7%B0III&day=0&lot_no=253&mode=')

# 画面描画の待ち時間
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)

# ページへアクセス
element = driver.find_element_by_id('canvas')

# ページが読み込まれるまで待機
wait.until(EC.presence_of_all_elements_located)

# 画像の場所
xpath = '/html/body/div[1]/div[3]/div[1]/section[1]/div/div[6]/div/div/div/div[1]/div[1]/div[2]/canvas'
img = driver.find_element_by_xpath(xpath)

# 画像の場所へマウス移動してから右クリック
actions = ActionChains(driver)
actions.move_to_element(img).context_click(img).perform()

# 「↓」キーを5回入力
actions.send_keys(Keys.ARROW_DOWN).perform()
# Enterキーを入力
actions.send_keys(Keys.ENTER).perform()
