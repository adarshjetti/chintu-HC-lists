import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import shutil
import sys
import datetime
from ChintuCourt.config import *
from ChintuCourt.createFolder import *
from ChintuCourt.getHighCourtHomePage import GetHighCourtHomePage
from ChintuCourt.sendSMS import *
from ChintuCourt.zipAFolder import *
from ChintuCourt.sendEmailAttachment import *
from ChintuCourt.sendEmailMultipleAttachments import *
import traceback
import numpy as np

'''class ProgramFailedError(Exception):
    pass
    def __init__(self,value="'ProgramFailedError'"):
        self.value = value
    def __str__(self):
        return(repr(self.value))'''

class GetSearchDatesPage():
    def get_search_dates_page(self):
        cause_list_btn_locator="//td/a[@href='http://hc.tap.nic.in/Hcdbs/search.do']"
        daily_list_btn_locator="//input[@value='DAILY LIST']"
        cause_list_date_select_locator="listdate"

        homepage=GetHighCourtHomePage()
        browser=homepage.get_home_page()
        browser.implicitly_wait(3)

        cause_list_btn_element=browser.find_element_by_xpath(cause_list_btn_locator)
        cause_list_btn_element.click()
        #time.sleep(0.25)

        daily_list_btn_element= browser.find_element_by_xpath(daily_list_btn_locator)
        daily_list_btn_element.click()
        #time.sleep(0.25)

        cause_list_date_select_element = browser.find_element_by_id(cause_list_date_select_locator)
        date_selecting = Select(cause_list_date_select_element)
        select_options_list = date_selecting.options

        date_index_dictionary = {}
        print(str(len(select_options_list)) + " options are present")
        for option in select_options_list:
            date_index_dictionary[option.get_attribute("value")] = int(option.get_attribute("index"))
        print(date_index_dictionary)

        selected_date = None
        selected_date_index = None
        date_to_be_checked = pass_todays_date
        #print("starting while loop")
        while str(date_to_be_checked) <= str(max(date_index_dictionary.keys())):
            print("date being checked:" + str(date_to_be_checked))
            if str(date_to_be_checked) in date_index_dictionary:
                selected_date = str(date_to_be_checked)
                print(selected_date + " is chosen date")
                selected_date_index = date_index_dictionary[str(date_to_be_checked)]
                #print(selected_date_index)
                #print(type(selected_date_index))
            date_to_be_checked = date_to_be_checked + datetime.timedelta(days=1)
            #print(date_to_be_checked)
            if selected_date_index in date_index_dictionary.values():
                break
        #print("loop ended")
        print(selected_date + " is the selected date.And " + str(selected_date_index) + " is its index.")

        #index_and_option_list = [browser, selected_date_index, date_index_dictionary]
        #return index_and_option_list
        browser_index_and_dict_list = [browser, selected_date_index,date_index_dictionary]
        return browser_index_and_dict_list

