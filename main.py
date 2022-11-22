from selenium import webdriver
from selenium.webdriver.common.by import By


def login(driver, useName, Password):
    try:
        driver.implicitly_wait(10)
        username = driver.find_element(By.NAME, 'username')
        username.send_keys(useName)
        password = driver.find_element(By.NAME, 'password')
        password.send_keys(Password)
        logIN = driver.find_element(By.XPATH, "//button[contains(.,'Log in')]")
        logIN.click()
    except:
        print("I can't log in \U0001F62A")

def Confirm_and_silence_notifications(driver):
    driver.implicitly_wait(10)
    try:
        sava = driver.find_element(By.XPATH, "//button[contains(.,'Not now')]")
        sava.click()
    except:
        pass
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@class="aOOlW   HoLwm "]').click()

def finnd_user_and_post(driver, userToLiked):
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//*[name()='svg' and @aria-label='Search']").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//*[name()='input' and @aria-label='Search input']").send_keys(userToLiked)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//*[@role='none']").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//*[@class='_aagw' or @class='_9AhH0']").click()

def nextPost(driver):
    try:
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//*[name()='svg' and @aria-label='Next']").click()
        print(driver.find_element(By.TAG_NAME, 'img'))
        click_like(driver)
    except:
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//*[name()='svg' and @aria-label='Close']").click()
        print('I finished \U0001F600')


def click_like(driver):
    try:
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//button[@type='button']//*[name()='svg' and @aria-label='Like' and @color='#262626']").click()
        print('like \u2764\ufe0f')
        nextPost(driver)
    except:
        print('unlike')
        nextPost(driver)


def main():
    useName = '<your userName>'
    Password = '<your password>'
    userToLiked = '<userName to liked>'
    chrom_options = webdriver.ChromeOptions()
    prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
    chrom_options.add_experimental_option("prefs", prefs)
    chrom_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=chrom_options)
    driver.get("https://www.instagram.com/")
    login(driver, useName, Password)
    Confirm_and_silence_notifications(driver)
    finnd_user_and_post(driver, userToLiked)
    getPosts = driver.find_element(By.XPATH, '//*[@class="_ac2a" or @class="g47SY "]').text
    print(f'The number of {userToLiked} posts is {getPosts}')
    click_like(driver)

if __name__ == '__main__':
    main()
