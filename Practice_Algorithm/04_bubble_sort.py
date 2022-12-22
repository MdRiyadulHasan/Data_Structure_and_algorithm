def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
if __name__ == '__main__':
    arr = [5,10,7,2,12,8,6,15,4]
    ans = bubble_sort(arr)
    print(ans)
