import pickle

print("vocab.pkl\n")
with open('D:\\GitHub-Reposatories\\Internship\\LogClass\\output\\binary_sole_open_Apache_aPP_0\\features\\vocab.pkl', 'rb') as f:
    data = pickle.load(f)
print(data)

print("\nTFILF\n")
with open('D:\\GitHub-Reposatories\\Internship\\LogClass\\output\\binary_sole_open_Apache_aPP_0\\features\\tfilf.pkl', 'rb') as f:
    data = pickle.load(f)
print(data)

print("\nPUestimator\n")
with open('D:\\GitHub-Reposatories\\Internship\\LogClass\\output\\binary_sole_open_Apache_aPP_0\\models\\pu_estimator.pkl', 'rb') as f:
    data = pickle.load(f)
print(data)