#!/usr/bin/env python3
"""
Function for extracting the data from MED-PC output data files. 

For more information on the MED-PC's programming language, Trans: 
- https://www.med-associates.com/wp-content/uploads/2017/01/DOC-003-R3.4-SOF-735-MED-PC-IV-PROGRAMMER%E2%80%99S-MANUAL.pdf
"""

def get_first_key_from_dictionary(input_dictionary):
    """
    Gets the first key from a dictionary. 
    Usually used to get the dataframe from the nested dictionary created by medpc2excel.medpc_read . 

    Args:
        input_dictionary: dict
    
    Returns:
        str (usually)
            - First key to the inputted dictionary
    """
    # Turns the dictionary keys into a list and gets the first item
    return list(input_dictionary.keys())[0]

def get_med_pc_dataframe(medpc_read_dictionary_output):
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


def main():
    """
    Main function that runs when the script is run
    """

if __name__ == '__main__': 
    main()
