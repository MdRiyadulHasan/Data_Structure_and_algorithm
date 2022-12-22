def binary_search_recursive(arr,target,l,r):
    if r<l:
        return -1
    m=(l+r)//2
    if arr[m]==target:
        return m
    elif arr[m]<target:
        l=m+1
    else:
        r=m-1
    return binary_search_recursive(arr,target,l,r)

if __name__ == '__main__':
    arr = [5,6,8,10,12,16,18,19,22,25]
    target = 22
    index = binary_search_recursive(arr,target,0,len(arr)-1)
    if index !=-1:
        print(f'{target} found in position { index}')
    else:
        print(f'{target} not found')
