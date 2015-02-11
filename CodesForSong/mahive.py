from operator import itemgetter

f = open("all.txt")
l = f.readlines()
print len(l)
counts = {}
for line in l:
    words = line.split()
    for word in words:
    	a = word.lower()
        if a not in counts:
            counts[a] = 1
        else:
            counts[a] += 1

sort_dict = sorted(counts.values())
print len(counts)
print sort_dict
print counts

for key,values in sorted(counts.items(), key = itemgetter(1), reverse=True):
	print(key,values)