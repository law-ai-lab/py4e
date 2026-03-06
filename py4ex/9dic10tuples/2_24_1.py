text = "dog cat dog bird dog"

# word count 作る

words = text.split()

counts = {}

for word in words  :
   counts[word] = counts.get (word, 0) +1

#print(counts)

lst = []

for k,v in counts.items() :
   lst.append((v,k))
   lst.sort(reverse = True)

print(lst[ :3])