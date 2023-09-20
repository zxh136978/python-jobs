import os

#print(os.getcwd())
path = os.getcwd()

for i in range(1, 101):
    if os.path.exists(os.path.join(path, str(i))):
        continue
    else:
        os.makedirs(os.path.join(path, str(i)))