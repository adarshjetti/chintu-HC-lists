import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from ChintuCourt.config import *
from ChintuCourt.createFolder import *
from ChintuCourt.getHighCourtHomePage import GetHighCourtHomePage

class ListingDate():

    def find_listing_date(self):

        case_status_info_locator="//a[contains(text(),'Case Status Information') and (@href='http://distcourts.tap.nic.in/csis')]"
        case_type_locator="ctype"
        case_number_locator="cno"
        case_year_locator="cyear"
        submit_btn_locator="searchone"
        case_details_locator="casedetails"
        ld_date_locator="//td[text()='Listing Date']//following-sibling::td"

        homepage = GetHighCourtHomePage()
        browser = homepage.get_home_page()

        case_status_info_element=browser.find_element_by_xpath(case_status_info_locator)
        case_status_info_element.click()

        case_type_element=browser.find_element_by_id(case_type_locator)
        case_type_element.send_keys("AS")

        case_number_element=browser.find_element_by_id(case_number_locator)
        case_number_element.send_keys("199")

        case_year_element=browser.find_element_by_id(case_year_locator)
        case_year_element.send_keys("2018")

        submit_btn_element=browser.find_element_by_id(submit_btn_locator)
        submit_btn_element.click()

        wait=WebDriverWait(browser,15,0.5)
        wait.until(expected_conditions.visibility_of_element_located(("id",case_details_locator)))

        ld_date_element=browser.find_element_by_xpath(ld_date_locator)
        ld_date=ld_date_element.text
        print("-"*50)
        print("Listing Date :"+ld_date)
        if ld_date != "8":
            path=pass_ListingDate_folder_path
            catch_folder_name_and_path=create_new_result_folder(path,__class__.__name__)
            result_folder_path = catch_folder_name_and_path[1]
            print("folder path:" + result_folder_path)
            folder_name = catch_folder_name_and_path[0]
            print("folder_name:" + folder_name)
            screenshot_name = folder_name+".png"
            print("screenshot_name:"+screenshot_name)
            destination_file = result_folder_path + "\\" + screenshot_name
            browser.execute_script("arguments[0].scrollIntoView(true);", ld_date_element)
            browser.save_screenshot(destination_file)
        print("-" * 50)

        time.sleep(3)

obj=ListingDate()
obj.find_listing_date()
