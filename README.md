# MED-PC Data Analysis

## Overview TODO Edit

## Repository Organization TODO Edit

- med_pc_repo/bin
- med_pc_repo/jupyter_notebooks
- med_pc_repo/results
- med_pc_repo/src

## Steps To Take

Step 0. Clone this repository 
- Check if you have the Git program on your computer. Do this on the Bash terminal(Linux), Powershell(Windows), and Terminal(Mac). In the terminal, type `git` then enter. 
    - If you don't have Git on your computer, install it following these instructions: https://git-scm.com/downloads
- Once you have Git, download the repository in a folder that you want to save it in
    - From the terminal: `git clone https://github.com/padillacoreanolab/med_pc_repo`
- NOTE: Every time you use this repo after cloning it, check for updates with: 
    - `cd {./path/to}/med_pc_repo`
    - `git pull origin main`

Step 1. Create Conda environment to install necessary Python libraries
- Check if you have Anaconda:
    - Use the `python` command in your terminal. If you have Anaconda, then it will say "Anaconda" somewhere in the output.
    - If you don't have Anaconda, follow the installation instructions on: https://www.anaconda.com/ 
- Create the Conda environment by following the instructions in: [./bin/conda_environments/doc/README.md](./bin/conda_environments/doc/README.md)
- This step only needs to be done once. Every subsquent time you want to run the analysis, you'll turn on the Conda environment with:
    - `conda deactivate`
    - `conda activate {./path/to}/med_pc_repo/bin/conda_environments/env/med_pc_env`

Step 2. Turn on Jupyter Notebooks
- 1 Use the command `jupyter notebook --allow-root` in your terminal
- 1.1 If a browser window doesn't pop up with Jupyter notebooks, open up a browser window. Then copy and paste the URL given in the command line. It will be followed by `To access the notebook, open this file in a browser:` and `Or copy and paste one of these URLs:`
    - It should have a format similar to: `http://localhost:8888/?token=gsOH0vx373NRzHUmDzwX9TFzBf5Wx6czWIr1irV7ERKBLmlK`
- 2 Click on [./jupyter_notebooks](./jupyter_notebooks) in the Jupyter Notebooks GUI (Should be in the web browser)

Step 3. Follow the instructions to run the Jupyter Notebooks at [./jupyter_notebooks/README.MD](./jupyter_notebooks/README.MD)

## Resources

### MED-PC Trans
- https://www.med-associates.com/wp-content/uploads/2017/01/DOC-003-R3.4-SOF-735-MED-PC-IV-PROGRAMMER%E2%80%99S-MANUAL.pdf

### Python library to extract data from MED-PC Recording Files
- https://github.com/cyf203/medpc2excel
- https://pypi.org/project/medpc2excel/