class CauseList():
    def __init__(self,adv_code,screenshots_to_be_saved_path):
        self.advocate_code=adv_code
        if (str(self.advocate_code) == "13780"):
            self.advocate_name="K Ramachandra"
        elif (str(self.advocate_code) == "13197"):
            self.advocate_name="M Chalapati Rao"
        self.ss_folder_path=screenshots_to_be_saved_path

    def find_time_and_location(self,get_index,get_d_and_i_dict):

        datespage = GetSearchDatesPage()
        b_and_i_list = datespage.get_search_dates_page()
        browser = b_and_i_list[0]
        browser.implicitly_wait(3)
        
        cause_list_date_select_locator = "listdate"
        advocate_code_wise_btn_locator = "//input[@value='ADVOCATE CODE WISE']"
        cause_list_date_locator = "//table//td[text()='Cause List Date:']//following-sibling::td"
        advocate_code_text_locator = "advcd"
        submit_btn_locator = "//input[@value='submit']"
        t_data_details_locator = "//tbody//td"
        get_print_detail_locator = "(//tbody // td[contains(text(),'{0}')] /../..// td/../..)[{1}]"
        get_print_head_locator = "(//td[contains(text(),'{0}')]//parent::tr//parent::tbody//preceding-sibling::thead)[{1}]"
        case_num = pass_case_num

        cause_list_date_select_element = browser.find_element_by_id(cause_list_date_select_locator)
        date_selecting = Select(cause_list_date_select_element)

        local_select_options_list = date_selecting.options

        local_date_index_dictionary = {}
        print(str(len(local_select_options_list)) + " options are present")
        for option in local_select_options_list:
            local_date_index_dictionary[option.get_attribute("value")] = int(option.get_attribute("index"))

        print("get_d_and_i_dict           :"+str(get_d_and_i_dict))
        print("local_date_index_dictionary:"+str(local_date_index_dictionary))

        if get_d_and_i_dict==local_date_index_dictionary:
            date_selecting.select_by_index(get_index)
            #time.sleep(0.25)

            advocate_code_wise_btn_element = browser.find_element_by_xpath(advocate_code_wise_btn_locator)
            advocate_code_wise_btn_element.click()
            #time.sleep(0.25)

            cause_list_date_element=browser.find_element_by_xpath(cause_list_date_locator)
            cause_list_date=cause_list_date_element.text

            print("-"*100)
            print("Looking up for cases of Advocate:"+self.advocate_name)
            print("-" * 100)
            print("Cause List Date:"+cause_list_date)
            print("-" * 100)

            advocate_code_text_element=browser.find_element_by_id(advocate_code_text_locator)
            advocate_code_text_element.send_keys(self.advocate_code)
            #time.sleep(0.3)

            submit_btn_element=browser.find_element_by_xpath(submit_btn_locator)
            submit_btn_element.click()
            #time.sleep(0.25)

            t_data_details_elements=browser.find_elements_by_xpath(t_data_details_locator)
            t_data_details_text_attr =[o.text for o in t_data_details_elements]
            case_num_indices = [i for i, x in enumerate(t_data_details_text_attr) if case_num in x]
            print(t_data_details_text_attr)
            print(case_num_indices)
            a = np.array(t_data_details_text_attr)
            case_num_present_detail_text_elements=list(a[case_num_indices])
            print(case_num_present_detail_text_elements)

            b=np.array(t_data_details_elements)
            case_num_present_detail_elements=list(b[case_num_indices])
            print(case_num_present_detail_elements)

            notify_chintu_list = None
            notify_chintu = None

            for index,detail in enumerate(case_num_present_detail_elements):

                if case_num in detail.text:
                    i = index + 1
                    print("i:" +str(i))
                    browser.execute_script("arguments[0].scrollIntoView(true);",detail)
                    #time.sleep(0.35)
                    notification=self.capture_screen_shot(browser,cause_list_date)

                    notify_chintu="Your case '"+case_num+"' is being heard on "+str(cause_list_date)+",argued by lawyer "+self.advocate_name+"."

                    print("-"*100)
                    get_print_head_elements=browser.find_elements_by_xpath(get_print_head_locator.format(case_num,i))
                    for head_element in get_print_head_elements:
                        print(head_element.text)
                    print("-" * 100)
                    get_print_detail_elements=browser.find_elements_by_xpath(get_print_detail_locator.format(case_num,i))
                    for detail_element in get_print_detail_elements:
                        print(detail_element.text)

                    print("-"*100)
                    print(notification)
                    print("XXXXX"+"-"*90+"XXXXX")


            if not case_num_present_detail_elements:
                print("Case No:"+case_num+" is not being heard on "+str(cause_list_date))
            print("-" * 100)

            notify_chintu_list=[notify_chintu,cause_list_date]
            #time.sleep(1)
            browser.close()
            return notify_chintu_list
        else:
            '''raise ProgramFailedError("'DatesMismatchError'")'''

    def capture_screen_shot(self, browser,cause_list_date):
        image_file_name = self.advocate_name+"_Screen_on_"+cause_list_date+".png"
        destination_file = os.path.join(self.ss_folder_path,image_file_name)
        try:
            browser.save_screenshot(destination_file)
            time = datetime.datetime.now()
            image_capture_time = str(time.strftime("%d-%m-%y %I:%M:%S %p"))
            notify_user="Image '"+image_file_name+"' is captured at "+image_capture_time+".\nAnd saved to path:'"+self.ss_folder_path+"'"
            return notify_user
        except:
            notify_exception="Error Occured!Failed to capture Screenshot."
            return notify_exception

