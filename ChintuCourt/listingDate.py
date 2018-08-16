import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import datetime
from ChintuCourt.config import *
from ChintuCourt.createFolder import *
from ChintuCourt.getHighCourtHomePage import GetHighCourtHomePage
from ChintuCourt.sendSMS import *
from ChintuCourt.zipAFolder import *
from ChintuCourt.sendEmailAttachment import *
from ChintuCourt.sendEmailMultipleAttachments import *
import traceback


class ListingDate():

    def find_listing_date(self):

        case_status_info_locator="//a[contains(normalize-space(text()),'Case Status Information') and (@href='http://distcourts.tap.nic.in/csis')]"
        case_type_locator="ctype"
        case_number_locator="cno"
        case_year_locator="cyear"
        submit_btn_locator="searchone"
        case_details_locator="casedetails"
        ld_date_locator="//td[text()='Listing Date']//following-sibling::td"
        main_num_locator="//td/b[text()='Main Number']/..//following-sibling::td[1]"


        homepage = GetHighCourtHomePage()
        browser = homepage.get_home_page()
        browser.implicitly_wait(2)

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

        main_num_element=browser.find_element_by_xpath(main_num_locator)
        main_num=main_num_element.text

        wait=WebDriverWait(browser,15,0.5)
        wait.until(expected_conditions.visibility_of_element_located(("id",case_details_locator)))

        ld_date_element=browser.find_element_by_xpath(ld_date_locator)
        ld_date=ld_date_element.text
        print("-"*50)
        line1_to_be_printed="Listing Date : "+ld_date

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
            #browser.execute_script("arguments[0].scrollIntoView(true);", ld_date_element)
            browser.save_screenshot(destination_file)
            line1="Hai Abhilash,\n\nYour case '"+main_num+"' has been assigned a listing date as on "+str(datetime.date.today())+"\n\n"+line1_to_be_printed+"\n\n"
            email_line = "A zip file containing captured screenshot is attached.Please check it.\n\nThank You!"
            sms_line = "A zip file containing captured screenshot is sent to your mail.Please check it.\n\nThank You!"
            output_line="A screenshot '"+screenshot_name+"' is captured and saved to the path:'"+result_folder_path+"'."
            print(output_line)

            email_body=line1+email_line
            email_subject="Listing date Alert:You've got a listing date"
            sms_body=line1+sms_line

            zip_file_path=zip_a_folder(path,folder_name,result_folder_path)
            try:
                send_email_with_attachments(email_subject,email_body,zip_file_path)
                send_email_with_multiple_attachments(email_subject,email_body,result_folder_path)
            except:
                print("failed to send email!")
            try:
                send_ponni_sms("Listing date Alert!!\n\n"+sms_body)
                send_chintu_sms("Listing date Alert!!\n\n"+sms_body)
            except:
                print("failed to send email!")

        else:
            print("Listing date is not assigned to your case '"+main_num+"' as on "+str(datetime.date.today()))
        print("-" * 50)
        browser.close()

        #time.sleep(3)

log_file_name="ListingDate_failed_traceback.txt"
log = open(log_file_name, "w")
program_start_time = datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")
try:
    obj=ListingDate()
    obj.find_listing_date()
    log.close()
    current_directory_path = os.path.dirname(os.path.abspath(__file__))
    get_log_file_path = current_directory_path + "\\" + log_file_name
    os.remove(get_log_file_path)
except:
    program_failed_time=datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")
    traceback.print_exc(file=log)
    log.close()
    current_directory_path=os.path.dirname(os.path.abspath(__file__))
    get_log_file_path=current_directory_path+"\\"+log_file_name
    #print(get_log_file_path)
    print("Program failed!\n'"+os.path.basename(__file__)+"' Program started on "+program_start_time+" has failed at "+program_failed_time+".\nFailed report '"+log_file_name+"' is generated.\nPlease look into it.")
    email_bod="Hi Abhilash,\n\n'"+os.path.basename(__file__)+"' Program started on "+program_start_time+" has failed at "+program_failed_time+".\nFailed report '"+log_file_name+"' is attached.\nPlease look into it.\n\nThank You!"
    email_sub="Program failed Alert!!"
    send_email_with_attachments(email_sub,email_bod,get_log_file_path)
    sms_text="Program failed Alert!!\n\n'"+os.path.basename(__file__)+"' Program started on "+program_start_time+" has failed at "+program_failed_time+".\nFailed report '"+log_file_name+"' is sent to your email.\nPlease look into it\nThank You!."
    send_ponni_sms(sms_text)


