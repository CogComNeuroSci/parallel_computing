#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

from time import sleep

import os
import sys
import numpy as np

#%%

# get input from command line and check its length
cl = sys.argv[1:]
assert len(cl) == 3

# assign to some parameters
lr, sync, sub_id = sys.argv[1:]

# make a new folder (location depending on mode)
DATA_DIR = r"/user/gent/435/vsc43506/parameter_sweep/data"

# make a new folder
folder   = "BURST {0:1d} LR {1:.2f} - subject {2:02d}".format(int(sync), 
                                                              float(lr), 
                                                              int(sub_id))
NEWDIR   = os.path.join(DATA_DIR, folder)
if not os.path.exists(NEWDIR):
    os.makedirs(NEWDIR)

# save some data
np.save(os.path.join(NEWDIR, "weights"), np.random.random((100, 100)))
np.save(os.path.join(NEWDIR, "rt"), np.random.normal(300, 50, (100, 100)))

# stop for five seconds (300 * 5 /60 ~ 25 minutes is how long it would have taken when run sequentially, while now it will take only 1 minute)
sleep(5)
