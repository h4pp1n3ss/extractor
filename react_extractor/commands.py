
import subprocess
from react_extractor.utils import  log
from react_extractor.exceptions import ExecutionFailedException
import os, re, sys
from time import sleep
import jsbeautifier as jb


def apk_decompile(filename):
    """"
    Decompiles an APK file using apktool.
    Args:
        filename: The name of the APK file to decompile.
    Raises:
        ExecutionFailedException: If apktool fails to execute.

    """
    command = "apktool d {} -o {}".format(filename, filename.replace(".apk", "_out"))
    output = subprocess.getoutput(command)
    if 'Exception in' in output:
        raise ExecutionFailedException('''\
            Failed to execute apktool using the following command \
            {cmd}
        '''.format(cmd=command))


def extract_android_bundle(file, out_path="./index.bundle.out"):
    """"
    Extract Android bundle file from an android app.
    Args:
        file (str): The path to the file to extract the bundle from.
        out_path (str): The path to write the extracted bundle to.
    Returns:
        bool: True if the extraction was successful, False otherwise.
    """
    try: 
        js = jb.beautify_file(file)
        with open(out_path, "at") as f:
            f.write(js)
        return True
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

def extract_endpoints(file):
    """"
    This function takes a file as input and extracts all the endpoints from it.
    It then prints them out.
    
    Parameters
    ----------
    file : str
        The name of the file to be read.
    
    Returns
    -------
    None
    
    Examples
    --------
    >>> extract_endpoints('endpoints.txt')
    /v1/accounts/{account_id}/transactions
    /v1/accounts/{account_id}/transactions/{transaction_id}
    /v1/accounts/{account_id}/transactions/{transaction_id}/tags
    """

    # regex from  https://github.com/GerbenJavado/LinkFinder/blob/master/linkfinder.py 
    regex_str = r"""
        (?:"|')                               # Start newline delimiter
        (
            ((?:[a-zA-Z]{1,10}://|//)           # Match a scheme [a-Z]*1-10 or //
            [^"'/]{1,}\.                        # Match a domainname (any character + dot)
            [a-zA-Z]{2,}[^"']{0,})              # The domainextension and/or path
            |
            ((?:/|\.\./|\./)                    # Start with /,../,./
            [^"'><,;| *()(%%$^/\\\[\]]          # Next character can't be...
            [^"'><,;|()]{1,})                   # Rest of the characters can't be
            |
            ([a-zA-Z0-9_\-/]{1,}/               # Relative endpoint with /
            [a-zA-Z0-9_\-/]{1,}                 # Resource name
            \.(?:[a-zA-Z]{1,4}|action)          # Rest + extension (length 1-4 or action)
            (?:[\?|#][^"|']{0,}|))              # ? or # mark with parameters
            |
            ([a-zA-Z0-9_\-/]{1,}/               # REST API (no extension) with /
            [a-zA-Z0-9_\-/]{3,}                 # Proper REST endpoints usually have 3+ chars
            (?:[\?|#][^"|']{0,}|))              # ? or # mark with parameters
            |
            ([a-zA-Z0-9_\-]{1,}                 # filename
            \.(?:json|js|xml)                   # . + extension
            (?:[\?|#][^"|']{0,}|))              # ? or # mark with parameters
            |
            \/[a-z]+\/[a-z]+-[a-z]+\/.*
            |
            \/v1\/[a-z]+-[a-z]+\/.*
            |
            \/v2\/[a-z]+-[a-z]+\/.*
        )
        (?:"|')                               # End newline delimiter
    """
    with open(file) as f:
           urls = f.read()
           regex = re.compile(regex_str, re.VERBOSE )
           links = re.findall(regex, urls)

    sleep(2)
    for url in links:
        print(url[0])

    

  
    
