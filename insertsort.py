arr = [5,2,4,6,1,3]

for i in range(1,len(arr)):
    for j in range(i):
        while arr[i]<arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
    print(arr)
