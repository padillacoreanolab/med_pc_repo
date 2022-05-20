# `med_pc_repo/jupyter_notebooks/data` Directory Layout

## Directories

- `med_pc_repo/jupyter_notebooks/data/timestamp_dataframes`
    - Where all the recordings from MED-PC will be stored
    - NOTE: The processing notebooks will not run if you do not include the MED-PC script in the same directory as the recordings. This script will have been used during the recording sessions and contains the names of the variables in the recorded data. The script will have the `.mpc` extension.
    - You can also create subdirectories in this directory, but you will need to change the path in the notebooks.