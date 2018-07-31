import os
from selenium import webdriver
import functools
import operator
from ChintuCourt.config import *

class GetHighCourtHomePage():

    def get_home_page(self):

        driver_location=pass_driver_location
        os.environ["webdriver.Chrome.driver"]=driver_location
        driver=webdriver.Chrome(driver_location)

        driver.maximize_window()
        driver.get("http://hc.tap.nic.in/")
        window_required=driver.current_window_handle
        print("required window's ID:"+window_required)

        driver.implicitly_wait(2)

        windows_opened_list=driver.window_handles
        print(str(len(windows_opened_list))+" windows are opened in the driver.")
        print("They are:"+str(windows_opened_list))

        for window1 in windows_opened_list:
            if window1!=window_required:
                driver.close()
            else:

                print("'"+window1+"' is the wanted window.")
                unnecessary_windows_list=list(filter(functools.partial(operator.ne, window1), windows_opened_list))
                if len(unnecessary_windows_list)<2:
                    print("1 unwanted window:"+str(unnecessary_windows_list))
                else:
                    print(str(len(unnecessary_windows_list))+" unwanted windows list:"+str(unnecessary_windows_list))

                for unwanted_window in unnecessary_windows_list:
                    driver.switch_to.window(unwanted_window)
                    print("Closing unwanted window '"+unwanted_window+"'")
                    driver.close()
                break
        driver.switch_to.window(window_required)
        return driver