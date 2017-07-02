#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CirQ
# Created Time: 2017-05-12 17:28:03

import numpy as np


method_list = ["gridsum_d540", "gridsum_d324", "gaussiansum_d60"]
rsme_list = [16.0753, 16.0301, 14.6318]

record = np.zeros((2000, len(method_list)))

for j in range(len(method_list)):
    with open("RESULT_%s.csv" % method_list[j], "r") as read:
        for i in range(2000):
            l = read.readline()
            if not l: break
            record[i][j] = float(l) * rsme_list[j] / np.sum(rsme_list)

weightedsum = record.sum(axis=1)
with open("RESULT_weightedsum.csv", "w") as w:
    for f in weightedsum:
        if f > 1e-4:
            w.write("%.4f\n" % f)
        else:
            w.write("0.0\n")
