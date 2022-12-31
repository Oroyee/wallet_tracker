from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from datetime import date

opt = Options()
opt.page_load_strategy = "eager"
opt.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=opt)

driver.execute_script("window.open('');")
# switch to new window with switch_to.window()s
driver.switch_to.window(driver.window_handles[0])
driver.get("https://etherscan.io/token/0x3506424f91fd33084466f402d5d97f05f8e3b4af#balances")

driver.implicitly_wait(5)
time.sleep(4)
driver.switch_to.frame(driver.find_element(By.ID,"tokeholdersiframe"))

    
def get_all_data():
    today = date.today()
    fileName = "Chiliz_Top50_" + str(today)
    allData = []
    # iterate over the rows, to ignore the headers we have started the i with '1'
    for i in range(1, 51):
        # reset the row data every time
        ro = []
        for j in range(1, 5) :
            ro.append(driver.find_element("xpath","/html/body/div[2]/div[3]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text)
            ro.append("\t")
        # add the row data to allData of the self.table
        ro.append("\n")
        allData.append(ro)
    with open(fileName,'w')as fp:
        for item in allData:
            for i in item:
                fp.write(i)
        print("done") 
    return allData

print("\nAll table data : ", get_all_data())