from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def download_with_title(title):
    """ Download both prior works and derivative works from https://www.connectedpapers.com.
    
    Args:
        title: The paper's title formatted as a string.
     """

    # TODO(2022-01-01): error handling
    option = webdriver.ChromeOptions()
    # get the web
    driver = webdriver.Chrome(executable_path='./web_driver/chromedriver.exe')
    # paper title you want to search
    url = 'https://www.connectedpapers.com/search?q={}'.format(title)
    url = url.replace(' ', '%20')
    print('your url is: {}'.format(url))

    # open the page
    driver.get(url)
    # choose the first search result as default
    driver.find_element(By.XPATH, '//*[@id="open-in-container"]/a[1]').click()
    # switch to another window
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    print('current url is :{}'.format(driver.current_url))

    # switch to prior works page
    driver.find_element(By.XPATH, '//*[@id="desktop-app"]/div[2]/div[1]/div/button[1]').click()
    print(driver.current_url)
    # download prior works
    driver.find_element(By.XPATH, '//*[@id="desktop-app"]/div[2]/div[3]/div[2]/div/div/div/div/span').click()
    # switch to derivative works
    driver.find_element(By.XPATH, '//*[@id="desktop-app"]/div[2]/div[1]/div/button[2]').click()
    print(driver.current_url)
    # download derivative works
    driver.find_element(By.XPATH, '//*[@id="desktop-app"]/div[2]/div[3]/div[2]/div/div/div/div/span').click()
    sleep(3)
    print('succeed')
    driver.quit()

if __name__ == '__main__':
    title = input('please input paper title: ')
    download_with_title(title)