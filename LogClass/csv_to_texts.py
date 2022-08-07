import pandas as pd
import re

df = pd.read_csv('D:\\GitHub-Reposatories\\Internship\\LogClass\\data\\FP2\\test_2022-05-24_11_22_54.csv')

df["result"].to_csv('D:\\GitHub-Reposatories\\Internship\\LogClass\\data\\FP2\\preprocessed_logs_weight.txt', sep="\n", index=False, header = False)

df["words"].to_csv('D:\\GitHub-Reposatories\\Internship\\LogClass\\data\\FP2\\preprocessed_logs_word.txt', sep="\n", index=False, header = False)

#removing first four characters
f = open("D:\\GitHub-Reposatories\\Internship\\LogClass\\data\\FP2\\preprocessed_logs_word.txt","r")
data = f.readlines()
for i in range(len(data)):
    data[i] = data[i][4:]
f.close()

for i in range(len(data)):
    for j in range(len(data[i])):
        if(re.search("[0-9]", data[i][j])):
            data[i][j] = ""

f = open("D:\\GitHub-Reposatories\\Internship\\LogClass\\data\\FP2\\preprocessed_logs_word1.txt","w")
for i in range(len(data)):
    f.write(data[i])
f.close()

#conv to -1 and 1: healthy and anomalous respectively
f = open("D:\\GitHub-Reposatories\\Internship\\LogClass\\data\\FP2\\preprocessed_logs_weight.txt","r")
data = f.readlines()
for i in range(len(data)):
    if(data[i] == "NewTemplate\n" or data[i] == "Seq/Quant\n"):
        data[i] = '1\n'
    else:
        data[i] = '-1\n'
f.close()
f = open("D:\\GitHub-Reposatories\\Internship\\LogClass\\data\\FP2\\preprocessed_logs_weight.txt","w")
for i in range(len(data)):
    f.write(data[i])
f.close()