from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Your Instagram account
IG = "YOUR IG USERNAME"
IGPW = "YOUR IG PASSWORD"

#Enter an account you think it shares similar target audience with your own account
TARGET_ACCT = "YOUR CHOICE OF IG ACCOUNT"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    #log in Instagram
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        #Reject the cokkies
        reject_cookies = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        reject_cookies.click()
        time.sleep(3)
        #Enter IG username and password
        enter_username = self.driver.find_element(By.XPATH, "//input[@aria-label='Phone number, username or email address']")
        enter_username.send_keys(IG)
        enter_pw = self.driver.find_element(By.XPATH, "//input[@aria-label='Password']")
        enter_pw.send_keys(IGPW)
        enter_pw.send_keys(Keys.ENTER)
        time.sleep(3)
        #Save log in information
        not_now = self.driver.find_elements(By.TAG_NAME,'button')
        not_now[0].click()
        time.sleep(3)
        #Turn off notification
        turn_off_notice = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        turn_off_notice.click()


    #Find the target followers that belong to an account you think it shares similar demographics with your own IG
    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCT}/")

        #open the "followers" pop up window or page
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCT}/followers/")

        time.sleep(5)
        #scrolling the followers pop up window
        pop_up = self.driver.find_element(By.CLASS_NAME, '_aano')
        for i in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)
            time.sleep(3)

    #Following the targeted followers
    def follow(self):
        #getting all the follow buttons
        all_follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div._aano button._acan._acap._acas._aj1-')
        for button in all_follow_buttons:
            try:
                button.click()
                time.sleep(2)
            #handle already followed people cases by clicking "cancel"
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                cancel_button.click()

    #Exit the bot after a while to avoid being identified as a bot
    def exit_bot(self):
        time.sleep(30)
        self.driver.quit()
        print("Take a break!")

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
bot.exit_bot()

