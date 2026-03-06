text = "Python123Rocks456"
dig_count  = 0
letr_count = 0


for char in text :
    if '0' <= char <= '9' :
      dig_count += 1
    elif ('a' <= char <= 'z') or ('A' <= char <= 'Z') :
      letr_count += 1

print("digits", dig_count)
print("letters", letr_count)