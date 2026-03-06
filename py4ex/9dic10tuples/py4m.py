text = "applr banana apple orange apple banana"

words = text.split()

counts ={}

for word in words:
    counts[word] = counts.get(word, 0) + 1

lst = []

for key, val in counts. items() :
    lst.append((val, key))

lst.sort(reverse=True)

for count, word in lst[ :3] :
    print(word, count)

print(lst)
