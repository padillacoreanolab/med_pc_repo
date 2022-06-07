#!/usr/bin/env bash

# Moving to the root directory of the Github repo
# Uncomment if using Linux or Mac
# cd $(git rev-parse --show-toplevel)

# Creating the Conda environment
conda create --prefix ./med_pc_env python=3.9 --yes
# Turning on the Conda environment
conda activate ./med_pc_env

# Installing the Python libraries
pip install medpc2excel
conda install -c conda-forge openpyxl --yes
conda install -c conda-forge notebook --yes
conda install -c conda-forge matplotlib --yes

# Running Jupyter Notebooks
jupyter notebook --allow-root