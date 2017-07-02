#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CirQ
# Created Time: 2017-05-10 08:41:54

import numpy as np

# This file include methods to generate data vectors, one row for one vector

def gridsum_d540(label, struct_map):  # final evaluation is 16.0753
    vector = [label*10000]  # here the label is expanded with 10000 timestand should be divided during predction

    for t in range(15):  # get 15 groups as 15 time spans, t stands for temporal
        for s in range(4):  # get 4 groups as 4 height records, s stands for spacial

            reduced_map = [0 for k in range(81)]

            for i in range(1, 100):  # iterate the grid map
                for j in range(1, 100):  # only the middle 99*99 will be chosen
                    if struct_map[t][s][101*i+j] == -1.0:  # outliers process
                        struct_map[t][s][101*i+j] = 0.0
                        surround, count = 0.0, 0
                        for I in [-1, 0, 1]:
                            for J in [-1, 0, 1]:
                                if struct_map[t][s][101*(i+I)+(j+J)] != -1.0:
                                    surround += struct_map[t][s][101*(i+I)+(j+J)]
                                    count += 1
                        struct_map[t][s][101*i+j] = surround / count

                    I = (i - 1) / 11
                    J = (j - 1) / 11
                    reduced_map[9*I+J] += struct_map[t][s][101*i+j]
            struct_map[t][s] = [(reduced_map[i]+reduced_map[i+1]+reduced_map[i+2])/3 for i in range(0,81,3)]
        if t % 3 != 0:
            for s in range(4):
                for k in range(27):
                    struct_map[t-(t%3)][s][k] += struct_map[t][s][k]
    for t in struct_map[::3]:
        for s in t:
            vector.extend(s)

    del struct_map
    return vector


def gridsum_d1620(label, struct_map):  # final evaluation is 17.0613
    vector = [label*10000]  # here the label is expanded with 10000 timestand should be divided during predction

    for t in range(15):  # get 15 groups as 15 time spans, t stands for temporal
        for s in range(4):  # get 4 groups as 4 height records, s stands for spacial

            reduced_map = [0 for k in range(81)]

            for i in range(1, 100):  # iterate the grid map
                for j in range(1, 100):  # only the middle 99*99 will be chosen
                    if struct_map[t][s][101*i+j] == -1.0:  # outliers process
                        struct_map[t][s][101*i+j] = 0.0
                        surround, count = 0.0, 0
                        for I in [-1, 0, 1]:
                            for J in [-1, 0, 1]:
                                if struct_map[t][s][101*(i+I)+(j+J)] != -1.0:
                                    surround += struct_map[t][s][101*(i+I)+(j+J)]
                                    count += 1
                        struct_map[t][s][101*i+j] = surround / count

                    I = (i - 1) / 11
                    J = (j - 1) / 11
                    reduced_map[9*I+J] += struct_map[t][s][101*i+j]
            vector.extend([(reduced_map[i]+reduced_map[i+1]+reduced_map[i+2])/3 for i in range(0,81,3)])

    del struct_map
    return vector


def gridsum_d324(label, struct_map):  # final evaluation is 16.0301
    vector = [label*10000]  # here the label is expanded with 10000 timestand should be divided during predction

    for t in range(15):  # get 15 groups as 15 time spans, t stands for temporal
        for s in range(4):  # get 4 groups as 4 height records, s stands for spacial

            reduced_map = [0 for k in range(81)]

            for i in range(1, 100):  # iterate the grid map
                for j in range(1, 100):  # only the middle 99*99 will be chosen
                    if struct_map[t][s][101*i+j] == -1.0:  # outliers process
                        struct_map[t][s][101*i+j] = 0.0
                        surround, count = 0.0, 0
                        for I in [-1, 0, 1]:
                            for J in [-1, 0, 1]:
                                if struct_map[t][s][101*(i+I)+(j+J)] != -1.0:
                                    surround += struct_map[t][s][101*(i+I)+(j+J)]
                                    count += 1
                        struct_map[t][s][101*i+j] = surround / count

                    I = (i - 1) / 11
                    J = (j - 1) / 11
                    reduced_map[9*I+J] += struct_map[t][s][101*i+j]
            struct_map[t][s] = [(reduced_map[i]+reduced_map[i+1]+reduced_map[i+2])/3 for i in range(0,81,3)]
        if t % 5 != 0:
            for s in range(4):
                for k in range(27):
                    struct_map[t-(t%5)][s][k] += struct_map[t][s][k]
    for t in struct_map[::5]:
        for s in t:
            vector.extend(s)

    del struct_map
    return vector


