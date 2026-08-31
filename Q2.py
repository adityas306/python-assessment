# 2.What is the difference between break, continue and pass statements? Give a small example. [3 Marks]
# break - break statement used to break
#continue - continue statement used to ignore that particular 
for i in range(1 , 10):
    if(i == 3):
        pass
    if(i == 2):
        continue
    if(i == 8):
        break
    print(i , end=" ")