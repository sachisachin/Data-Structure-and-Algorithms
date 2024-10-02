List = list(map(int,input("Enter the Numbers: ").split(",")))
target = int(input("Enter the Target Element: "))
for i in range(len(List)):
    if List[i]==target:
        print(f"Target {target} found at index {i}.")
        break
else:
        print(f"Target {target} not found in list")