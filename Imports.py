py_name = "EZLog"
v = "0.0.1"
f0I = """
              .#:                                 
             .#MM:                                
            .#MMMM:                ,+%%+          
            %MMMMMM:            .+@MMMMM.         
           +MMMMMMMM:          ,@MMMMMM:          
          ,MMMMMMMMMM:        ,MMMMMMM:           
          %MMMMMMMMMMM:      .@MMMMMM:            
         :@MMMMMMMMMMM@      #MMMMMM:             
        %MMMMMMMMMMMM@.     ,MMMMMM:              
       %MMMMMMMMMMMM@.      #MMMMM#               
      :MMMMMMMMMMMM@.      .MMMMMMM.          ,+  
      #MMMMMMMMMMM#.       ,MMMMMMM:         :MM. 
     :MMMMMMMMMM#:         ,MMMMMMM%        :MMM. 
    .MMMMMMMMMM@.          ,MMMMMMM@       :MMMM. 
    #MMMMMMMMMMM@.         ,MMMMMMMM:.    :MMMM@  
   ,MMMMMMMMMMMMM@.        .MMMMMMMMMM@%::MMMMM%  
   %MMMMMMMMMMMMMM@.        #MMMMMMMMMMMMMMMMMM,  
  .MMMMMM@+,MMMMMMM@.      :MMMMMMMMMMMMMMMMMM#   
  ,MMMMM%.  ,MMMMMMM@.    +MMMMMMMMMMMMMMMMMM@.   
  +MMMM+     ,MMMMMMM@.  +MMMMMMMMMMMMMMMMMMM,    
  %MMM%       ,MMMMMMM@.+MMMMMMMMMMMMMMMMMM@,     
  %MMM.        ,MMMMMMMMMMMMMMMMMMMMMMMMMM%.      
  %MM+          ,MMMMMMMMMMMMMMMM+:%###%:.        
  +MM,           ,MMMMMMMMMMMMMM+                 
  ,MM             ,MMMMMMMMMMMM+                  
   @#             .#MMMMMMMMMM#                   
   ..            .#MMMMMMMMMMMM+                  
                .#MMMMMMMMMMMMMM+                 
               .#MMMMMMMMMMMMMMMM+                
              .#MMMMMMMMMMMMMMMMMM+               
             .@MMMMMMMMMMMMMMMMMMMM+              
            .@MMMMMMMMMMMMMMMMMMMMMM+             
           .@MMMMMMMMMM@%MMMMMMMMMMMM+            
          ,@MMMMMMMMMM@. %MMMMMMMMMMMM+           
         ,@MMMMMMMMMM@.   %MMMMMMMMMMMM+          
        ,@MMMMMMMMMM@,     %MMMMMMMMMMMM+         
       ,MMMMMMMMMMM@,       %MMMMMMMMMMMM+        
      ,MMMMMMMMMMMM,         %MMMMMMMMMMMM+       
     :MMMMMMMMMMMM,           %MMMMMMMMMMMM+      
    :MMMMMMMMMMMM:             %MMMMMMMMMMMM+     
   :MMMMMMMMMMMM:               %MMMMMMMMMMMM+    
  ,MMMMMMMMMMMM:                 %MMMMMMMMMMMM+   
  @MM#+@MMMMMM+                   %MMMMMMMMMMMM:  
 ,MM%  .MMMMM+                     %MMMMMMMMMMMM. 
 :MM+   @MMM+                       %MMMMMMMMMMM: 
 :MM#. ,MMM%                         %MMMMMMMMMM: 
 .MMM@#MMM%                           %MMMMMMMMM, 
  +MMMMMM%                             %MMMMMMM@. 
   :@MM@:                               %MMMMMM,  
     ,.                                  :#M@%,
   


- Imports
- created by Napo_II
- """ + v + """
- python 3.10.7
- https://github.com/NapoII/

"""
####################################################################################################
#import

import os
import os, sys
import time
import pyautogui
from configparser import ConfigParser
import urllib

####################################################################################################
#def

