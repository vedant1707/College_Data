l1=[]
n=int(input("Enter Number of Numbers you want to enter"))
print("Enter Numbers")
for i in range(n):
    ele=int(input())
    l1.append(ele)
odd=[]
for i in l1:
    if i%2!=0:
        odd.append(i)
print("\n Resultant List is:",odd)
