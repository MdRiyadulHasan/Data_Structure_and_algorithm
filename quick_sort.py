def pivot_place(elements,first,last):
    pivot=elements[first]
    left=first+1
    right=last
    while True:
        while left<=right and elements[left]<=pivot:
            left=left+1
        while left<=right and elements[right]>=pivot:
            right = right-1
        if right<left:
            break
        else:
            elements[left],elements[right]=elements[right],elements[left]
    elements[first],elements[right]=elements[right],elements[first]
    return right
def quicksort(elements,first,last):
    if first<last:
        p=pivot_place(elements,first,last)
        quicksort(elements, first,p-1)
        quicksort(elements,p+1,last)
if __name__ == '__main__':
    elements=list(map(int, input().strip().split()))
    last=len(elements)-1
    quicksort(elements,0,last)
    print(elements)