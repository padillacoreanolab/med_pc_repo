#!/usr/bin/env bash

# Moving to the root directory of the Github repo
git_top_level="$(git rev-parse --show-toplevel)"
cd $(git_top_level)

# Creating the Conda environment
conda create --prefix ./bin/conda_environments/env/med_pc_env python=3.9 --yes
# Turning on the Conda environment
conda activate ./bin/conda_environments/env/med_pc_env

# Installing the Python libraries
pip install medpc2excel
conda install -c conda-forge openpyxl --yes
conda install -c conda-forge notebook --yes
conda install -c conda-forge matplotlib --yes
conda install -c conda-forge pylint --yes
