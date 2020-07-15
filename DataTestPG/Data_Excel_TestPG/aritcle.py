# encoding=utf-8

from selenium import webdriver

driver = webdriver.Chrome(r'/Users/cp/PycharmProjects/DataTestPG/chromedriver')
test_url = 'https://www.zhihu.com/question/28122825'
driver.get(test_url)


aritcle = driver.find_element_by_xpath('//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[1]/div/div[2]/div[1]')
a = aritcle.text()
print(a)

