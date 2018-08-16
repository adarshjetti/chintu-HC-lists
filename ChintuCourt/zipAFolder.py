import shutil
import os

def zip_a_folder(get_parent_folder_path,get_name_of_folder_to_be_zipped,get_folder_to_be_zipped_path):
    parent_folder_path=get_parent_folder_path
    name_of_folder_to_be_zipped=get_name_of_folder_to_be_zipped
    newly_created_zip_file=name_of_folder_to_be_zipped
    folder_to_be_zipped_path=get_folder_to_be_zipped_path
    newly_created_zip_file_path=parent_folder_path+newly_created_zip_file
    try:
        shutil.make_archive(newly_created_zip_file_path,'zip',folder_to_be_zipped_path)
        print("'"+newly_created_zip_file_path+".zip' is the path of newly created zip file.")

    except:
        print("A file with same name already exists.Replacing previous zip file.")
        os.remove(newly_created_zip_file_path+".zip")
        shutil.make_archive(newly_created_zip_file_path, 'zip', folder_to_be_zipped_path)
    return newly_created_zip_file_path+".zip"


