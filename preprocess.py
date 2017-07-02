#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CirQ
# Created Time: 2017-05-08 09:25:07

def get_row_in_dataset(dataset):  # dataset can only be train, testA, testB
    with open("/media/cirq/All matters/CIKM/%s.txt" % dataset, "r") as r:
        while True:
            line = r.readline().strip()
            if not line:
                break
            row_id, label, radar_map = line.split(",")
            del line
            yield row_id, float(label), [float(z) for z in radar_map.split(" ")]
            del row_id, label, radar_map


# a useless method checking for the correctness of data format
def validate_dataset(dataset):
    with open("/media/cirq/All matters/CIKMmining/validate_%s.txt" % dataset, "w") as w:
        for row_id, label, radar_map in get_row_in_dataset(dataset):
            vlen = len(radar_map)
            if vlen != 612060:  # 612060 = 15 * 4 * 101 * 101
                w.write("%s %.2f %d\n" % (row_id, label, vlen))
            else:
                w.write(row_id+"->is!\n")
            print "validate ", row_id


import re
def generate_csv(method, dataset):
    dim = re.match(r"^\D+(\d+)$", method).group(1)
    with open("/media/cirq/All matters/CIKMmining/VECTOR_%s_%s.csv" % (method, dataset), "w") as w:
        w.write('"row_id","label"' + ',"radar_map"'*int(dim) + '\n')
        for row_id, label, radar_map in get_row_in_dataset(dataset):
            w.write("\"%s\"," % row_id)
            struct_map = [[radar_map[40804*t+10201*h:40804*t+10201*(h+1)] for h in range(4)] for t in range(15)]
            vector = eval("%s(label, struct_map)" % method)
            w.write(",".join([str("%.2f" % f) for f in vector]))
            w.write("\n")
            print "processing", row_id


if __name__ == "__main__":
    from methods import *
    method = "timesum_h_d99"
    while True:
        b = raw_input("want to generate data vector? (y/n) ")
        if b == "y":
            break
        elif b == "n":
            import sys
            sys.exit(0)
    generate_csv(method, "train")
    generate_csv(method, "testB")
