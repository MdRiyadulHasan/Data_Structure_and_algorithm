def merge_sort(elements):
    if len(elements)<=1:
        return
    mid=len(elements)//2
    left_list = elements[:mid]
    right_list= elements[mid:]
    merge_sort(left_list)
    merge_sort(right_list)
    merge_two_sorted_list(elements, left_list,right_list)
def merge_two_sorted_list(elemnts,left_list,right_list):
    i=j=k=0
    len_left_list=len(left_list)
    len_right_list=len(right_list)
    while i<len_left_list and j<len_right_list:
        if left_list[i]<=right_list[j]:
            elemnts[k]=left_list[i]
            i=i+1
        else:
            elemnts[k]=right_list[j]
            j=j+1
        k=k+1
    while i<len_left_list:
        elemnts[k]=left_list[i]
        i=i+1
        k=k+1
    while j <len_right_list:
        elemnts[k]=right_list[j]
        j=j+1
        k=k+1
if __name__ == '__main__':
    test_case=[
        [10,-5,15,8,18,-12,14],
        [],
        [70,20,30,25,-10,35,45,10],
        [30,25,35,25,-10,12,32,-5,45,24,30]
    ]
    for elements in test_case:
        merge_sort(elements)
        print(elements)