#Stop when they type "done".
#Ignore invalid input.
total = 0
count =0 

while True :
  entry = input( "Enter numbers (or 'done' to stop): ")

  if entry == "done" :
       break
  try :
     num = int(entry)
     total = total + num
     count = count + 1
  except:
     print("invalid input, ignore")


if count > 0 :
 print("total: ", total)
 print("count: ", count)
 print("average: ", total / count)
else:
 print("no numbers are enterd.")