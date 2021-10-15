from selenium import webdriver
import sys
from utils import parseDate
import time

# To work with dropdown menus
from selenium.webdriver.support.ui import Select


# Need to specify the path for the Chrome web driver
path = "/opt/ChromeDriver/chromedriver"
driver = webdriver.Chrome(path)
# wait = WebDriverWait(driver, 5)
url = "https://intranet.upv.es/pls/soalu/est_intranet.Ni_portal_n"
driver.get(url)


# find login fields and input login params
dni = driver.find_element_by_name("dni")
dni.send_keys(sys.argv[1])
password = driver.find_element_by_name("clau")
password.send_keys(sys.argv[2])

# login into the intranet and redirect to pitch reservation site
driver.find_element_by_class_name("upv_btsubmit").click()
driver.find_element_by_xpath('//*[@id="intranet"]/a[2]').click()
driver.find_element_by_xpath('//*[@id="elemento_1001"]/tbody/tr/td[1]/p/a').click()

# Now select PADEL from the dropdown menu and wait until courts and dates are displayed
dropdown = Select(driver.find_element_by_name("deporte"))
# select by visible text
dropdown.select_by_visible_text("PADEL")

courtDates = driver.find_elements_by_class_name("upv_btreset")
formatedDate = parseDate(int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
for day in courtDates:
    # Get all available dates and check the day we want to book
    if day.get_attribute("value") == formatedDate:
        day.click()
        break

# Get the table showing court times based on selected xpath
courtTableButton = driver.find_element_by_xpath(
    "/html/body/div[2]/div/div/div[5]/table[2]/tbody/tr/td[{}]/div/div/table/tbody/tr[{}]/td[2]".format(
        sys.argv[6], (int(sys.argv[7]) - 7)
    )
)
# Now that we have selected the correct table row we can click the link
courtTableButton.click()

time.sleep(0.5)

# Now select Si o No from the dropdown menu
dropdown = Select(driver.find_element_by_id("conforme"))
# select by visible text
dropdown.select_by_visible_text("SI")


driver.find_element_by_xpath('//*[@id="t8343409"]/tbody/tr/td/input[2]').click()
