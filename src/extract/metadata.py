#!/usr/bin/env python3
"""
Function for extracting the metadata for MED-PC output data files. 
Metadata includes: "File", "Start Date", "End Date", "Subject", "Experiment", "Group", "Box", "Start Time", "End Time", "MSN"

For more information on the MED-PC's programming language, Trans: 
- https://www.med-associates.com/wp-content/uploads/2017/01/DOC-003-R3.4-SOF-735-MED-PC-IV-PROGRAMMER%E2%80%99S-MANUAL.pdf
"""
from collections import defaultdict

def get_med_pc_meta_data(file_path, meta_data_headers=None, file_path_to_meta_data=None):
    """
    """
    # The default metadata found in MED-PC files
    if meta_data_headers is None:
        meta_data_headers = ["File", "Start Date", "End Date", "Subject", "Experiment", "Group", "Box", "Start Time", "End Time", "MSN"]
    if file_path_to_meta_data is None:
        file_path_to_meta_data = defaultdict(dict)

    # Going through each line of the MED-PC data file
    with open(file_path) as file:
        for line in file.readlines():
            # Going through each header to see which line starts with the header
            for header in meta_data_headers:
                if line.strip().startswith(header):
                    # Removing all unnecessary characters
                    file_path_to_meta_data[file_path][header] = line.strip().replace(header, '').strip(":").strip()
                    # Move onto next line if header is found
                    break
    return file_path_to_meta_data

def main():
    """
    Main function that runs when the script is run
    """