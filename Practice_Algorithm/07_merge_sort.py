def merge_sort(arr):
    if len(arr)==1:
        return
    m = len(arr)//2
    left = arr[:m]
    right = arr[m:]
    merge_sort(left)
    merge_sort(right)
    merge(arr,left,right)
def merge(arr,left,right):
    l=r=k=0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            arr[k]=left[l]
            l+=1
        else:
            arr[k]=right[r]
            r+=1
        k+=1
    while l<len(left):
        arr[k]=left[l]
        l+=1
        k+=1
    while r<len(right):
        arr[k]=right[r]
        r+=1
        k+=1
if __name__ == '__main__':
    arr = [5,3,7,1,0,8,5]
    merge_sort(arr)
    print(arr)