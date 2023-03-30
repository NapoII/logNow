"""EzLog" is a Python package created to simplify logging for developers working on Python applications. The package provides a simple logging function that allows developers to output log messages to a file with timestamps, instead of using the standard "print" statement.

With "EzLog", developers can easily create custom log messages and output them to a log file, allowing them to monitor the behavior of their applications and quickly identify any errors or issues that arise. The package provides several useful features, including support for multiple log levels, the ability to configure log formatting, and the option to output logs to the console in addition to the log file.

In addition to its core functionality, "EzLog" is designed to be easy to use and configure. The package is well-documented, and the code is written in a modular and extensible manner, making it easy for developers to customize and extend its functionality to suit their needs."""


from functions import *
import sys
import os

def test():

    folder_path_EZLog = os.path.abspath(os.path.dirname(__file__))+ os.path.sep 
    print(folder_path_EZLog)
    config_dir = folder_path_EZLog + "config.ini"
    print(config_dir)
    x = Read_File_Out(folder_path_EZLog + "Log_top_img.ascii")
    print(x)
    print(TimeStemp())


    # Der Name der auszuführenden Datei wird in der Variable "filename" gespeichert.
    filename = os.path.basename(sys.argv[0])
    print("Der Name der auszuführenden Datei lautet: ", filename)


def EZLog_Start():
    """Starts the EZLog module by creating a log folder and log file with a time-stamped name.

    Returns:
    str: The path of the created log file."""

    filename = os.path.basename(sys.argv[0])
    file_path = os.path.dirname(sys.argv[0])
    os_name = get_os_name()
    folder_path_EZLog = os.path.abspath(os.path.dirname(__file__))+ os.path.sep 
    
    
    # If in the .ini log_folder_dir = default then log folder = file folder:

    config_dir = folder_path_EZLog +"config.ini"
    log_folder_dir = read_config(config_dir, "folder", "log_folder_dir")

    if str(log_folder_dir) == "default":
        log_folder_dir = file_path
        
    log_folder_dir = Folder_gen("log", log_folder_dir )

    # create Log file:

    Log_filename = f"Log_{File_name_with_time(filename)}"
    
    ascii = Read_File_Out(folder_path_EZLog + "Log_top_img.ascii")
    Create_TextFile( Log_filename, log_folder_dir, ascii )
    
# EZLog_Start()

