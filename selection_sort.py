def selection_sort(element):
    n=len(element)
    for i in range(n-1):
        min_index=i
        for j in range(min_index+1,n):
            if(element[j]<element[min_index]):
                min_index = j
        element[i],element[min_index]=element[min_index],element[i]
    return element


if __name__ == '__main__':
    element =list(map(int,input().strip().split()))
    sorted_list =selection_sort(element)
    print(f"sorted_list : {sorted_list}")