import os

PROJECT_DIR = 'C:\\Users\\siron\\Desktop\\python_git'
SETTINGS_FILE = 'settings.ini'

print(os.path.join(PROJECT_DIR,SETTINGS_FILE))
print(os.path.join(PROJECT_DIR,'settings_dir',SETTINGS_FILE))