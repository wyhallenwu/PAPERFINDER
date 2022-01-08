from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# TODO(2021-01-06): make code more modulized such as load_chromedriver 
def download_with_title(title, path='F:\github\PAPERFINDER\dataset'):
    """ Download both prior works and derivative works from https://www.connectedpapers.com.
    
    Args:
        title: The paper's title formatted as a string.
        path: The download path to store your files.
     """

    # TODO(2022-01-01): error handling and setting no interface
    option = Options()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': path}
    option.add_experimental_option('prefs', prefs)
    # get the web
    driver = webdriver.Chrome(executable_path='./web_driver/chromedriver.exe', options=option)
    # paper title you want to search
    url = 'https://www.connectedpapers.com/search?q={}'.format(title)
    url = url.replace(' ', '%20')
    print('your url is: {}'.format(url))

    # open the page
    driver.get(url)
    sleep(2)
    # choose the first search result as default
    driver.find_element(By.XPATH, '//*[@id="open-in-container"]/a[1]').click()
    # switch to another window
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    print('current url is :{}'.format(driver.current_url))

    # switch to prior works page
    driver.find_element(By.XPATH, '//*[@id="desktop-app"]/div[2]/div[1]/div/button[1]').click()
    print(driver.current_url)
    driver.implicitly_wait(3)
    # download prior works
    driver.find_element(By.XPATH, '//*[@id="desktop-app"]/div[2]/div[3]/div[2]/div/div/div/div/span').click()
    sleep(2)
    # switch to derivative works
    driver.find_element(By.XPATH, '//*[@id="desktop-app"]/div[2]/div[1]/div/button[2]').click()
    print(driver.current_url)
    driver.implicitly_wait(3)
    # download derivative works
    driver.find_element(By.XPATH, '//*[@id="desktop-app"]/div[2]/div[3]/div[2]/div/div/div/div/span').click()
    sleep(2)
    print('succeed')
    driver.quit()

# paperwithcode
def search_code(title):
    """search codes on paperwithcode.com. """
    # paper title you want to search
    option = Options()
    # option.add_argument('--headless')
    # option.add_argument('--disable-gpu')
    title = 'Deep Residual Learning for Image Recognition'
    # get the web
    driver = webdriver.Chrome(executable_path='./web_driver/chromedriver.exe', options=option)
    # paper title you want to search
    url = 'https://paperswithcode.com'
    print('your url is: {}'.format(url))
    # open the page
    driver.get(url)
    input_box = driver.find_element(By.XPATH, '//*[@id="id_global_search_input"]')
    input_box.send_keys(title)
    driver.find_element(By.XPATH, '//*[@id="id_global_search_form"]/button/span').click()
    driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[1]/h1/a').click()
    code = driver.find_elements(By.XPATH, '//*[@id="implementations-short-list"]')
    paper_impl = []
    for li in code:
        paper_impl.append(li.find_elements(By.CLASS_NAME, 'paper-impl-cell'))
    for each in paper_impl[0]:
        print(each.text)
    driver.quit()


if __name__ == '__main__':
    title = input('please input paper title: ')
    # download_with_title(title)
    search_code(title)