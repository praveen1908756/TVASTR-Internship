filename1 = open("D:\\GitHub-Reposatories\\Internship\\LogClass\\data\\new_data\\preprocessed_logs_full.txt", "r")
filename2 = open("D:\\GitHub-Reposatories\\Internship\\LogClass\\data\\new_data\\preprocessed_logs_word.txt","r")
filename3 = open("D:\\GitHub-Reposatories\\Internship\\LogClass\\data\\new_data\\preprocessed_logs_occurences.txt","w")

lis1 = []

def find():
    for line1 in filename2:
        lis1.append(line1)

find()
cnt = 0

for line in filename1:
    if(line[:17] != "NewTemplateXXXXX " and line[:17] != "Seq/QuantXXXXXXX "):
        filename3.write("-1")
        filename3.write('\n')
    else:
        filename3.write("1")
        filename3.write('\n')
        # cnt = 0
        # for i in lis1:
        #     # print(i, " =? ", line[17:], end="\n")
        #     if i == line[17:]:
        #         cnt += 1
        # filename3.write(str(cnt))
        # filename3.write('\n')
        # filename3.write(line[:17])
        # filename3.write('\n')