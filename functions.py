"""EzLog" is a Python package created to simplify logging for developers working on Python applications. The package provides a simple logging function that allows developers to output log messages to a file with timestamps, instead of using the standard "print" statement.

With "EzLog", developers can easily create custom log messages and output them to a log file, allowing them to monitor the behavior of their applications and quickly identify any errors or issues that arise. The package provides several useful features, including support for multiple log levels, the ability to configure log formatting, and the option to output logs to the console in addition to the log file.

In addition to its core functionality, "EzLog" is designed to be easy to use and configure. The package is well-documented, and the code is written in a modular and extensible manner, making it easy for developers to customize and extend its functionality to suit their needs."""

import os
from configparser import ConfigParser
import time

folder_path_EZLog = os.path.abspath(os.path.dirname(__file__))+ os.path.sep 
config_dir = folder_path_EZLog + "config.ini"

import os

def get_os_name():
    """
    This function determines the name of the operating system running on a computer.

    Returns:
    - If the operating system is Unix-based, the function returns the string "Unix-based".
    - If the operating system is Windows, the function returns the string "Windows".
    - If the operating system is Java Virtual Machine, the function returns the string "Java Virtual Machine".
    - If the operating system is OS/2, the function returns the string "OS/2".
    - If the operating system is not recognized, the function returns the string "Operating system not recognized".

    Example Usage:
    ```
    print(get_os_name())
    ```
    """
    # Determine the operating system
    if os.name == 'posix':
        return('Unix-based')
    elif os.name == 'nt':
        return('Windows')
    elif os.name == 'java':
        return('Java Virtual Machine')
    elif os.name == 'os2':
        return('OS/2')
    else:
        return('Operating system not recognized')

    

def read_config(config_dir, section, option):
    """Reads a specific option from a config file in a specific section

    Args:
        config_dir (str): The path of the config file.
        section (str): The section where the searched option is located.
        option (str): The name of the searched option.

    Returns:
        str: The value of the searched option.

    """

    config = ConfigParser()
    config.read(config_dir)
    load_config = (config[section][option])

    print("Config geladen: [ "+(option) +" = "+ (load_config)+" ]")

    return load_config


def write_config(config_dir, section, Key, option):

    """Writes a specific option to a config file in a specific section.

    Args:
        config_dir (str): The path of the config file. section
        (str): The section where the option is to be written. key
        (str): The name of the option. option
        (str): The value to be written for the option..

    """

    config = ConfigParser()
    # update existing value
    config.read(config_dir)
    try:
        config.add_section(section)
    except:
        pass
    config.set(section, Key,option) #Updating existing entry 
    with open(config_dir, 'w') as configfile:
        config.write(configfile)
    print ("\nSetting change -> "+str(config_dir)+"\n"+"["+str(section)+"]\n"+str(Key)+" = " + str(option)+"\n")


def Folder_gen(Folder_Name, Folder_dir ):
   """
   This function checks if a specified folder already exists in the specified directory. If it does not exist,
    it creates the folder.

    Args:
    - Folder_Name (str): The name of the folder to be checked/created.
    - Folder_dir (str): The directory path where the folder should be located.

    Returns:
    - (str): The full path of the checked/created folder
    """
   print("Folder structure is checked and created if necessary...\n")
   folder = Folder_Name
   #dir = "~/"+str(Folder_dir)+"/"+str(folder)           # Specifies desired file path
   
   dir = Folder_dir + os.path.sep + folder
   full_path = os.path.expanduser(dir)                 # Adds file path with PC user name
   full_path = os.path.normpath(full_path)
   if os.path.exists(full_path):                       # Checks file path for exsistance Ture/False
      print("Folder structure already exists")
      print("  ->   " + str(full_path))
   else:                                               # Creates folder if not available
      os.makedirs(full_path)
      print("The folder ["+folder+"] was created in the directory:" )
      print("  ->   " + str(full_path))
   print("\n")
   return(full_path)


def Read_File_Out(dir):
    """his function reads the contents of a specified file and returns the output.

    Args:
    - dir (str): The directory path of the file to be read.

    Returns:
    - (str): The contents of the file"""
    # Open the file and read its contents
    with open(dir, 'r') as f:
        output = f.read()

    # Output the contents of the file
    return(output)

def Fill_Datei(dir, toFill, Attribut):
    """
    This function writes specified data to a file at a specified directory.

    Args:
    - dir (str): The directory path of the file to be written to.
    - toFill (str): The string to be written to the file.
    - Attribut (str): The attribute to open the file with, such as "w" for write or "a" for append.

    Returns:
    - None
    """
    file1 = open(dir, Attribut,encoding="utf-8")                                 # File is opened
    #print("File ["+str(dir) + "] is written and saved...\n")
    file1.write(toFill)                                             # File is filled with input
    file1.close()


def Create_TextFile( Text_File_name, save_path, Contents ):
    """Ercreates a new text file if it does not already exist and fills it with the specified contents Contents.

    Args:
        Text_File_name (str): The name of the text file.
        save_path (str): The path where the text file is to be saved.
        Inhalt (str): The content to be written to the text file.

    Returns:
        str: The full path of the created text file.
    """
    complete_Path_Text = os.path.join(save_path+ os.path.sep+ Text_File_name+".txt")   
    if os.path.exists(complete_Path_Text):
        return complete_Path_Text
    else:
        print("\nTextdatei ["+str(complete_Path_Text)+"] wird erstellt...")
        file1 = open(complete_Path_Text, "w")                                   # Create file
        #toFile = input("Write what you want into the field")                   # File input def.
        file1.write(Contents)                                                     # File is filled with input
        file1.close()
        
        return complete_Path_Text
    

def TimeStemp():
    """Generates a timestamp in the specified format.

    Returns:
        str: The generated timestamp.
    """
    time_format = read_config(config_dir, "log_file", "time_format")
    if time_format == "default":
        time_format = "%d-%m-%Y_%H:%M:%S"
    TimeStemp = Date_Time=(time.strftime(time_format))
    return TimeStemp


def time_stemp_to_file_str(str):
    """
    Converts a timestamp string in the format "yyyy-mm-dd_HH:MM:SS" to a file name string 
    in the format "(SS.MM.HH)_dd-mm-yyyy". 

    Args:
    str (str): A timestamp string in the format "yyyy-mm-dd_HH:MM:SS".

    Returns:
    str: A file name string in the format "(SS.MM.HH)_dd-mm-yyyy".
    """
    str_list = str.split("_")
    str_list.reverse()
    full_str = ""

    while True:
        str_list_len = len(str_list)
        if str_list_len == 0:
            break

        item = str_list.pop()
        if ":" in item:
            item = item.replace(":", ".")
            item = f"({item})"


        full_str += f"{item}_"
    full_str = full_str[:-1]
    
    return full_str


def File_name_with_time(FileName):
    """Generates a file name by combining the name passed with the current date and time.

    Args:
        FileName (str): The name of the file to be used.
    Returns:
        str: The generated file name.
    """
    Date = TimeStemp()        # Generiert date formater
    FullName = f"{time_stemp_to_file_str(Date)}_{FileName}"                        # Generiert Datei name

    return FullName