def Folder_gen(Folder_Name, Folder_dir ):
   print("Ordner Struktur wird überprüft und ggf. angelegt...\n")
   folder = Folder_Name
   dir = "~/"+str(Folder_dir)+"/"+str(folder)           # gibt gewünschten Datei-Pfad an
   full_path = os.path.expanduser(dir)                 # ergänzt datei pfad mit PC User name
   if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
      print("Ordner Struktur existiert bereits")
      print("  ->   " + str(full_path))
   else:                                               # Erstellt Ordner falls nicht vorhadnen
      os.makedirs(full_path)
      print("Der Ordner ["+folder+"] wurde erstellt im Verzeichnis:" )
      print("  ->   " + str(full_path))
   print("\n")
   return(full_path)

def Datei_name_mit_Zeit(FileName):

    """Generiert einen Dateinamen, indem er den übergebenen Namen mit dem aktuellen Datum und der Uhrzeit verbindet.

    Args:
        FileName (str): Der Name der Datei, der verwendet werden soll.
    Returns:
        str: Der generierte Dateiname.

    """
    Date = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generiert date formater
    FullName = (FileName+"-"+(Date))                           # Generiert Datei name
    return FullName

def Erstelle_TextDatei( Text_File_name, save_path, Inhalt ):

    """Erstellt eine neue Textdatei, falls sie noch nicht vorhanden ist, und füllt sie mit dem angegebenen Inhalt.

    Args:
        Text_File_name (str): Der Name der Textdatei.
        save_path (str): Der Pfad, in dem die Textdatei gespeichert werden soll.
        Inhalt (str): Der Inhalt, der in die Textdatei geschrieben werden soll.

    Returns:
        str: Der vollständige Pfad der erstellten Textdatei.

    """

    complete_Path_Text = os.path.join(save_path+"\\"+Text_File_name+".txt")     # Path + text datei name
    if os.path.exists(complete_Path_Text):
        return complete_Path_Text
    else:
        print("\nTextdatei ["+str(Text_File_name)+".txt] wird erstellt...")
        file1 = open(complete_Path_Text, "w")                                         # Datei erstellen
        #toFile = input("Write what you want into the field")                   # Datei input def.
        file1.write(Inhalt)                                                    # Datei wird gefüllt mit input
        file1.close()
        return complete_Path_Text

def Lese_Datei_aus(dir):
    # Öffne die Datei und lese ihren Inhalt
    with open('data.txt', 'r') as f:
        inhalt = f.read()

    # Gib den Inhalt der Datei aus
    return(inhalt)

def Fill_Datei(dir, toFill, Attribut):

    """Öffnet eine Datei und füllt sie mit dem angegebenen Inhalt.

    Args:
        dir (str): Der Pfad der zu öffnenden Datei.
        toFill (str): Der Inhalt, der in die Datei geschrieben werden soll.
        Attribut (str): Das Öffnungsattribut für die Datei (z.B. "w" für Schreiben, "r" für Lesen).

    """

    file1 = open(dir, Attribut,encoding="utf-8")                                 # Datei wird geöffnet
    #print("Datei ["+str(dir) + "] wird beschrieben und gespeichtert...\n")
    file1.write(toFill)                                             # Datei wird gefüllt mit input
    file1.close()

def TimeStemp():

    """Generiert einen Zeitstempel im angegebenen Format.

    Returns:
        str: Der generierte Zeitstempel.

    """

    TimeStemp = Date_Time=(time.strftime("%d_%m-%Y_%H:%M:%S"))
    return TimeStemp

def log(Log_input):
    """Schreibt einen Eintrag in das Log-File und gibt ihn auf der Konsole aus.

    Args:
        Log_input (str): Der Eintrag, der im Log-File und auf der Konsole ausgegeben werden soll.

    """
    Fill_Datei(Log_File, TimeStemp()+" --> " + Log_input+"\n", "a")
    print (TimeStemp()+" --> " + Log_input+"\n")

def Zeit_pause(seconds):

    """Führt eine Zeitpause für die angegebene Anzahl an Sekunden aus.

    Args:
        seconds (int): Die Anzahl an Sekunden, die gewartet werden soll.

    """
    
    start_time = time.time()
    while True:                             # Zeit schelife startet
        current_time = time.time()
        elapsed_time = current_time - start_time        # berechung rest Zeit
        if elapsed_time > seconds:
            break

