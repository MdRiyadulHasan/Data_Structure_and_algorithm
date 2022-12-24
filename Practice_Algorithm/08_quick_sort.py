def partition(arr,first,last):
    pivot = arr[first]
    l=first+1
    r=last
    while l<r:
        while arr[l]<pivot:
            l+=1
        while arr[r]>pivot:
            r-=1
        if l<r:
            arr[l],arr[r]=arr[r],arr[l]
    arr[first],arr[r]=arr[r],arr[first]
    return r
def quick_sort(arr,first,last):
    if first<last:
        p = partition(arr,first,last)
        quick_sort(arr,first,p-1)
        quick_sort(arr,p+1,last)


if __name__ =='__main__':
    arr = [29,99,27,41,66,28,44,78,87,19,12,21,44]
    first = 0
    last = len(arr)-1
    quick_sort(arr,first,last)
    print(arr)
    