from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import datetime


driver = webdriver.Chrome('/Users/cc/Downloads/chromedriver')
wait = WebDriverWait(driver, 10)
driver.get('https://www.smiles.com.ar/')
driver.maximize_window()

# find the origin search box and click on it
origin_airport = "BUE"
destination_airport = "MIA"

# find the origin search box and send origin airport
origin = wait.until(EC.element_to_be_clickable((By.ID, 'airport-origin')))
origin.send_keys(origin_airport + Keys.ENTER)
# find the destination search box and send destination airport
destination = driver.find_element(By.ID, "airport-destination")
destination.send_keys(destination_airport + Keys.ENTER)

# find the one way button and click it
# one_way_btn = driver.find_element(
#     By.XPATH, "/html/body/div[3]/div/main/div[1]/div[2]/div/form/div[2]/div/div[2]/div/div[1]/button[2]")
# one_way_btn.click()

one_way_btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[3]/div/main/div[1]/div[2]/div/form/div[2]/div/div[2]/div/div[1]/button[2]"))
)
one_way_btn.click()

# find the date field and click it
date_picker = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
      (By.XPATH, "/html/body/div[3]/div/main/div[1]/div[2]/div/form/div[2]/div/div[3]/div[1]/div[2]/div/div[1]/div/div/div[1]"))
)
date_picker.click()

date = 'martes, 12 de julio de 2022'

# click on a date of the calendar (July 15, 2022). BY XPATH. THIS FINDS THE DATE OF THE CALENDAR
origin_date = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
      (By.XPATH, "/html/body/div[3]/div/main/div[1]/div[2]/div/form/div[2]/div/div[3]/div[1]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[@aria-label='{}']".format(date)))
)
print(origin_date.text)
origin_date.click()

# search_button = driver.find_element(By.CLASS_NAME, "search")
# search_button.click()
# origin_date = driver.find_element(By.XPATH, "//button[@aria-label='martes, 12 de julio de 2022']")
# origin_date.click()


# origin_date = driver.find_elements(By.XPATH, "//button[aria-label='martes, 12 de julio de 2022']")
# origin_date.click()

#identify list of all dates
# days = driver.find_elements(By.XPATH, "/html/body/div[3]/div/main/div[1]/div[2]/div/form/div[2]/div/div[3]/div[1]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td")
# # iterate over list
# for i in days:
#   print(i.text)
# # verify required date then click
#   if i.text == '12':
#     i.click()
#     break
# # get selected date
# s = date_picker.get_attribute('value')
# print("Date entered is: ")
# print(s)

