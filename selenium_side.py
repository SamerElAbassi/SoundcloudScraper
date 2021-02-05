# %%
from user_related import User
from selenium.webdriver import Chrome
import time


def store_data(data, filename):
    with open(filename, "w") as f:
        for index, info in enumerate(data):
            f.write(str(index) + " " + str(info) + "\n")

def get_track_info(track):
    track
class NewTab:
    def __init__(self, driver, username, scroll_pause_time=1, open_tab=1, handle=-1,user=None):
        self.driver = driver
        self.username = username
        self.scroll_pause_time = scroll_pause_time
        self.url = "https://soundcloud.com/" + username + "/tracks"
        if open_tab:
            self.open_tab(handle)
        self.tracks = []
        self.followers = []
        self.user = user

    def open_tab(self,handle):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[handle])
        self.driver.get(self.url)

    def scroll(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(self.scroll_pause_time)
        new_height = self.driver.execute_script("return document.body.scrollHeight")
        return 0 if new_height == last_height else 1

    def get_tracks(self, limit=None):
        counter = 0
        tracks = []
        while self.scroll() and counter < limit:
            counter += 1
        tracks.extend(self.driver.find_elements_by_class_name("soundList__item"))
        for track in tracks:
            track_url=track.get_attribute
        # self.tracks= selecteaza piesa extrage data compara cu diff
        return self.driver.find_elements_by_class_name("soundList__item")


class InitTab(NewTab):
    def __init__(self, driver, username):
        super().__init__(driver, username, open_tab=0)
        self.url = "https://soundcloud.com/" + self.username + "/following"
        self.open_tab()

    def get_tracks(self, limit=100):
        followers = []
        counter = 0

        while self.scroll() and counter < limit:
            print("Still scrolling")
            counter += 1

        followers.extend(self.driver.find_elements_by_class_name("userBadgeListItem__image"))
        self.followers = [elem.get_attribute('href') for elem in followers]
        store_data(self.followers, "followers.txt")

        return self.followers


class TabManager:
    def __init__(self, init_username, tabs=None, init_tab=None):
        self.driver = Chrome()
        self.tabs = tabs
        self.init_username = init_username
        self.init_tab = init_tab
        self.user = User(init_username, "init")

    def startup(self):
        self.init_tab = InitTab(self.driver, self.init_username)
        time.sleep(1)
        followers = self.init_tab.get_tracks()
        self.user.set_follow_list(followers)

    def open_tabs(self,indexes):
        tabs=[]
        for index in indexes:
            new_tab=NewTab(self.driver,self.init_username,open_tab=1,handle=index)
            tabs.append(new_tab)

    def get_followers(self):
        return self.user.get_follow_list()
