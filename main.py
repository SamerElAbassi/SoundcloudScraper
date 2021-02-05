from selenium_side import TabManager
import time
if __name__=="__main__":
    USERNAME="jjjjsamer"
    tab_manager=TabManager(USERNAME)
    tab_manager.startup()
    time.sleep(5)
    tab_manager.driver.quit()