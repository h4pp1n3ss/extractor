
import os 
from os import path
import shutil

def log(message, is_warning=False):
    """"
    This function prints a message to the console.
    
    Parameters:
        message (str): The message to print.
        is_warning (bool): If True, the message will be printed as a warning.
        
    Returns:
        None
    """
    if is_warning:
        print("[!] " + message)
    else:
        print("[*] " +  message)

def is_binary_exists(file):
    """"
    This function checks if a binary exists in the system.
    It takes a string as an argument and returns a boolean.
    If the binary exists, it returns True, otherwise False.
    """
    if shutil.which(file) is None:
        return False
    else:
        return True

def file_exists(filepath):
    """""
    This function checks if a file exists.
    
    Parameters
    ----------
    filepath : str
        The path to the file to be checked.
    
    Returns
    -------
    bool
        True if the file exists, False if it does not.
    
    Examples
    --------
    >>> file_exists('/Users/johndoe/Desktop/file.txt')
    True
    
    >>> file_exists('/Users/johndoe/Desktop/file.txt')
    False

    """
    
    exists  = path.exists(filepath)
    if exists:
        return True
    else:
        return False

def is_react(filepath, project_dir):
    """"
    This function checks if the app is built with react-native.
    It checks for the following:
    1. If the index.android.bundle file exists in the decompiled apk
    2. If the com.facebook.react package is found in AndroidManifest.xml
    3. If the com.facebook.react.devsupport.Devsettings.Activity is found in AndroidManifest.xml
    If any of the above conditions are met, it returns True.
    Else, it returns False.
    """
    detected = False
   
    # Method 1: Check if the index.android.bundle file exists in decompile apk 
    if file_exists(project_dir + os.sep + "assets/index.android.bundle"):

            detected = True
            
    if detected == False:
        with open(filepath) as fh:
            content = fh.read()
            # try to detect if the app was built with react-native
            # Method 2 : Check if com.facebook.react is found in AndroidManifest.xml 
            if content.find("com.facebook.react"):
                detected = True

            # Method 3 : Check if com.facebook.react.devsupport.Devsettings.Activity is found in AndroidManifest.xml
            elif content.find("com.facebook.react.devsupport.DevsettingsActivity"):
                detected = True

    if detected == True:
        return True
    else:
        return False

def banner():

    banner = """\n                                                                              
                                                                               
    @@@@@@@@ @@@  @@@ @@@@@@@ @@@@@@@   @@@@@@   @@@@@@@ @@@@@@@  @@@@@@  @@@@@@@  
    @@!      @@!  !@@   @!!   @@!  @@@ @@!  @@@ !@@        @!!   @@!  @@@ @@!  @@@ 
    @!!!:!    !@@!@!    @!!   @!@!!@!  @!@!@!@! !@!        @!!   @!@  !@! @!@!!@!  
    !!:       !: :!!    !!:   !!: :!!  !!:  !!! :!!        !!:   !!:  !!! !!: :!!  
    : :: ::  :::  :::    :     :   : :  :   : :  :: :: :    :     : :. :   :   : : 
                                                                                                                                                                                                                                                                                                                                                                                                                           
    @Author: h4pp1n3ss
    @Date: 13012023
    @version: 0.1
    @Description: react endpoint extractor (no need more description)

    Execute: 
    $> python extractor.py -a APK_FILE
                                                                                                                                                                            
    """
    
    return banner
