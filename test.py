#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CirQ
# Created Time: 2017-05-12 08:10:08


from preprocess import *
def pre(method):
    while True:
        b = raw_input("want to generate data vector? (y/n) ")
        if b == "y":
            break
        elif b == "n":
            import sys
            sys.exit(0)
    generate_csv(method, "testA")
    generate_csv(method, "train")


from learning import *
def learning(method, n_splits=None):
    while True:
        b = raw_input("want to learning the data? (y/n) ")
        if b == "y":
            break
        elif b == "n":
            import sys
            sys.exit(0)
    if n_splits:
        RMSEs = test_trainset(method, LinearRegression(), n_splits=n_splits)
        print "RMSEs of method", method, "is\n", RMSEs
        print "average RMSE of method", method, "is", reduce(lambda x,y:x+y,RMSEs)/len(RMSEs)
    else:
        model, y_expand = test_trainset(method, LinearRegression())
        pred_testset(method, model, y_expand)


if __name__ == "__main__":
    method = "gaussiansum_d60"
    # pre(method)
    learning(method, n_splits=10)
