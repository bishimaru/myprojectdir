from django.core.management.base import BaseCommand, CommandError
from ... models import SlotData
from django.utils import timezone
import requests
from bs4 import BeautifulSoup
import datetime
from selenium import webdriver


class Command(BaseCommand):
    def handle(self, *args, **options):

        print('hello')
        day = 0
        # 台番号4001 ~ 4268
        i = 4222
        url = 'https://p-ken.jp/p-arkst/bonus/detail?ps_div=2&cost=21.7&model_nm=%CF%B2%BC%DE%AC%B8%DE%D7%B0IV&day=' + str(day) + '&lot_no=' + \
            str(i) + '&mode='
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # soup.canvas_get()
        list = {}
        now = datetime.datetime.now()

        get_data1 = soup.find_all('div', class_='first')
        get_data1 = get_data1[0]
        get_li = get_data1.find_all('li')

        nb = get_li[1].text
        nb = nb[-4:]

        list['number'] = (int)(nb)
        list['name'] = get_li[2].text

        get_data2 = soup.find_all("div", class_="bonus_summary2 card-content")
        get_data2 = get_data2[0]
        get_n = get_data2.find_all('span')

        list['store_name'] = 'ピーアーク竹ノ塚スタジオ'
        list['BB'] = (int)(get_n[0].text)
        list['RB'] = (int)(get_n[1].text)
        list['lastgame'] = (int)(get_n[3].text)
        list['totalgames'] = (int)(get_n[4].text)
        list['BBchance'] = get_n[5].text
        list['RBchance'] = get_n[6].text
        list['totalchances'] = get_n[8].text
        list['date'] = now

        print(list)

# canvas要素の保存方法を調べる


def sample_run():
    # 収集先urlを指定
    url = 'https://p-ken.jp/p-charakawa/bonus/detail?ps_div=2&cost=21.28&model_nm=%CF%B2%BC%DE%AC%B8%DE%D7%B0III&day=0&lot_no=253&mode='
    try:
        # クラス生成
        Soup = selenium_webdriver.Main(url)
        # webdriver初期設定
        Soup.driver_init()
        # 指定したurlへ移動+処理
        Soup.driver_wait()
        for _ in range(6):
            # canvasタグ内の画像を取得
            Soup.canvas_get()
            # # 次のページに移動
            # Soup.next_page_click()
            # time.sleep(3)
    except Exception as e:
        print(e)
        Soup.driver.quit()
