text = "dog cat dog bird dog"

# word count 作る

words = text.split()


counts = {}

for word in words :
    counts[word] = counts.get(word, 0) + 1

#print(counts)

lst = []

for v, k in counts.items() :
    lst.append((k, v))
    lst.sort(reverse =True)

print (lst[ :3])