import argparse
parser = argparse.ArgumentParser()                                               

parser.add_argument("--file1", "-f1", type=str, required=True)
parser.add_argument("--file2", "-f2", type=str, required=True)
args = parser.parse_args()

weight = open(args.file1,"r")
data_weight = weight.readlines()

template = open(args.file2,"r")
l = template.readlines()