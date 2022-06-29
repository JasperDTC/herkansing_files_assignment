__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


#Onderdeel 1.
#Uitwerking van medestudent Sander de Jong.
#https://www.codegrepper.com/code-examples/python/make+directory+python
import os.path

path_cache = os.getcwd()+'\\files'
def clean_cache():
    path = path_cache
    if os.path.isdir('files\cache'):
        for file in os.scandir(path+'\cache'):
            os.remove(file.path)
        print('aanwezig')
    else:
        print('niet aanwezig')
        os.mkdir('files\cache')
  
#Onderdeel 2.
#Gevonden op https://appdividend.com/2022/01/19/python-unzip/#:~:text=To%20unzip%20a%20file%20in,inbuilt%20python%20module%20called%20zipfile.
#tweede source: https://docs.python.org/3/library/zipfile.html
from zipfile import ZipFile
def cache_zip(file_name, cache_dir):
    file_name = os.getcwd()+'\\files\\data.zip'
    cache_dir = os.getcwd()+'\\files\\cache'
    with ZipFile(file_name, 'r') as zip:
        zip.extractall(cache_dir)

#Onderdeel 3.
#Op basis van de uitwerking van medestudent Stefan.

import os
def cached_files():
    dir_path = os.getcwd()+'\\files\\cache'
    list_of_files = []
    for i in os.listdir(dir_path):
        list_of_files.append(os.path.join(dir_path, i))
    return list_of_files

#Voorbeeld gevonden op: https://pynative.com/python-list-files-in-a-directory/
#De onderstaande uitwerking heb ik zelf gemaakt op basis van de uitleg op de bovenstaande webpagina. Kunnen jullie mij uitleggen waarom mijn uitwerking niet werkt?
"""
import os
def cached_files():
    dir_path = r'C:\\Users\\Jasper\\Desktop\Winc\\files\\cache'
    list_of_files = []
    for file in os.listdir(dir_path):
        if os.file.isfile(os.path.join(dir_path, file)):
            list_of_files.append(file)
    return list_of_files
    """

#Onderdeel 4.
#Voorbeeld gevonden op: https://pynative.com/python-search-for-a-string-in-text-files/
import os
def find_password(list_of_files):
    for file_name in list_of_files:
        with open(file_name, 'r') as f:
            contents = f.readlines()
            for line in contents:
                if 'password' in line:
                   return line.strip()[10:]






