infile = open("lbs.txt", 'r')
lbs = list()
count = 0
line = infile.readline()

while line !="":
    lbs.append(float(line))
    count += 1
    line = infile.readline()

kilos = [n*0.453592 for n in lbs]

# print(lbs)
print(kilos)