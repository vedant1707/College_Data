li=[]
n=int(input("Enter Number of Elements in List"))
print("Enter Numbers")
for i in range(n):
    ele=int(input())
    li.append(ele)
l1=[]
for i in li:
    l1.insert(len(l1)-1,i)
print(l1)
