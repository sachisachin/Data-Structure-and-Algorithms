List = list(map(int,input("Enter the Numbers: ").split(",")))
target = int(input("Enter the Target Element: "))
left = 0
right = len(List)-1
for i in range(len(List)):
    midpoint = (left+right)//2
    if List[midpoint]==target:
        print(f"Target{target} found at index{midpoint}.")
        break
    elif List[midpoint]<target:
        left = midpoint+1
    else:
        right = midpoint-1
else:
    print(f"Target {target} not found in the list")
