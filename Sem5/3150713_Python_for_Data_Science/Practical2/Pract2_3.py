r_string=""
s1=[]
n=int(input("Enter Number of Characters you want to enter"))
print("Enter Characters")
for i in range(n):
    ele=(input())
    s1.append(ele)
print("Given list of string is: ",s1,end=" ")
print("\nResulted String is:",end=" ")
print(r_string.join(s1))
