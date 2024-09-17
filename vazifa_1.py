import math

lst = ["A","B","C","D","E","F","G","L","Q","U"]

n = int(input("N ni kiriting: "))
new_lst = []
q = 0
#List ichida nechta list borligini aniqlayabman va tashqi for shuncha aylanadi
for i in range(math.ceil(len(lst)/n)):
    new_lst.append([])
    for j in range(n):
        new_lst[i].append(lst[q])
        q += 1
        # Agar berilgan listdagi elementlar tugasa kichik sikl to'xtaydi 
        #  va oxirgi listda sodir bo'lishi mumkin bo'lgan xatolik oldi olindi 
        if q == len(lst):
            break
print(new_lst)
        