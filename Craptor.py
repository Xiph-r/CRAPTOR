from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager


def title():
    print(r'''
		
___________________    _____ _____________________________ __________ 
\_   ___ \______   \  /  _  \\______   \__    ___/\_____  \\______   \
/    \  \/|       _/ /  /_\  \|     ___/ |    |    /   |   \|       _/
\     \___|    |   \/    |    \    |     |    |   /    |    \    |   \
 \______  /____|_  /\____|__  /____|     |____|   \_______  /____|_  /
        \/       \/         \/                            \/       \/ 
  
		''')

#Created by Xipher
def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://web.whatsapp.com/')

    name = input('Enter the name of user or group: ')
    msg = input('Enter your message: ')
    number = int(input('Enter the count: '))

    input('Enter any key to continue after connecting through QR.')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')

    for i in range(number):
        msg_box.send_keys(msg)
        button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[2]/button')
        button.click()
    print('Task completed successfully.')


title()
main()