def gaussiansum_d60(label, struct_map):  # final evaluation is 14.6318
    vector = [label*100]  # here the label is expanded with 100 timestand should be divided during predction

    for t in range(15):  # get 15 groups as 15 time spans, t stands for temporal
        for s in range(4):  # get 4 groups as 4 height records, s stands for spacial

            gaussiansum = 0.0
            sigmas = np.var(struct_map[t][s])
            if sigmas < 1e-4: sigmas = 100
            gaussian = lambda x, y: 0.16/(sigmas*(1.13**((x*x+y*y)/sigmas)))

            for i in range(1, 100):  # iterate the grid map
                for j in range(1, 100):  # only the middle 99*99 will be chosen
                    if struct_map[t][s][101*i+j] == -1.0:  # outliers process
                        struct_map[t][s][101*i+j] = 0.0
                        surround, count = 0.0, 0
                        for I in [-1, 0, 1]:
                            for J in [-1, 0, 1]:
                                if struct_map[t][s][101*(i+I)+(j+J)] != -1.0:
                                    surround += struct_map[t][s][101*(i+I)+(j+J)]
                                    count += 1
                        struct_map[t][s][101*i+j] = surround / count

                    gaussiansum += struct_map[t][s][101*i+j] * gaussian(i-50, j-50)
            vector.append(gaussiansum)

    del struct_map
    return vector


def timesum_h_d99(label, struct_map):  # final evaluation is 14.7946 alpha=0.7, 14.7798 alpha=0.9
    for t in range(15):  # get 15 groups as 15 time spans, t stands for temporal
        for s in range(4):  # get 4 groups as 4 height records, s stands for spacial
            for i in range(1, 100):  # iterate the grid map
                for j in range(1, 100):  # only the middle 99*99 will be chosen
                    if struct_map[t][s][101*i+j] == -1.0:  # outliers process
                        struct_map[t][s][101*i+j] = 0.0
                        surround, count = 0.0, 0
                        for I in [-1, 0, 1]:
                            for J in [-1, 0, 1]:
                                if struct_map[t][s][101*(i+I)+(j+J)] != -1.0:
                                    surround += struct_map[t][s][101*(i+I)+(j+J)]
                                    count += 1
                        struct_map[t][s][101*i+j] = surround / count

    alpha = 0.9
    vector = [label*100]  # here the label is expanded with 100 timestand should be divided during predction
    for i in range(1, 100):
        sums = []
        for j in range(1, 100):
            timesum = 0.0
            for s in range(4):
                series = np.zeros((15,))
                series[0] = struct_map[0][s][101*i+j]
                for t in range(1, 15):
                    series[t] = alpha * struct_map[t][s][101*i+j] + (1 - alpha) * series[t-1]
                timesum += series[-1] * (4-s) / 10.0
            sums.append(timesum)
        vector.append(np.mean(sums))

    del struct_map
    return vector


def timesum_v_d99(label, struct_map):
    for t in range(15):  # get 15 groups as 15 time spans, t stands for temporal
        for s in range(4):  # get 4 groups as 4 height records, s stands for spacial
            for i in range(1, 100):  # iterate the grid map
                for j in range(1, 100):  # only the middle 99*99 will be chosen
                    if struct_map[t][s][101*i+j] == -1.0:  # outliers process
                        struct_map[t][s][101*i+j] = 0.0
                        surround, count = 0.0, 0
                        for I in [-1, 0, 1]:
                            for J in [-1, 0, 1]:
                                if struct_map[t][s][101*(i+I)+(j+J)] != -1.0:
                                    surround += struct_map[t][s][101*(i+I)+(j+J)]
                                    count += 1
                        struct_map[t][s][101*i+j] = surround / count

    alpha = 0.7
    vector = [label*100]  # here the label is expanded with 100 timestand should be divided during predction
    for j in range(1, 100):
        sums = []
        for i in range(1, 100):
            timesum = 0.0
            for s in range(4):
                series = np.zeros((15,))
                series[0] = struct_map[0][s][101*i+j]
                for t in range(1, 15):
                    series[t] = alpha * struct_map[t][s][101*i+j] + (1 - alpha) * series[t-1]
                timesum += series[-1] * (4-s) / 10.0
            sums.append(timesum)
        vector.append(np.mean(sums))

    del struct_map
    return vector


if __name__ == "__main__":
    from preprocess import get_row_in_dataset

    for row_id, label, radar_map in get_row_in_dataset("data_sample"):
        struct_map = [[radar_map[40804*t+10201*h:40804*t+10201*(h+1)] for h in range(4)] for t in range(15)]
        vectorh = timesum_h_d99(label, struct_map)
        vectorv = timesum_v_d99(label, struct_map)
        print vectorh
        print vectorv
