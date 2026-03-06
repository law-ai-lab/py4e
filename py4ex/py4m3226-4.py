#Count both lowercase and uppercase vowels.
text = "Professional Growth"
count = 0

for letter in text :
   if letter in 'aeiouAEIOU' :
    count =  count + 1

print(count)
