#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CirQ
# Created Time: 2017-05-08 23:22:17

import re
import math
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error


def test_trainset(method, model, n_splits=None):
    dim = re.match(r"^\D+(\d+)$", method).group(1)
    features = ["radar_map"]
    features.extend(["radar_map.%d" % i for i in range(1, int(dim))])
    trainset = pd.read_csv("/media/cirq/All matters/CIKMmining/VECTOR_%s_train.csv" % method)
    X, y = trainset[features], trainset.label

    y_expand = y[0] / 2.3  # meaning: y is expanded by so much times

    if n_splits:
        kf = KFold(n_splits=n_splits).split(y)
        X = X.loc
        RMSEs = []
        for train, test in kf:
            X_train = [X[i] for i in train]
            X_test = [X[i] for i in test]
            y_train = [y[i] for i in train]
            y_real = [y[i]/y_expand for i in test]
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            RMSE = math.sqrt(mean_squared_error(y_real, y_pred/y_expand))
            RMSEs.append(RMSE)
            del X_train, X_test, y_train, y_real
        print RMSEs, np.mean(RMSEs)
    else:
        model.fit(X, y)
    return model, y_expand


def pred_testset(method, model, y_expand):
    dim = re.match(r"^\D+(\d+)$", method).group(1)
    features = ["radar_map"]
    features.extend(["radar_map.%d" % i for i in range(1, int(dim))])
    testset = pd.read_csv("/media/cirq/All matters/CIKMmining/VECTOR_%s_testB.csv" % method)
    X_test = testset[features]
    y_pred = model.predict(X_test)
    with open("/media/cirq/All matters/CIKMmining/RESULT_%s.csv" % method, "w") as w:
        for pred in y_pred:
            if pred > 1e-4:
                w.write("%.4f\n" % (pred/y_expand))
            else:
                w.write("0.0\n")


if __name__ == "__main__":
    method = "gridsum_d324"
    model, y_expand = test_trainset(method, Lasso(alpha=0.9, max_iter=1000), n_splits=10)
    # pred_testset(method, model, y_expand)
