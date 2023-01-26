
import subprocess
from react_extractor.utils import  log
from react_extractor.exceptions import ExecutionFailedException
import os, re
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
    with open(file) as f:
        # TODO: regex need work
           urls = f.read()
           links_v1 = re.findall("\/v1\/[a-z]+-[a-z]+\/.*", urls)
           links_v2 = re.findall("\/v2\/[a-z]+-[a-z]+\/.*", urls)
        #   links_v3 = re.findall("\/[a-z]+\/[a-z]+-[a-z]+\/.*", urls)

    sleep(2)
    for url in links_v1:
        print(url)
    sleep(2)
    
    for url in links_v2:
        print(url)

    
