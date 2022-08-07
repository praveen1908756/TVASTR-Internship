from turtle import pos

filename1 = "D:\\GitHub-Reposatories\\Internship\\LogClass\\data\\new_data\\preprocessed_logs_word.txt"
lis1 = []
lis2 = []
cnt = 0
with open(filename1) as file:
    for line1 in file:
        lis1.append(line1)

for i in lis1:
    cnt = 0
    for j in lis1:
        if i == j:
            cnt += 1
    lis2.append(cnt)
    print(cnt, end='\n')
    with open(r'D:\\GitHub-Reposatories\\Internship\\LogClass\\data\\new_data\\preprocessed_logs_weight.txt', 'a') as fp:
        fp.write("%s\n" % cnt)
print("\n")