from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class auto_reply:
    def __init__(self):
        self.waiting_time = 0.5
        self.number_of_waits= 4     
    def login(self,email,password):
        url = 'https://m.facebook.com/'
        driver.get(url)
        email_entry = driver.find_element(By.ID,'m_login_email')
        email_entry.send_keys(email)
        password_entry = driver.find_element(By.ID,'m_login_password')
        password_entry.send_keys(password)
        password_entry.submit()
        while driver.current_url == url:
            pass
    def open_post(self,post_link):
        driver.get(post_link)
        while '_2b0a"' not in driver.page_source:
            pass
    def get_comments_links(self):
        i=0
        x=0
        while 1:
            j=i
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            if '_108_' in driver.page_source:
                driver.find_element( By.CLASS_NAME,'_108_').click()
                
            comment_links=set()
            for element in driver.find_elements( By.CLASS_NAME,'_2b0a'):
                comment_link = element.get_attribute('data-uri')
                if comment_link:
                    if 'replies' in element.get_attribute('data-uri'):
                        comment_links.add(comment_link)
                        if len(comment_link) == count :
                            break
                        i = len(comment_links)
            if i == j:
                time.sleep(self.waiting_time)
                x+=1
                if x == self.number_of_waits:
                    break
            else:
                x=0
        return comment_links
    def reply(self,count,_reply):
        for comment_link in self.get_comments_links():
            driver.get(comment_link)
            while 'textarea' not in driver.page_source:
                pass
            textarea = driver.find_element(By.TAG_NAME,'textarea')
            textarea.click()
            textarea.send_keys(_reply)
            textarea.submit()
        driver.quit()
email = input('Enter email : ')
password = input('Enter Password : ')
post_link = input('Enter Url Post : ').replace('https://www','https://m')
_reply = input('reply :')
count = int(input('Number Of Responses : '))
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
_auto_reply = auto_reply()
_auto_reply.login(email,password)

_auto_reply.open_post(post_link)
_auto_reply.reply(count,_reply)







        
