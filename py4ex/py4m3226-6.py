#handl = data.txt

fhandl = open("data.txt", "r")

total = 0
largest =None
count = 0

for line in fhandl :
    num = int(line)
    total = total + num
    count = count + 1

    if largest is None or num > largest :
        largest = num

fhandl.close()

average = total / count

print("Total", total)
print("Average", average)
print("Max", largest)