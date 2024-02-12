from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

url = "https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1#anchorGICnt_1"

driver = webdriver.Chrome()
driver.get(url)
# 페이지 맨 위로 스크롤
# 페이지 맨 위로 스크롤
driver.execute_script("window.scrollTo(0, 0);")

# 버튼 요소 선택
button_xpath = '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dt/p'
button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_xpath)))

# 클릭
button.click()

# 두 번째 버튼 요소 선택
button2_xpath = '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[1]/dd/div[1]/ul/li[6]/label/span'
button2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button2_xpath)))

# 클릭
button2.click()

button3_xpath = '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[2]/dd/div[1]/ul[2]/li[1]/label/span'
button3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button3_xpath)))
# 클릭
button3.click()

# 스크롤을 내리면서 각 요소를 클릭합니다.
for i in range(2, 20):
    try:
        # 버튼 요소 선택
        button_xpath = f'/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[2]/dd/div[1]/ul[2]/li[{i}]/label/span'
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_xpath)))
        # 버튼 클릭
        button.click()

        # 페이지를 스크롤 다운하여 다음 요소로 이동합니다.
        body = driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)

    except Exception as e:
        print(f"버튼 클릭에 실패했습니다: {e}")

# 작업이 끝났다면, 다시 맨 아래로 스크롤합니다.
body.send_keys(Keys.END)
time.sleep(2)

# 특정 엘리먼트가 나타날 때까지 스크롤 다운
try:
    element_present = EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div[1]/select'))
    WebDriverWait(driver, timeout=10).until(element_present)
except Exception as e:
    print("특정 엘리먼트가 발견되지 않았습니다. 스크롤을 내리면서 기다리겠습니다.")

# 특정 엘리먼트 클릭
try:
    target_element = driver.find_element(By.XPATH,
                                         '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div[1]/select')
    target_element.click()
    print("특정 엘리먼트를 클릭했습니다.")
except Exception as e:
    print("특정 엘리먼트를 클릭하는데 실패했습니다.")

# 특정 자식 엘리먼트 클릭 (예시로 첫 번째 옵션 클릭)
try:
    option_element = driver.find_element(By.XPATH,
                                         '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div[1]/select/option[2]')
    option_element.click()
    print("자식 엘리먼트를 클릭했습니다.")
except Exception as e:
    print("자식 엘리먼트를 클릭하는데 실패했습니다.")

# 나머지 스크롤 다운 코드를 필요한 만큼 반복
# 이 부분을 필요한 만큼 반복하여 페이지를 스크롤 다운합니다.
time.sleep(3)

page_button_xpath_pattern = '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[6]/div/ul/li[{}]/a'
page_button_next_xpath_pattern = '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[6]/div/p[{}]/a'
# 초기 페이지 버튼 번호
page_button_number = 2
page_next_button_number = page_button_number + 1
# 원하는 작업을 수행하고 나서 브라우저 닫기
while True:
    try:
        for tr_index in range(1, 41):  # tr[1]부터 tr[40]까지
            try:
                # tr[현재 행 + 1]이 화면에 보이지 않으면 스크롤을 내리고 기다린다.
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                f'/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{tr_index}]/td[2]/div/strong/a')))
                a_element = driver.find_element(By.XPATH,
                                                f'/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{tr_index}]/td[1]/a')
                a_text = a_element.text
                print(f"회사이름 {tr_index}: {a_text}")

                text_element = driver.find_element(By.XPATH,
                                                   f'/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{tr_index}]/td[2]/div/strong/a')
                text_value = text_element.text
                print(f"회사설명{tr_index}: {text_value}")

                for i in range(1, 5):
                    span_element = driver.find_element(By.XPATH,
                                                       f'/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{tr_index}]/td[2]/div/p[1]/span[{i}]')
                    span_text = span_element.text
                    print(f"설명 {i} 텍스트 {tr_index}: {span_text}")

            except Exception as e:
                print(f"텍스트 {tr_index}를 가져오는데 실패했습니다.")

            # 중간에 스크롤 내리기
           # if tr_index < 40:
            #    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
             #   time.sleep(0.5)  # 스크롤 후 대기 시간 (동적으로 로딩되는 경우 대기 시간이 필요할 수 있습니다.)
        # 페이지 버튼 클릭
        page_button_xpath = page_button_xpath_pattern.format(page_button_number)
        print(page_button_xpath)
        # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        # time.sleep(0.5)
        page_button = driver.find_element(By.XPATH, page_button_xpath)
        page_button.click()
        time.sleep(0.5)
        page_button_number += 1
        page_next_button_number += 1
        if str(page_button_number).endswith('1'):
        if page_button_number == 11:
            page_button_number = 2
        if page_next_button_number == 11:
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(0.5)
            page_next_button = driver.find_element(By.XPATH,
                                                   '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[6]/div/p/a')
            page_next_button.click()
            page_next_button_number += 1
        if (page_next_button_number > 11 and page_next_button_number % 10 == 1):
            page_next_button_xpath = page_button_next_xpath_pattern.format(page_next_button_number // 10)
            print(page_next_button_xpath)
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(0.5)
            page_next_button = driver.find_element(By.XPATH, page_next_button_xpath)
            page_next_button.click()
            page_next_button_number += 1
    except Exception as e:
        print("페이지 버튼이 더 이상 없습니다.")
        break

driver.quit()