# current_month_calendar_element = <div class="CalendarMonth CalendarMonth_1" data-visible="true" style="padding: 0px 13px;"><div class="CalendarMonth_caption CalendarMonth_caption_1"><span class="month-name">julio</span><br><span class="year">2022</span></div><table class="CalendarMonth_table CalendarMonth_table_1" role="presentation"><tbody><tr><td></td><td></td><td></td><td></td><td></td><td class="CalendarDay CalendarDay_1 CalendarDay__defaultCursor CalendarDay__defaultCursor_2 CalendarDay__default CalendarDay__default_3 CalendarDay__blocked_out_of_range CalendarDay__blocked_out_of_range_4" role="button" aria-disabled="true" aria-label="Not available. viernes, 1 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">1</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2 CalendarDay__today CalendarDay__today_3 CalendarDay__selected CalendarDay__selected_4" role="button" aria-disabled="false" aria-label="Selected. sábado, 2 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">2</td></tr><tr><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2 CalendarDay__lastDayOfWeek CalendarDay__lastDayOfWeek_3" role="button" aria-disabled="false" aria-label="domingo, 3 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">3</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2 CalendarDay__firstDayOfWeek CalendarDay__firstDayOfWeek_3" role="button" aria-disabled="false" aria-label="lunes, 4 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">4</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="martes, 5 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">5</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="miércoles, 6 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">6</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="jueves, 7 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">7</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="viernes, 8 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">8</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="sábado, 9 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">9</td></tr><tr><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2 CalendarDay__lastDayOfWeek CalendarDay__lastDayOfWeek_3" role="button" aria-disabled="false" aria-label="domingo, 10 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">10</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2 CalendarDay__firstDayOfWeek CalendarDay__firstDayOfWeek_3" role="button" aria-disabled="false" aria-label="lunes, 11 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">11</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="martes, 12 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">12</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="miércoles, 13 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">13</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="jueves, 14 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">14</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="viernes, 15 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">15</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="sábado, 16 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">16</td></tr><tr><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2 CalendarDay__lastDayOfWeek CalendarDay__lastDayOfWeek_3" role="button" aria-disabled="false" aria-label="domingo, 17 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">17</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2 CalendarDay__firstDayOfWeek CalendarDay__firstDayOfWeek_3" role="button" aria-disabled="false" aria-label="lunes, 18 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">18</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="martes, 19 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">19</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="miércoles, 20 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">20</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="jueves, 21 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">21</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="viernes, 22 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">22</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="sábado, 23 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">23</td></tr><tr><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2 CalendarDay__lastDayOfWeek CalendarDay__lastDayOfWeek_3" role="button" aria-disabled="false" aria-label="domingo, 24 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">24</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2 CalendarDay__firstDayOfWeek CalendarDay__firstDayOfWeek_3" role="button" aria-disabled="false" aria-label="lunes, 25 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">25</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="martes, 26 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">26</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="miércoles, 27 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">27</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="jueves, 28 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">28</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="viernes, 29 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">29</td><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-disabled="false" aria-label="sábado, 30 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">30</td></tr><tr><td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2 CalendarDay__lastDayOfWeek CalendarDay__lastDayOfWeek_3" role="button" aria-disabled="false" aria-label="domingo, 31 de julio de 2022" tabindex="-1" style="width: 39px; height: 38px;">31</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table></div>
# element that has the
# one_way_btn = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located(
#         (By.XPATH, '/html/body/div[3]/div/main/div[1]/div[2]/div/form/div[2]/div/div[2]/div/div[1]/button[2]]'))
# )
# one_way_btn.click()

# one_way_btn = driver.find_element(By.XPATH,"//*[@id='root']/div/main/div[1]/div[2]/div/form/div[2]/div/div[2]/div/div[1]/button[2]")
# calendar = driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div[1]/div[2]/div/form/div[2]/div/div[3]/div[1]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[1]/input")
# calendar.click()
# start_date = driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div[1]/div[2]/div/form/div[2]/div/div[3]/div[1]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[3]/div/table/tbody/tr[3]/td[3]")


# search_button = driver.find_element(By.CLASS_NAME, "search")
# search_button.click()


# start_date = wait.until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "#d1-btn")))
# end_date = wait.until(EC.presence_of_element_located(
#     (By.CSS_SELECTOR, "#d2-btn")))
# start_date.click()


# date format in calendar: 'aria-label': 'miercoles, 20 de Julio de 2022'

# convert the date from 'Aug 12, 2021' to 'August 2021'

# def date_formater(date):
#     d = datetime.datetime.strptime(date, '%b %d, %Y')
#     return d.strftime('%B %Y')

# # create a function to right click until the date is found in the calendar


# def press_right_arrow_until_date_is_found(date):
#     # get the text of the initial calendar
#     current_calendar = driver.find_element_by_class_name("uitk-calendar").text
#     # while the date does not appear in the calendar view press right arrow until it does
#     while(date_formater(date) not in current_calendar):
#         right_arrow = driver.find_elements_by_xpath(
#             "//button[@data-stid='date-picker-paging']")[1]
#         right_arrow.click()
#         current_calendar = driver.find_element_by_class_name(
#             "uitk-calendar").text

# # function to select the dates using xpath with the unique attribute. Ex: aria-label="Aug 12, 2021"


# def select_date(start_date_calendar, end_date_calendar):
#     # press right until the start date is found
#     press_right_arrow_until_date_is_found(start_date_calendar)
#     # click on the date that matches the xpath with the aria-label
#     driver.find_element_by_xpath(
#         "//button[@aria-label='{}']".format(start_date_calendar)).click()

#     # press right until the end date is found
#     press_right_arrow_until_date_is_found(end_date_calendar)
#     # click on the date that matches the xpath with the aria-label
#     driver.find_element_by_xpath(
#         "//button[@aria-label='{}']".format(end_date_calendar)).click()


# select_date('Sep 12, 2021', 'Dec 9, 2021')
