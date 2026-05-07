#!/usr/bin/env python
import logging
import sys
import os
from react_extractor.utils import is_react
from react_extractor.utils import file_exists
from react_extractor.commands import extract_endpoints
from react_extractor.commands import extract_android_bundle
from react_extractor.commands import apk_decompile
from react_extractor.utils import check_tools

logger = logging.getLogger(__name__)

def extractor(apk):

    if not check_tools():
        logger.warning("Required tools are missing. Please install apktool and try again.")
        sys.exit(1)

    # Decompile the app
    logger.info("Extractor is running.  Please wait ...")
    apk_decompile(apk)
    project_dir = apk.replace('.apk', '_out')

    # Check manifest
    manifest_filepath = project_dir + os.sep + "AndroidManifest.xml"

    # Check if the app is React
    if is_react(manifest_filepath, project_dir):
        # point to index.bundle file
        in_index_bundle = project_dir + os.sep + "assets/index.android.bundle"
        out_index_bundle = project_dir + os.sep + "/index.js"
        if file_exists(out_index_bundle):
            logger.info("Trying to extract all endpoints")
            extract_endpoints(out_index_bundle)
        elif file_exists(in_index_bundle):
            logger.info("Trying to extract all endpoints")
            out = extract_android_bundle(in_index_bundle, out_index_bundle)
            logger.info("Extracting file, please wait")
            extract_endpoints(out_index_bundle)
        else:
            logger.error("Something failed")
    else:
        logger.warning("No react native app were detected")
        sys.exit(-1)
    
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s",
    )
    apk = sys.argv[1]
    extractor(apk)