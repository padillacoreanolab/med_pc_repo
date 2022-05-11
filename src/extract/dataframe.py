#!/usr/bin/env python3
"""
Function for extracting the data from MED-PC output data files. 

For more information on the MED-PC's programming language, Trans: 
- https://www.med-associates.com/wp-content/uploads/2017/01/DOC-003-R3.4-SOF-735-MED-PC-IV-PROGRAMMER%E2%80%99S-MANUAL.pdf
"""
from collections import defaultdict
import traceback
from medpc2excel.medpc_read import medpc_read

def get_first_key_from_dictionary(input_dictionary):
    """
    Gets the first key from a dictionary. 
    Usually used to get the dataframe from the nested dictionary created by medpc2excel.medpc_read . 

    Args:
        input_dictionary: dict
            - A dictionary that you want to get the first key from
    
    Returns:
        str (usually)
            - First key to the inputted dictionary
    """
    # Turns the dictionary keys into a list and gets the first item
    return list(input_dictionary.keys())[0]

def get_medpc_dataframe_from_medpc_read_output(medpc_read_dictionary_output):
    """
    Gets the dataframe from the output from medpc2excel.medpc_read, that extracts data from a MED-PC file.
    This is done by getting the values of the nested dictionaries. 

    Args:
        medpc_read_dictionary_output: Nested defaultdict
            - The output from medpc2excel.medpc_read . 
            This contains the dataframe extracted from MED-PC file

    Returns:
        str(usually), str(usually), Pandas DataFrame
            - The data key to the medpc2excel.medpc_read output
            - The subject key to the medpc2excel.medpc_read
            - The dataframe extracted from the MED-PC file
    """
    date_key = get_first_key_from_dictionary(input_dictionary=medpc_read_dictionary_output)
    subject_key = get_first_key_from_dictionary(input_dictionary=medpc_read_dictionary_output[date_key])
    # Dataframe must use both the date and subject key with the inputted dictionary
    return date_key, subject_key, medpc_read_dictionary_output[date_key][subject_key]

def get_medpc_dataframe_from_list_of_files(medpc_files, stop_with_error=False):
    """
    Gets the dataframe from the output from medpc2excel.medpc_read that extracts data from a MED-PC file.
    This is done with multiple files from a list. And the date and the subject of the recording session is extracted as well.
    Everything is stored in a nested dictionary of file path keys to the values "date_key", "subject_key", "medpc_df". 
    Which are the keys to corresponding date, subject name, and MED-PD dataframe.

    Args:
        medpc_files: list
            - List of MED-PC recording files. Can be either relative or absolute paths.
        stop_with_error: bool
            - Flag to terminate the program when an error is raised.
            - Sometimes MED-PC files have incorrect formatting, so can be skipped over.
    Returns:
        file_path_to_medpc_data
            - A nested dictionary of file path keys to the values "date_key", "subject_key", "medpc_df". 
            Which are the keys to corresponding date, subject name, and MED-PD dataframe.
    """
    file_path_to_medpc_data = defaultdict(dict)
    for file_path in medpc_files:
        try:
            # Reading in the MED-PC log file
            ts_df, medpc_log = medpc_read(file=file_path, override=True, replace=False)
            # Extracting the corresponding MED-PC Dataframe, date, and subject ID
            date_key, subject_key, medpc_df = get_medpc_dataframe_from_medpc_read_output(medpc_read_dictionary_output=ts_df)
            file_path_to_medpc_data[file_path]["date_key"] = date_key
            file_path_to_medpc_data[file_path]["subject_key"] = subject_key
            file_path_to_medpc_data[file_path]["medpc_df"] = medpc_df
        except Exception: 
            # Printing out error messages and the corresponding traceback
            print(traceback.format_exc())
            if stop_with_error:
                # Stopping the program all together
                raise ValueError("Invalid Formatting for file: {}".format(file_path))
            else:
                # Continuing with execution
                print("Invalid Formatting for file: {}".format(file_path))
    return file_path_to_medpc_data

def main():
    """
    Main function that runs when the script is run
    """

if __name__ == '__main__': 
    main()
