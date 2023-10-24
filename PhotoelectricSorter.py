# This is a sample Python script.
import numpy as np
import pandas as pd

# These variables are inputted from the command line
temp = 0  # Temperature (in kelvin)
wavelength = 0  # Wavelength (in meters)

# Their original values have no meaning, I'm just not good enough with python to not init them.

WF_database = pd.read_csv('WF_database_29270_part1.csv')
WF_database2 = pd.read_csv('WF_database_29270_part2.csv')

wf = 0  # work function
matName = 'AlCl'  # name of the material
print(len(WF_database.columns))
print(WF_database.size / len(WF_database.columns))

for row in WF_database.itertuples(index=False):
    matName = row.surface_elements_string
    wf = row.WF
    print(f'{matName}: {wf}')
