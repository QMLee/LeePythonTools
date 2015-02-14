# -*- coding: gb18030 -*- 
# -*- coding: utf-8 -*-

''' Change files'  extension name in current directory except "*.py" to  para you set'''

import sys
import os
import shutil

dir_global_path = os.getcwd()
print dir_global_path

def rename_files_in_dir(dir_path, ext_name):
       for each_file in os.listdir(dir_path):
               tup=os.path.splitext(each_file)
               if not 'py' in tup[1]:
                      os.rename(each_file,tup[0]+"."+ext_name)
                      print each_file+"----------->"+tup[0]+"."+ext_name
rename_files_in_dir(dir_global_path,"doc")
