from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://chartink.com')


screener_tab = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[2]/div/div[2]/a')
screener_tab.click()

search_screener = driver.find_element_by_xpath(
    '/html/body/div[2]/div[2]/form/div/div/input')
search_screener.send_keys('Filter_Strength')

search_click = driver.find_element_by_xpath(
    '/html/body/div[2]/div[2]/form/div/div/span/button')
search_click.click()

select_scan = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/table/tbody/tr/td/a/strong')
select_scan.click()

run_scan = driver.find_element_by_xpath(
    '//*[@id="root"]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/button[1]')
run_scan.click()

dl_scan = driver.find_element_by_xpath(
    '//*[@id="DataTables_Table_0_wrapper"]/div[1]/div/button[3]/span')
dl_scan.click()
