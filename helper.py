from bs4 import BeautifulSoup
from datetime import datetime
from user_related import Track
from selenium.webdriver import Chrome
import time
def delta_time(then: datetime):
    then = datetime.strptime(then, "%Y-%m-%d").date()
    now = datetime.today().date()
    return (now - then).days


def get_user_from_url(url):
    return url[len("https://soundcloud.com/"):]


def store_data(data, filename):
    with open(filename, "w") as f:
        for index, info in enumerate(data):
            f.write(str(index) + "," + str(info) + "\n")


def get_track_objects(new_tab):
    soup = BeautifulSoup(new_tab.driver.page_source, 'lxml')
    sound_contents = soup.find_all('div', class_="sound__content")
    tracks = []
    for content in sound_contents:
        basic_inf = content.find('a', class_="soundTitle__title sc-link-dark")
        title, url = basic_inf.get_text(), basic_inf.get('href')
        date = content.find('time', class_="relativeTime").get('datetime').split('T')[0]
        tracks.append(Track(url, date, title, new_tab.username))

    return tracks

