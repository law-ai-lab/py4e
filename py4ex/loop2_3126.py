text = "I believe in Python"
count = 0

for letter in text :
    if letter in 'aeiou' :
       count = count + 1

print(count)
#Count how many vowels appear. (a, e, i, o, u — lowercase only for now)