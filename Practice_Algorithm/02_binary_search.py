def binary_search(arr,target):
    l=0
    r = len(arr)-1
    while l<=r:
        m = (l+r)//2
        if arr[m]==target:
            return m
        elif arr[m]<target:
            l=m+1
        else:
            r=m-1
    return -1
if __name__ == '__main__':
    arr = [ 2, 3, 4, 10, 15, 20, 25, 35, 40]
    target = 22
    index = binary_search(arr,target)
    if index !=-1:
        print(f'{target} found at position { index}')
    else:
        print(f'{target} not found')