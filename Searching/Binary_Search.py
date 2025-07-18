def binary_search(arr:list[int],target:int,low:int,high:int)->int:
    if low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            return binary_search(arr,target,mid+1,high)
        else:
            return binary_search(arr,target,low,mid-1)
    else:
        return -1
#main function to test the binary_search function
if __name__=="__main__":
    arr=[1,7,13,15,20,50]
    target=15
    print("Binary Search")
    result=binary_search(sorted(arr),target,0,len(arr)-1)
    if result!=-1:
        print(f"Found element at index {result}")
    else:
        print("Not found")