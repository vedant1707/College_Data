num=[]
n=int(input("Enter Number of Elements in List"))
print("Enter Elements")
for i in range(n):
    ele=int(input())
    num.append(ele)
sum=0
if(num[0]!=13):
    sum+=num[0]
for i in range(1,n):
    if(num[i]!=13):
        if(num[i-1]!=13):
            sum=sum+num[i]
print(sum,"is Sum of Numbers in Array")
