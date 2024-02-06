from WebDriver import WebDriver
import pandas as pd
from selenium.webdriver.common.by import By
from time import sleep

if __name__ == '__main__':
    url = 'https://job.incruit.com/jobdb_list/searchjob.asp?cate=occu'
    driver = WebDriver(False, False)
    driver.open_url(url)
    buttons = driver.get_elements_by_name('occ1_list')
    refresh = driver.get_element_by_class('shb-btn-ref')

    shb_labels = driver.get_elements_by_class('shb-label')
    print(len(shb_labels))
    print()
    except_idx = 0
    for button in buttons[:1]:
        button.click()
        refresh.click()
        sub_buttons = driver.get_elements_by_name('occ2_list')
        iter_idx = len(sub_buttons) - except_idx
        for i in range(iter_idx):
            sub_buttons[i].click()
            refresh.click()
        except_idx = len(sub_buttons)
    shb_labels = driver.get_elements_by_class('shb-label')
    print(len(shb_labels))
    refresh.click()
    # occ3_div
    # driver.close_url()
