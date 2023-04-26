import random, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from update_profile import update_cookie_profile, get_saved_cookie
from parse import news_list as list_news


service = Service(
    executable_path=r'C:\Users\МС\Desktop\Test\try\first\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service)


def create_session():
    url, url_index = get_profile()
    try:
        # insert saved cookies into session
        cookie_db = get_saved_cookie(url_index)
        driver.get(url=url)

        if cookie_db:
            for cock in cookie_db:
                driver.add_cookie(cock)
                
        driver.refresh()
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randint(1, 10))

        # get new cookies and update profile_cookie
        cock = driver.get_cookies()
        update_cookie_profile(id=url_index, cookies=cock)
        
    except Exception as ex:
        print('WROOOOOOOOOOOOOOOONG')
        print(ex)
    finally:
        driver.close()
        driver.quit()


def get_profile() -> tuple:
    url = random.choice(list_news)
    url_index = list_news.index(url) + 1
    
    return url, url_index
