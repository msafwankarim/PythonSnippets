
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#       Author:     Safwan                                                                  #
#       Date:       Sunday, ‎27 ‎September ‎2020, ‏‎5:52:17 PM                                   #
#       Brief:      Following code will add comments on facebook post                       #
#                   * Used to work with older facebook version. Not tested on current one   #
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome(executable_path = r"C:\Users\Safwan\Downloads\Compressed\chromedriver.exe")
driver.get("http://www.facebook.com/")

input("Enter credentials on Login screen and Press any key to when target page is fully loaded . . .")

def comment(word, index):
    commentBox = driver.find_elements_by_css_selector("div._1mf._1mj")[index]
    commentBox.send_keys(word)

def startSending():
    good_words = ['admirable', 'adorable', 'alluring', 'angelic', 'appealing', 'beauteous', 'bewitching', 'captivating', 'charming', 'classy', 'comely', 'cute', 'dazzling', 'delicate', 'delightful', 'divine', 'elegant', 'enthralling', 'enticing', 'excellent', 'exquisite', 'fair', 'fascinating', 'fetching', 'fine', 'foxy', 'good-looking', 'gorgeous', 'graceful', 'grand', 'handsome', 'ideal', 'inviting', 'lovely', 'magnetic', 'magnificent', 'marvelous', 'mesmeric', 'nice', 'pleasing', 'pretty', 'pulchritudinous', 'radiant', 'ravishing', 'refined', 'resplendent', 'shapely', 'slightly', 'splendid statuesque', 'stunning', 'sublime', 'superb', 'symmetrical', 'taking', 'tantalizing', 'teasing', 'tempting', 'well-formed', 'winning', 'wonderful']
    for i in range(3):
        for word in good_words:
            comment(word+Keys.ENTER, 0)
            time.sleep(2)

def main():
    startSending()
    os.system("pause")
    driver.close()


main()
