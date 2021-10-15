#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

from time import sleep

import numpy as np
import sys

#%%

# get identifier of the datafile you want to process
val = sys.argv[1:]
assert len(val) == 1
val = val[0]

# load the dataset based on the provided identifier
arr = np.load("/data/gent/435/vsc43506/job_arrays/input/dataset_{}.npy".format(val))

# save the output
np.save("/data/gent/435/vsc43506/job_arrays/output/dataset_{}".format(val), np.log(arr))

# wait five seconds
sleep(5)