from selenium_side import TabManager, NewTab
import time
from selenium.webdriver import Chrome
from datetime import datetime
import concurrent.futures
import multiprocessing as mp
from manager import *
from helper import *

if __name__ == "__main__":
    USERNAME = input("Type your username: ")
    FOLLOWERS = 300
    indexes = []
    indexes_length = 20
    for i in range(0, FOLLOWERS, indexes_length):
        indexes.append([i for i in range(i, i + indexes_length)])
    param_list = []
    for index in indexes:
        param_list.append((USERNAME, index))
    p = mp.Pool(mp.cpu_count() // 2)
    p.starmap(start_tabs, param_list)
