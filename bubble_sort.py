def bubble_sort(element_list):
    n=len(element_list)
    for i in range(n-1):
        for j in range(n-1-i):
            if(element_list[j]>element_list[j+1]):
                temp=element_list[j]
                element_list[j]=element_list[j+1]
                element_list[j+1]=temp
    return element_list
if __name__=='__main__':
    element_list = list(map(int,input().strip().split()))
    sorted_list = bubble_sort(element_list)
    print(f'sorted list is : {sorted_list}')