#!/usr/bin/env python3
"""
Functions for processing tone information from MED-PC's output

For more information on the MED-PC's programming language, Trans: 
- https://www.med-associates.com/wp-content/uploads/2017/01/DOC-003-R3.4-SOF-735-MED-PC-IV-PROGRAMMER%E2%80%99S-MANUAL.pdf
"""
from collections import defaultdict

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
    latency_dict = defaultdict(dict)
    for index, current_tone_time in tone_pd_series.items():
        # Using a counter so that we don't go through all the rows that include NaNs
        try:
            latency_dict[index]["current_tone_time"] = current_tone_time
            # Getting all the port entries that happened after the tone started
            # And then getting the first one of those port entries
            first_port_entry_after_tone = port_entries_pd_series[port_entries_pd_series >= current_tone_time].min()
            latency_dict[index]["first_port_entry_after_tone"] = first_port_entry_after_tone
        except:
            print("Look over value {} at index {}".format(current_tone_time, index))
    return latency_dict

def main():
    """
    Main function that runs when the script is run
    """

if __name__ == '__main__': 
    main()
