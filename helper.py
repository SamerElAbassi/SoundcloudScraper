from bs4 import BeautifulSoup
from datetime import datetime
def delta_time(then: datetime):
    print(then)
    then = datetime.strptime(then, "%Y-%d-%m").date()
    now = datetime.today().date()
    return ((now - then).days)

def get_user_from_url(url):
    return url[len("https://soundcloud.com/"):]


def store_data(data, filename):
    with open(filename, "w") as f:
        for index, info in enumerate(data):
            f.write(str(index) + "," + str(info) + "\n")


def get_track_info(new_tab):
    soup=BeautifulSoup(new_tab.driver.page_source,'lxml')
    sound_contents=soup.find_all('div',class_="sound__content")
    contents=[sound_content.find('a',class_="soundTitle__title sc-link-dark") for sound_content in sound_contents]
    for content in sound_contents:
        basic_inf=content.find('a',class_="soundTitle__title sc-link-dark")
        title,url=basic_inf.get_text(),basic_inf.get('href')
        time=content.find('time',class_="relativeTime").get('datetime').split('T')[0]
        print(delta_time(time))

    return contents

