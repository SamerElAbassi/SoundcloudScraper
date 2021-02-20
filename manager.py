import concurrent.futures
from selenium_side import TabManager, NewTab


def start_tabs(username, indexes):
    print(f"Starting new tab with {indexes}")
    tab_manager = TabManager(username)
    tab_manager.startup()
    try:
        tab_manager.open_tabs(indexes)
    except:
        tab_manager.driver.quit()
