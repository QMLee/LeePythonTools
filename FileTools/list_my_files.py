# -*- coding: gb18030 -*- 
# -*- coding: utf-8 -*-

'''查找当前目录和子目录中包含字符串的所有文件，并在本目录建立Lee_Files文件夹，将查到的文件copy到这个文件，以文件名后加序列号添加 '''
'''Attention: Linux System://         Windows System:\\'''
import sys
import os
import shutil

dir_global_path = os.getcwd()
count_num = 0
print dir_global_path

if not os.path.exists(dir_global_path+"\\Lee_Files"):
        os.mkdir("Lee_Files")
        
def print_files_in_dir(dir_path, str_para):
        global dir_global_path
        global count_num
#新建的Lee_files文件不用遍历	
	if dir_path == (dir_global_path+"\\Lee_Files"):
		return
        if os.path.isdir(dir_path):
                for each_file in os.listdir(dir_path):
                                print_files_in_dir(os.path.join(dir_path,each_file),str_para)
        else:
                
                if str_para in dir_path:
                        count_num += 1
			file_name_with_ext=os.path.split(dir_path)[1]
			file_name_without_ext=os.path.splitext(file_name_with_ext)[0]
                        new_file = dir_global_path+"\\Lee_Files\\"+file_name_without_ext+str(count_num)+".doc"
                        print new_file
                        shutil.copyfile(dir_path,new_file)
                else:
                        print dir_path
                        
print_files_in_dir(dir_global_path, "lee")
