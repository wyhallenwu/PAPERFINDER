from selenium import webdriver

def download_with_title(title):
    """ Download both prior works and derivative works from https://www.connectedpapers.com.
    
    Args:
        title: The paper's title formatted as a string.
     """
    # get the web
    driver = webdriver.Chrome('./web_driver/chromedriver.exe')
    # paper title you want to search
    url = 'https://www.connectedpapers.com/search?q={}'.format(title)
    print('your url is: {}'.format(url))
    url = url.replace(' ', '%20')
    # open the page
    driver.get(url)
    # choose the first search result as default
    driver.find_element_by_xpath('//*[@id="open-in-container"]/a[1]').click()
    # switch to another window
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    print(driver.current_url)
    # switch to prior works page
    driver.find_element_by_xpath('//*[@id="desktop-app"]/div[2]/div[1]/div/button[1]').click()
    # download prior works
    driver.find_element_by_xpath('//*[@id="desktop-app"]/div[2]/div[3]/div[2]/div/div/div/div/span').click()
    # switch to derivative works
    driver.find_element_by_xpath('//*[@id="desktop-app"]/div[2]/div[1]/div/button[2]').click()
    # download derivative works
    driver.find_element_by_xpath('//*[@id="desktop-app"]/div[2]/div[3]/div[2]/div/div/div/div/span').click()
