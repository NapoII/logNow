"""EzLog" is a Python package created to simplify logging for developers working on Python applications. The package provides a simple logging function that allows developers to output log messages to a file with timestamps, instead of using the standard "print" statement.

With "EzLog", developers can easily create custom log messages and output them to a log file, allowing them to monitor the behavior of their applications and quickly identify any errors or issues that arise. The package provides several useful features, including support for multiple log levels, the ability to configure log formatting, and the option to output logs to the console in addition to the log file.

In addition to its core functionality, "EzLog" is designed to be easy to use and configure. The package is well-documented, and the code is written in a modular and extensible manner, making it easy for developers to customize and extend its functionality to suit their needs."""


import os
import sys

from functions import *


#Pre var
filename = os.path.basename(sys.argv[0])
file_path = os.path.dirname(sys.argv[0])
folder_path_EZLog = os.path.abspath(os.path.dirname(__file__)) + os.path.sep
Log_File = f"Log_{File_name_with_time(filename)}"

## If in the .ini log_folder_dir = default then log folder = file folder:
config_dir = folder_path_EZLog + "config.ini"
log_folder_dir = read_config(config_dir, "folder", "log_folder_dir")
if str(log_folder_dir) == "default":
    log_folder_dir = file_path
log_folder_dir = Folder_gen("log", log_folder_dir)

print(f"log_folder_dir: {log_folder_dir}")
Log_filename = f"Log_{File_name_with_time(filename)}"

ascii = Read_File_Out(folder_path_EZLog + "Log_top_img.ascii")
print(ascii)
lines = ascii.split('\n')
len_a = 0
while True:
    if len(lines) == 0:
        break
    
    len_b = len(lines.pop())
    if len_b > len_a:
        ascii_max_width_minus = len_b
ascii_max_width_minus = ascii_max_width_minus*"-"
Log_File = Create_TextFile(Log_filename, log_folder_dir, ascii)
Log_into_text = f"{ascii_max_width_minus}\n{filename} was executed at {TimeStemp()}"

Fill_Datei(Log_File,Log_into_text , "a")


### var log data
os_name = get_os_name()


def test():

    folder_path_EZLog = os.path.abspath(
        os.path.dirname(__file__)) + os.path.sep
    print(folder_path_EZLog)
    config_dir = folder_path_EZLog + "config.ini"
    print(config_dir)
    x = Read_File_Out(folder_path_EZLog + "Log_top_img.ascii")
    print(x)
    print(TimeStemp())

    # Der Name der auszuführenden Datei wird in der Variable "filename" gespeichert.
    filename = os.path.basename(sys.argv[0])
    print("Der Name der auszuführenden Datei lautet: ", filename)

def log(Log_input):
    """Schreibt einen Eintrag in das Log-File und gibt ihn auf der Konsole aus.

    Args:
        Log_input (str): Der Eintrag, der im Log-File und auf der Konsole ausgegeben werden soll.

    """
    Fill_Datei(Log_File, TimeStemp()+" --> " + Log_input+"\n", "a")
    print(TimeStemp()+" --> " + Log_input+"\n")
