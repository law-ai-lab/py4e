largest_so_far = None
smallest_so_far = None

while True:
    num = input()
    if num == "done":
        break
    try:
        fval = int(num)
    except:
        print('Invalid input')
        continue
    
    if largest_so_far is None or fval > largest_so_far:
        largest_so_far = fval        # ✅ fixed spelling
    if smallest_so_far is None or fval < smallest_so_far:
        smallest_so_far = fval       # ✅ fixed spelling

print("Maximum is", largest_so_far)
print("Minimum is", smallest_so_far)
