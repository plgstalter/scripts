from selenium import webdriver
from sys import argv
from time import sleep

def ip_handler(dr, ip: str, i):
    tab_name = f"tab{i}"
    dr.execute_script(f"window.open('about:blank', '{tab_name}');")
    dr.switch_to_window(tab_name)
    dr.get('https://infotracer.com/reverse-ip-lookup/')
    sleep(2)
    dr.find_element_by_xpath('//*[@id="tab-01"]/div/form/div/div[1]/input').send_keys(ip)
    sleep(0.1)
    cookie_button_1 = dr.find_elements_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
    if  len(cookie_button_1) > 0:
        cookie_button_1[0].click()
    sleep(0.1)
    cookie_button_2 = dr.find_elements_by_xpath('//*[@id="tab-01"]/div/form/div/div[2]/button')
    if  len(cookie_button_2) > 0:
        cookie_button_2[0].click()
    sleep(0.1)
    dr.find_element_by_xpath('//*[@id="reg_disc"]/div/div[2]/a[2]').click()

def main(file_name: str):
    i = 0
    reverse_ip_website = open(file_name, 'r')
    dr = webdriver.Firefox()
    for line in reverse_ip_website.readlines():
        ip_handler(dr, line, i)
        i += 1
    reverse_ip_website.close()
    dr.close()

if  __name__=="__main__":
    if  len(argv) > 1:
        main(argv[1])
