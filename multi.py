f = open("sample.txt", "r")
lines = f.readlines()
mystr = 'HAHAHA'.join([line.strip() for line in lines])
print(mystr)
out = mystr.split('HAHAHA')
for line in out:
    print(line)