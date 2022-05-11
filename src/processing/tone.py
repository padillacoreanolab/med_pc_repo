#!/usr/bin/env python3
"""
Functions for processing tone information from MED-PC's output

For more information on the MED-PC's programming language, Trans: 
- https://www.med-associates.com/wp-content/uploads/2017/01/DOC-003-R3.4-SOF-735-MED-PC-IV-PROGRAMMER%E2%80%99S-MANUAL.pdf
"""
from collections import defaultdict
import pandas as pd

def get_max_tone_number(tone_pd_series):
    """
    Gets the index, and the number for valid tones in MED-PC's outputted data.
    The recorded tones produce numbers that are divisible by 1000 after the recorded data.
    You can use the index to remove these unnecessary numbers by indexing until that number.

    Args:
        tone_pd_series: Pandas Series
            - A column from the dataframe that contains the data from MED-PC's output file
            - Usually created with dataframe_variable["(S)CSpresentation"]
    Returns:
        int, float
            - The index of the max tone number. This number can be used to index the tone_pd_series to remove unnecessary numbers.
            - The max tone number. This number can be used to verify whether or not the tone_pd_series had unnecessary numbers.
    """
    for index, num in enumerate(tone_pd_series):
        if num % 1000 == 0:
            return index, num
    return index, num

def get_valid_tones(tone_pd_series, drop_1000s=True, dropna=True):
    """
    Removes all unnecessary numbers from a Pandas Series of tone times extracted from MED-PC's dataframe.
    The unnecessary numbers are added after recorded tone times. These numbers are usually divisible by 1000. 
    NaNs are also added after that. So we will remove all tone times entries that meet either of these criterias.

    Args:
        tone_pd_series: Pandas Series
            - 
        dropna: bool
            - Whether or not you want to remove NaNs from tone_pd_series.
            - Usually a good idea because MED-PC adds NaNs to the tone time column.
    Returns: 
        Pandas series
            - The tone times with unnecessary numbers and NaNs removed
    """
    if dropna:
        tone_pd_series = tone_pd_series.dropna()
    if drop_1000s:
        # Getting the index of the tone time that is divisible by 1000
        max_tone_index, max_tone_number = get_max_tone_number(tone_pd_series=tone_pd_series)
        tone_pd_series = tone_pd_series[:max_tone_index]
    # Removing all numbers that are after the max tone
    return tone_pd_series

def get_first_port_entries(tone_pd_series, port_entries_pd_series):
    """
    TODO: ADD DOC STRING
    """
    # Creating a dictionary of index(current row number we're on) to current/next tone time and first port entry
    first_port_entry_dict = defaultdict(dict)
    for index, current_tone_time in tone_pd_series.items():
        # Using a counter so that we don't go through all the rows that include NaNs
        try:
            first_port_entry_dict[index]["current_tone_time"] = current_tone_time
            # Getting all the port entries that happened after the tone started
            # And then getting the first one of those port entries
            first_port_entry_after_tone = port_entries_pd_series[port_entries_pd_series >= current_tone_time].min()
            first_port_entry_dict[index]["first_port_entry_after_tone"] = first_port_entry_after_tone
        except:
            print("Look over value {} at index {}".format(current_tone_time, index))
    return first_port_entry_dict

def get_concatted_first_porty_entry_dataframe(file_path_to_medpc_data, medpc_key="medpc_df", tone_time_column="(S)CSpresentation", \
        port_entry_column="(P)Portentry", stop_with_error=False):
    """
        Removes all unnecessary numbers from a Pandas Series of tone times extracted from MED-PC's dataframe.
    The unnecessary numbers are added after recorded tone times. These numbers are usually divisible by 1000. 
    NaNs are also added after that. So we will remove all tone times entries that meet either of these criterias.
    TODO: EDIT HERE
    Args:
        file_path_to_medpc_data, medpc_key="medpc_df", tone_time_column="(S)CSpresentation", \
        port_entry_column="(P)Portentry", stop_with_error=False
    
    Returns: 
        Pandas Dataframe
            - The tone times with unnecessary numbers and NaNs removed
    """
    # List to combine all the Data Frames at the end
    all_first_port_entry_df = []
    for key, value in file_path_to_medpc_data.items():
        # Getting the corresponding Dataframe for the MED-PC the current
        medpc_df = value[medpc_key]
        # Sometimes tones are NaN or just random numbers
        valid_tones = get_valid_tones(tone_pd_series=medpc_df[tone_time_column])
        # Sometimes the valid tones do not exist because it was a test recording
        if not valid_tones.empty:
            # All the first port entries for each tone            
            first_port_entry_dict = get_first_port_entries(tone_pd_series=valid_tones, port_entries_pd_series=medpc_df[port_entry_column])
            # Turning the dictionary into a Data Frame
            first_port_entry_df = pd.DataFrame.from_dict(first_port_entry_dict, orient="index")
            # Adding the metadata as columns
            first_port_entry_df["file_path"] = key
            first_port_entry_df["date_key"] = file_path_to_medpc_data[key]["date_key"]
            first_port_entry_df["subject_key"] = file_path_to_medpc_data[key]["subject_key"]
            all_first_port_entry_df.append(first_port_entry_df)
        elif valid_tones.empty and stop_with_error:
            raise ValueError("No valid tones for {}".format(key))
        else:
            print("No valid tones for {}".format(key))
    return pd.concat(all_first_port_entry_df)

def main():
    """
    Main function that runs when the script is run
    """

if __name__ == '__main__': 
    main()
