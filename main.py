from selenium_side import TabManager, NewTab
import time
from selenium.webdriver import Chrome
import timeago
from datetime import datetime
from helper import *

from datetime import datetime

if __name__ == "__main__":
    USERNAME = "jjjjsamer"
    '''
    tab_manager=TabManager(USERNAME)
    tab_manager.startup()
    tab_manager.open_tabs()
    time.sleep(5)
    tab_manager.driver.quit()
    '''

    driver = Chrome()
    new_tab = NewTab(driver, "orieliel-watcher")
    tracks = new_tab.get_tracks(limit=1)
    driver.quit()
