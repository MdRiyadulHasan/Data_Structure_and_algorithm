def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        temp = arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    return arr
if __name__ =='__main__':
    arr = [10,5,7,2,15,1,6]
    ans = insertion_sort(arr)
    print(ans)