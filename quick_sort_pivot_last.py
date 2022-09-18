def pivot_place(elements,first,last):
    pivot=elements[last]
    left=first
    right=last-1
    while True:
        while left<=right and elements[left]<=pivot:
            left=left+1
        while left<=right and elements[right]>=pivot:
            right=right-1
        if right<left:
            break
        else:
            elements[left],elements[right]=elements[right],elements[left]
    elements[last],elements[left]=elements[left],elements[last]
    return left

def quicksort(elements,first,last):
    
    if first<last:
        p=pivot_place(elements,first,last)
        quicksort(elements,first,p-1)
        quicksort(elements,p+1,last)

if __name__ == '__main__':
    elements=list(map(int,input().strip().split()))
    last=len(elements)-1
    first=0
    quicksort(elements,first,last)
    print(elements)