# -*- coding: gb18030 -*- 
# -*- coding: utf-8 -*-

'''���ҵ�ǰĿ¼����Ŀ¼�а����ַ����������ļ������ڱ�Ŀ¼����Lee_Files�ļ��У����鵽���ļ�copy������ļ������ļ���������к����� '''
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
#�½���Lee_files�ļ����ñ���	
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