class RunThisDate():
    def __init__(self,index_to_be_passed,d_and_i_dictionary_to_be_passed):
        self.pass_index=index_to_be_passed
        self.pass_d_and_i_dictionary=d_and_i_dictionary_to_be_passed
    def run_this_date(self):

        set_path=pass_CauseList_folder_path
        set_name="name_unassigned "
        catch_folder_name_and_path=create_new_result_folder(set_path,set_name)
        result_folder_path=catch_folder_name_and_path[1]

        temp_folder_name=catch_folder_name_and_path[0]

        temp_text_file_name=temp_folder_name+".txt"

        outputting_console_area=sys.stdout

        sys.stdout=open(temp_text_file_name, "w")

        advocates_dictionary=pass_advocates_dictionary

        class_name=[]
        captured_cause_list_date=[]
        intimate_chintu=[]

        for advocate_name,advocate_code in advocates_dictionary.items():
            advocate_name=CauseList(advocate_code,result_folder_path)
            notify_and_causelist_list=advocate_name.find_time_and_location(self.pass_index,self.pass_d_and_i_dictionary)
            intimate_chintu.append(notify_and_causelist_list[0])
            captured_cause_list_date.append(notify_and_causelist_list[1])
            class_name.append(advocate_name.__class__.__name__)

        sys.stdout.close()

        sys.stdout = outputting_console_area

        perm_folder_name=None
        perm_text_file_name=None
        date_being_checked=None

        if((class_name[0]+captured_cause_list_date[0])==(class_name[1]+captured_cause_list_date[1])):
            perm_folder_name=class_name[0]+" "+captured_cause_list_date[0]
            perm_text_file_name=perm_folder_name+".txt"
            date_being_checked=captured_cause_list_date[0]
        else:
            '''raise ProgramFailedError("'DatesMismatchError'")'''

        try:
            os.rename(temp_text_file_name,perm_text_file_name)
        except:
            print("A file with same name already exists. Replacing previous text file.")
            os.remove(perm_text_file_name)
            os.rename(temp_text_file_name,perm_text_file_name)

        shutil.move(perm_text_file_name,result_folder_path)
        corrected_folder_path=set_path+perm_folder_name
        try:
            os.rename(result_folder_path,corrected_folder_path)
        except:
            print("A folder with '"+perm_folder_name+"' already exists. Replacing previous folder.")
            shutil.rmtree(corrected_folder_path)
            os.rename(result_folder_path, corrected_folder_path)

        print(intimate_chintu)
        print("'"+perm_text_file_name+"' is created with the Results.\nAnd saved at the path:'"+corrected_folder_path+"'")
        if any(intimate_chintu):
            if None in intimate_chintu:
                intimate_chintu.append(intimate_chintu.pop(intimate_chintu.index(None)))
                intimate_chintu[intimate_chintu.index(None)] = "Other lawyer is not taking up the case."
            intimate_chintu_string = '\n'.join(map(str, intimate_chintu))
            #print(intimate_chintu_string)
            email_line="Result files are attached.Please check them.\n\nThank You!"
                       #"A zip file with the results is attached.Please check it.\n\nThank You!"
            sms_line = "Result files are sent to your email.Please check them.\n\nThank You!"
                       #"A zip file with the results is sent to your email.Please check it.\n\nThank You!"
            pass_email_subject = "High Court Alert: Your case is being heard on " + date_being_checked
            pass_email_body="Hi Abhilash,\n\n"+intimate_chintu_string+"\n\n"+email_line+"\n"
            pass_sms_text="Hi Abhilash,\n\n"+intimate_chintu_string+"\n\n"+sms_line+"\n"
            #zip_file_path=zip_a_folder(set_path,perm_folder_name,corrected_folder_path)
            try:
                #send_email_with_attachments(pass_email_subject, pass_email_body,zip_file_path)
                send_email_with_multiple_attachments(pass_email_subject,pass_email_body,corrected_folder_path)
            except:
                print("failed to send email!")
            try:
                send_ponni_sms("High Court Alert!!\n\n"+pass_sms_text)
                send_chintu_sms("High Court Alert!!\n\n"+pass_sms_text)
            except:
                print("failed to send sms!")
        if not all(intimate_chintu):
            dont_text_chintu_subject="Your case is not being heard on "+date_being_checked
            #dont_text_chintu="No case hearing!"
            #send_email(dont_text_chintu_subject,dont_text_chintu)
            print(dont_text_chintu_subject)
        program_end_time=datetime.datetime.now()

        text_file = open(os.path.join(corrected_folder_path, perm_text_file_name), "a")
        text_file.write("temporary text file name:"+temp_text_file_name+"\n")
        text_file.write("temporary folder name:"+temp_folder_name+"\n")
        text_file.write("path where files are being saved:"+result_folder_path+"\n")
        text_file.write("class names of "+str(len(class_name))+" objects created:"+str(class_name)+"\n")
        text_file.write("list dates of "+str(len(class_name))+" objects created:"+str(captured_cause_list_date)+"\n")

        i=0
        for advocate_name in advocates_dictionary.keys():
            text_file.write(advocate_name+":[class name:"+class_name[i]+",captured cause list date:"+captured_cause_list_date[i]+"]\n")
        text_file.write("permanent folder name:"+perm_folder_name+"\n")
        text_file.write("permanent text file name:"+perm_text_file_name+"\n")
        text_file.write("path after folder name change:"+corrected_folder_path+"\n")
        text_file.write("-"*75+"\n")
        text_file.write("Report:"+"\n")
        text_file.write("-"*75+"\n")
        text_file.write("program run started at "+str(program_start_time)+"\n")
        text_file.write("program run ended at "+str(program_end_time.strftime("%d-%m-%y %I:%M:%S %p"))+"\n")
        text_file.write("All your result files are located at path '"+corrected_folder_path+"'.")
        text_file.close()

