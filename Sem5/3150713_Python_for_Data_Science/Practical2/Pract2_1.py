num=[]
n=int(input("Enter Number of Elements in List"))
print("Enter Numbers: ")
for i in range(0,n):
    ele=int(input())
    num.append(ele)
max=num[0]
for i in range(1,n):
    if(num[i]>max):
        max=num[i]
print(max,"is Greatest Element")
