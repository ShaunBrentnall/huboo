import pandas as pd
import os

#import from homography.py
"""
H:
[[ 1.05278912e+00  3.68006799e-01 -7.05496230e+02]
 [ 4.03594194e-02  1.02726776e+00 -1.35568230e+02]
 [-4.88941331e-06  5.97119721e-04  1.00000000e+00]]
"""

path = os.path.join("C:\Projects", "huboo", "data", "top_down_pick_and_pack_detection.csv.txt")

data = pd.read_csv(path)

print(data)