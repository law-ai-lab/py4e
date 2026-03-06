text = " a b a c a"

# word count 作る

words = text.split()

counts = {}

for word in words:
    counts[word] = counts.get(word,0) + 1

print(counts)
