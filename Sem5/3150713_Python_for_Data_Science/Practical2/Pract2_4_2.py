sq_li=[]
for i in range(1,31):
    sq_li.append(i**2)
result=sq_li[:5] + sq_li[25:]
print(result,end=" ")