log_file_name="CauseList_failed_traceback.txt"
log = open(log_file_name, "w")
program_start_time = datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")
try:
    obj=GetSearchDatesPage()
    capture_list=obj.get_search_dates_page()
    driver=capture_list[0]
    selected_date_index=capture_list[1]
    d_and_i_dictionary=capture_list[2]
    driver.close()
    print("got the date to select.")

    while selected_date_index>=0:
        obj = RunThisDate(selected_date_index,d_and_i_dictionary)
        obj.run_this_date()
        if selected_date_index==0:
            break
        selected_date_index=selected_date_index-1
    log.close()
    current_directory_path = os.path.dirname(os.path.abspath(__file__))
    get_log_file_path = os.path.join(current_directory_path,log_file_name)
    os.remove(get_log_file_path)

except:
    sys.stdout = sys.__stdout__
    program_failed_time=datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")
    traceback.print_exc(file=log)
    log.close()
    current_directory_path=os.path.dirname(os.path.abspath(__file__))
    get_log_file_path = os.path.join(current_directory_path,log_file_name)
    #print(get_log_file_path)
    print("Program failed!\n'"+os.path.basename(__file__)+"' Program started on "+program_start_time+" has failed at "+program_failed_time+".\nFailed report '"+log_file_name+"' is generated.\nPlease look into it.")
    email_body="Hi Abhilash,\n\n'"+os.path.basename(__file__)+"' Program started on "+program_start_time+" has failed at "+program_failed_time+".\nFailed report '"+log_file_name+"' is attached.\nPlease look into it.\n\nThank You!"
    email_subject="Program failed Alert!!"
    send_email_with_attachments(email_subject,email_body,get_log_file_path)
    sms_text="Program failed Alert!!\n'"+os.path.basename(__file__)+"' Program started on "+program_start_time+" has failed at "+program_failed_time+".\nFailed report '"+log_file_name+"' is sent to your email.\nPlease look into it\nThank You!."
    send_ponni_sms(sms_text)
    #send_chintu_sms(sms_text)

#line 269-zip_file_path
#line 271-send_email_with_attachments
#line 277-send_chintu_sms


