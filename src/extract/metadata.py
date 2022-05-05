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
    Parses out the metadata from output of a MED-PC data file.
    The output file looks something like:
        Start Date: 05/04/22
        End Date: 05/04/22
        Subject: 4.4 (4)
        Experiment: Pilot of Pilot
        Group: Cage 4
        Box: 1
        Start Time: 13:06:15
        End Time: 14:10:05
        MSN: levelNP_CS_reward_laserepochON1st_noshock
    The metadata will be saved into a nested default dictionary. 
    With the file path as the key, and the meta data headers as the values. 
    And then the meta data headers are the nested keys, and the meta data as the values.

    The dictionary would look something like:
    defaultdict(dict,
            {'./data/2022-05-04_13h06m_Subject 4.4 (4).txt': {'File': 'C:\\MED-PC\\Data\\2022-05-04_13h06m_Subject 4.4 (4).txt',
              'Start Date': '05/04/22',
              'End Date': '05/04/22',
              'Subject': '4.4 (4)',
              'Experiment': 'Pilot of Pilot',
              'Group': 'Cage 4',
              'Box': '1',
              'Start Time': '13:06:15',
              'End Time': '14:10:05',
              'MSN': 'levelNP_CS_reward_laserepochON1st_noshock'}})
    
    Args:
        file_path: str
            - The path to the MED-PC data file 
        meta_data_headers: list
            - List of the types of metadata to be parsed out for
        file_path_to_meta_data: Nested Default Dictionary
            - Any dictionary that has already been produced by this function that more metadata is chosen to be added to.
            The dictionary will have the file path as the key, and the meta data headers as the values. 
            And then the meta data headers are the nested keys, and the meta data as the values.
    
    Returns:
        Nested Default Dictionary:
            - With the file path as the key, and the meta data headers as the values. 
            And then the meta data headers are the nested keys, and the meta data as the values.
    """
    # The default metadata found in MED-PC files
    if meta_data_headers is None:
        meta_data_headers = ["File", "Start Date", "End Date", "Subject", "Experiment", "Group", "Box", "Start Time", "End Time", "MSN"]
    # Creating a new dictionary if none is inputted
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
    pass

if __name__ == '__main__': 
    main()