# %%
from user_related import User, Track
from selenium.webdriver import Chrome
import time
import os
from os import path
import pandas as pd
from bs4 import BeautifulSoup
import pickle
from helper import *
from operator import itemgetter


class NewTab:
    def __init__(self, driver, username, scroll_pause_time=1, open_tab=1, handle=-1, user=None):
        self.driver = driver
        self.username = username
        self.scroll_pause_time = scroll_pause_time
        self.url = "https://soundcloud.com/" + username + "/tracks"
        if open_tab:
            self.open_tab(handle)
        self.tracks = []
        self.followers = []
        self.user = user
        time.sleep(3)  # Wait untill its done
        self.get_tracks()

    def open_tab(self, handle=-1):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[handle])
        self.driver.get(self.url)
        print(f'Sucessfully opened {self.url}')

    def get_username(self):
        return self.username

    def scroll(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(self.scroll_pause_time)
        new_height = self.driver.execute_script("return document.body.scrollHeight")
        return not new_height == last_height

    def get_tracks(self, limit=20):
        counter = 0
        while self.scroll() and counter < limit:
            counter += 1
        self.tracks = get_track_objects(self)

    def get_tracks_before_date(self, delta_limit=30):
        return [track for track in self.tracks if delta_time(track.date) < delta_limit]

    def __str__(self):
        string = "*" * 20 + "\n" + f"username:{self.username}"
        for track in self.tracks:
            string += "\n" + str(track)
        return string


class InitTab(NewTab):
    def __init__(self, driver, username):
        super().__init__(driver, username, open_tab=0)
        self.url = "https://soundcloud.com/" + self.username + "/following"
        self.open_tab()

    def get_followers(self, limit=100):
        followers = []
        counter = 0

        while self.scroll() and counter < limit:
            counter += 1
        followers.extend(self.driver.find_elements_by_class_name("userBadgeListItem__image"))
        self.followers = [elem.get_attribute('href') for elem in followers]
        store_data(self.followers, "followers.txt")

        return self.followers

    def __str__(self):
        string = "" * 20 + "\n" + f"USERNAME:{self.username}"
        for follower in self.followers:
            string += "\n" + str(follower)
        return string

class TabManager:
    time_diff = 30

    def __init__(self, init_username, tabs=None, init_tab=None):
        self.driver = Chrome()
        self.tabs = tabs
        self.init_username = init_username
        self.init_tab = init_tab
        self.user = User(init_username, "init")

    def startup(self):
        self.init_tab = InitTab(self.driver, self.init_username)
        time.sleep(1)
        if path.exists("followers.txt"):
            followers_dataframe = pd.read_csv("followers.txt")
            followers = followers_dataframe['followers'].values
        else:
            followers = self.init_tab.get_followers()

        self.user.set_follow_list(followers)

    def open_tabs(self, indexes):
        tabs = []
        counter = 0
        for followed_url in list(map(self.user.get_follow_list().__getitem__, indexes)):
            username = get_user_from_url(followed_url)
            new_tab = NewTab(self.driver, username, open_tab=1)
            tabs.append(new_tab)

            tracks = new_tab.get_tracks_before_date()
            if tracks:
                print("--------------New artist!--------------!\n" + \
                      f'--------------{new_tab.username}!--------------!')
                for track in tracks:
                    print(str(track))
            if counter > 20:
                break
            counter += 1

    def get_followers(self):
        return self.user.get_follow_list()
