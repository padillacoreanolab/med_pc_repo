# MED-PC Data Analysis

## Overview

## Repository Organization

- med_pc_repo/bin
- med_pc_repo/jupyter_notebooks
- med_pc_repo/results
- med_pc_repo/src

## Steps To Take

Step 1. Create Conda Environment to install necessary Python libraries
    - Follow the instructions in: [./bin/conda_environments/doc/README.md](./bin/conda_environments/doc/README.md)

Step 2. Turn on Jupyter Notebooks
    - 1 Use the command `jupyter notebook --allow-root` in your terminal
    - 1.1 If a browser window doesn't pop up with Jupyter notebooks, open up a browser window. Then copy and paste the URL given in the command line. It will be followed by `To access the notebook, open this file in a browser:` and `Or copy and paste one of these URLs:`
        - It should have a format similar to: `http://localhost:8888/?token=gsOH0vx373NRzHUmDzwX9TFzBf5Wx6czWIr1irV7ERKBLmlK`
    - 2 Click on [./jupyter_notebooks](./jupyter_notebooks) in the Jupyter Notebooks GUI (Should be on a web browser)

Step 3. Follow the instructions to run the Jupyter Notebooks at [./jupyter_notebooks/README.MD](./jupyter_notebooks/README.MD)

## Resources

### Python library to extract data from MED-PC Recording Files
- https://github.com/cyf203/medpc2excel
- https://pypi.org/project/medpc2excel/
