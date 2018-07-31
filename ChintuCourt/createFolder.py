import datetime
import os
import shutil

def create_new_result_folder(path_where_folder_has_to_be_created,folder_to_be_named):
    now=datetime.datetime.now()
    newly_created_folder_path=None
    new_folder_name=None
    try:
        folder_path = path_where_folder_has_to_be_created
        new_folder_name = folder_to_be_named+" "+str(now.strftime("%d-%m-%y"))
        newly_created_folder_path = folder_path + new_folder_name
        os.mkdir(newly_created_folder_path)
        folder_name=new_folder_name
        folder_path_where_currentRun_files_have_to_be_saved = newly_created_folder_path
        throw_folder_name_and_path=[folder_name,folder_path_where_currentRun_files_have_to_be_saved]
        return throw_folder_name_and_path
    except FileExistsError:
        print("A folder with name '"+new_folder_name+"' already exists with result files.\n Replacing the old folder with new results.")
        shutil.rmtree(newly_created_folder_path)
        os.mkdir(newly_created_folder_path)
        folder_name = new_folder_name
        folder_path_where_currentRun_files_have_to_be_saved = newly_created_folder_path
        throw_folder_name_and_path = [folder_name, folder_path_where_currentRun_files_have_to_be_saved]
        return throw_folder_name_and_path
