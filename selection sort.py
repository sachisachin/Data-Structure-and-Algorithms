List = list(map(int,input("Enter the Numbers: ").split(",")))
for i in range(0,len(List)):
    for j in range(i+1,len(List)):
        if List[j] < List[i]:
            temp = List[j]
            List[j] = List [i]
            List[i] = temp
print("The Sorted Result is : ",List)