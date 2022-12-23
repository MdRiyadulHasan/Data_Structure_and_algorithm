def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min = i
        for j in range(min+1,n):
            if arr[j]<arr[min]:
                min = j
        if i!=min:
            arr[i],arr[min]=arr[min],arr[i]
    return arr

if __name__ == '__main__':
    arr = [5,3,14,1,-1,0,8]
    ans = selection_sort(arr)
    print(ans)