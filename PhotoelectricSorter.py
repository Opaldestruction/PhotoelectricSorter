# This is a sample Python script.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from colour import Color

# These variables are inputted from the command line
temp = 0  # Temperature (in kelvin)
wavelength = 0  # Wavelength (in meters)

# Their original values have no meaning, I'm just not good enough with python to not init them.

WF_database = pd.read_csv('WF_database_29270_part1.csv')
WF_database2 = pd.read_csv('WF_database_29270_part2.csv')

aluminums, aluminumsH = [], []
zincs, zincsH = [], []
magnesiums, magnesiumsH = [], []
silicons, siliconsH = [], []
titaniums, titaniumsH = [], []

wf = 0  # work function
matName = 'AlCl'  # name of the material
print(len(WF_database.columns))
print(WF_database.size / len(WF_database.columns))

for row in WF_database.itertuples(index=False):
    matName = row.surface_elements_string
    if "Al" in matName:
        aluminums.insert(aluminums.__len__(), matName)
        aluminumsH.insert(aluminumsH.__len__(), row.WF)

    if "Zn" in matName:
        zincs.insert(zincs.__len__(), matName)
        zincsH.insert(zincsH.__len__(), row.WF)

    if "Mn" in matName:
        magnesiums.insert(magnesiums.__len__(), matName)
        magnesiumsH.insert(magnesiumsH.__len__(), row.WF)

    if "Si" in matName:
        silicons.insert(silicons.__len__(), matName)
        siliconsH.insert(siliconsH.__len__(), row.WF)

    if "Ti" in matName:
        titaniums.insert(titaniums.__len__(), matName)
        titaniumsH.insert(titaniumsH.__len__(), row.WF)



gray = Color("#a2b1ae")
fig, al = plt.subplots()

colors = list(gray.range_to(Color("#010101"), aluminums.__len__()))
for i, color in enumerate(colors):
    colors[i] = color.hex

al.bar(aluminums, aluminumsH, label=aluminums, color=(0, 0, 0, 1))
al.set_ylabel('Work Function')
al.set_title('Aluminum compounds and their work functions')
plt.show()

fig, zn = plt.subplots()

zn.bar(zincs, zincsH, label=zincs, color=(0, 0, 0, 1))
zn.set_ylabel('Work Function')
zn.set_title('zinc compounds and their work functions')
plt.show()

fig, mn = plt.subplots()

mn.bar(magnesiums, magnesiumsH, label=magnesiums, color=(0, 0, 0, 1))
mn.set_ylabel('Work Function')
mn.set_title('magnesium compounds and their work functions')
plt.show()

fig, si = plt.subplots()


si.bar(silicons, siliconsH, label=silicons, color=(0, 0, 0, 1))
si.set_ylabel('Work Function')
si.set_title('Silicon compounds and their work functions')
plt.show()

fig, ti = plt.subplots()

ti.bar(titaniums, titaniumsH, label=titaniums, color=(0, 0, 0, 1))
ti.set_ylabel('Work Function')
ti.set_title('titanium compounds and their work functions')
plt.show()



