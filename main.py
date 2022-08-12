import time
from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_DOWN = 150
PROMISED_UP = 10
WEB_DRIVER_PATH = "C:\Development/chromedriver.exe"
TWITTER_EMAIL = "sarunasj82@gmail.com"
TWITTER_PASSWORD = "*********"
USER_NAME = "*********"
SPEED_TEST = "https://www.speedtest.net/result/13530437072"
TWITTER_LOGIN = "https://twitter.com/login"
INTERNET_PROVIDER = "@TeliaCompany"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.up = 0
        self.down = 0
        self.driver = webdriver.Chrome(driver_path)

    def get_internet_speed(self, speed_test):
        self.driver.get(speed_test)
        time.sleep(5)
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(30)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]').text
        time.sleep(20)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]').text
        print(self.down)
        print(self.up)

    def tweet_at_provider(self, twitter_login):
        time.sleep(3)
        self.driver.get(twitter_login)
        time.sleep(3)
        enter_email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        enter_email.send_keys(TWITTER_EMAIL)
        time.sleep(3)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        time.sleep(3)
        user_name_enter = self.driver.find_element(By.CSS_SELECTOR, 'div .css-1dbjc4n input')
        user_name_enter.send_keys(USER_NAME)
        next_b = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
        next_b.click()
        time.sleep(3)
        password_enter = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_enter.send_keys(TWITTER_PASSWORD)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        log_in.click()
        time.sleep(3)

        new_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        new_tweet.click()
        tweet_message = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_message.send_keys(f"Hey {INTERNET_PROVIDER}, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        time.sleep(2)
        tweet_click = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweet_click.click()


bot = InternetSpeedTwitterBot(WEB_DRIVER_PATH)
bot.get_internet_speed(SPEED_TEST)
if float(bot.down) < PROMISED_DOWN or float(bot.up) < PROMISED_UP:
    bot.tweet_at_provider(TWITTER_LOGIN)