def read_config(config_dir, section, option):

    """Liest eine bestimmte Option aus einer Config-Datei in einem bestimmten Abschnitt.

    Args:
        config_dir (str): Der Pfad der Config-Datei.
        section (str): Der Abschnitt, in dem sich die gesuchte Option befindet.
        option (str): Der Name der gesuchten Option.

    Returns:
        str: Der Wert der gesuchten Option.

    """

    config = ConfigParser()
    config.read(config_dir)
    load_config = (config[section][option])

    print("Config geladen: [ "+(option) +" = "+ (load_config)+" ]")

    return load_config

def write_config(config_dir, section, Key, option):

    """Schreibt eine bestimmte Option in eine Config-Datei in einem bestimmten Abschnitt.

    Args:
        config_dir (str): Der Pfad der Config-Datei.
        section (str): Der Abschnitt, in dem die Option geschrieben werden soll.
        Key (str): Der Name der Option.
        option (str): Der Wert, der für die Option geschrieben werden soll.

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
    print ("\nEinstellungs änderung -> "+str(config_dir)+"\n"+"["+str(section)+"]\n"+str(Key)+" = " + str(option)+"\n")

def Download_from_link(link, dir):
    """Lädt eine Datei von einem gegebenen Link und speichert sie an einem bestimmten Ort.

    Args:
        link (str): Der Link, von dem die Datei heruntergeladen werden soll.
        dir (str): Der Pfad, an dem die Datei gespeichert werden soll.

    Returns:
        str: Der vollständige Pfad der gespeicherten Datei.

    """
    #link = "https://i.imgur.com/Mk1KPNa.png"
    dir = "E://Pr0grame//My_ Pyhton//work_in_progress//Discord-Ticket-Bot//Bilder//Test.png"
    urllib.request.urlretrieve(link, dir)
    log ("Img download [" +link + "] und gespeichert in [ "+dir+ " ]")
    return dir

def parse_int_tuple(input):

    """Parsed eine Eingabe in der Form "(a, b, c, ...)" in ein Tupel aus ganzen Zahlen.

    Args:
        input (str): Die Eingabe, die geparst werden soll.

    Returns:
        tuple: Ein Tupel aus ganzen Zahlen.

    """

    return tuple(int(k.strip()) for k in input[1:-1].split(','))

def parse_tuple(input):

    """Parsed eine Eingabe in der Form "(a, b, c, ...)" in ein Tupel.

    Args:
        input (str): Die Eingabe, die geparst werden soll.

    Returns:
        tuple: Das geparste Tupel.

    """

    return tuple(k.strip() for k in input[1:-1].split(','))

def str_to_bool(input):
    """Konvertiert einen String in einen booleschen Wert.

    Args:
        input (str): Der String, der konvertiert werden soll.

    Returns:
        bool: Der boolesche Wert, der durch die Konvertierung des Strings entstanden ist.
    """
    if input.lower() == "true":
        input = True
    else:
        input = False
    return input

################################################################################################################################
#PreSet Programm

file_path = os.path.dirname(sys.argv[0])
file_path_Bilder = file_path + "/Bilder/"
file_path_Work_Folder = file_path + "/Work_Folder/"
config_dir = file_path +"/config.ini"


Doku_Folder = Folder_gen (py_name, "Documents/")
Log_Folder = Folder_gen ("Log", ("Documents/"+str(py_name)))
Log_File_name = Datei_name_mit_Zeit ("LogFile-"+str(py_name))
Log_File = Erstelle_TextDatei (Log_File_name, Log_Folder, f0I + "Log-File:\n---------------------------------------------------------------------------------------\n")

Bot_Path = os.path.dirname(sys.argv[0])
log ( "Bot_Path: ["+str(Bot_Path) + "]\n")


################################################################################################################################
log ("Imports geladen : [" +str(file_path) + "/Imports.py]")
################################################################################################################################
#def spez.
