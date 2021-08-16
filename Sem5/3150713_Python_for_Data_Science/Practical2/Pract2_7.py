dob={"Vedant":"17/07/2001", "Kunjan":"24/04/2004", "Banish":"16/01/2003",  "Shivam":"18/09/2000"}
name= input("Enter name:")
l1= name.split()

for i in l1:
    if i in dob.keys():
        person=i
        print(" ".join([person,"'s Date Of Birth is :",dob[person]]))
    else:
        print(str(i)+" : Sorry! No Data Found")
